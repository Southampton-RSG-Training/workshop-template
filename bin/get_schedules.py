"""Create schedule for the workshop.

Reads the lessons.yml configuration file to determine the lessons, then parses
the schedules from each lesson and adds a delta time to the start time of each
schedule depending on the start time of the lesson. The scheduled for each
lesson are then put into a single schedule (split by tables) and written to
the main schedule.html file. There are a maximum of two tables per row.
"""

import datetime
import yaml
import pandas
from bs4 import BeautifulSoup as bs


def get_yaml_config(yaml_file):
    """Read a yaml file and return a dictionary of its contents.

    Args:
        lessons_file: The path to the lessons.yml file.

    Returns:
        A dictionary of lessons.
    """
    with open(yaml_file, "r") as fp:
        config = yaml.load(fp, yaml.Loader)

    return config


def get_start_time_object(lesson_start_time):
    """Return a datetime object from a string.

    Args:
        lesson_start_time: The string to convert to a datetime object.

    Returns:
        A datetime object.
    """
    if isinstance(lesson_start_time, str):
        try:
            time = datetime.datetime.strptime(lesson_start_time, "%I:%M %p")  # start-time: 9:30 am
        except ValueError:
            time = datetime.datetime.strptime(lesson_start_time, "%H:%M")     # start-time: "9:30"
    elif isinstance(lesson_start_time, int):
        hours, minutes = divmod(lesson_start_time, 60)
        time = datetime.datetime.strptime(f"{hours}:{minutes}", "%H:%M")      # start-time: 9:30
    else:
        raise ValueError(f"Invalid time string format for start-time: {lesson_start_time}")

    return time


workshop_config = get_yaml_config("_config.yml")
html_schedule = "<div class=\"row\">"

# Go through each lesson to get and update the schedule, depending on start time

for i, lesson in enumerate(workshop_config["lessons"]):

    lesson_title = lesson.get("title", None)
    lesson_name = lesson.get("gh-name", None)
    lesson_date = lesson.get("date", None)
    lesson_start = lesson.get("start-time", None)

    if [thing for thing in (lesson_name, lesson_date, lesson_title, lesson_start) if thing is None]:
        raise ValueError(f"gh-name, date, title, and start-time are required for each lesson")

    # Want these as a list, to loop over later

    if not isinstance(lesson_date, list):
        lesson_date = [lesson_date]
    if not isinstance(lesson_start, list):
        lesson_start = [lesson_start]

    # Get the schedules and html for each lesson

    with open(f"_includes/rsg/{lesson_name}-lesson/schedule.html", "r") as fp:
        schedule_html = fp.read()

    schedule_soup = bs(schedule_html, "html.parser")
    schedule_tables = pandas.read_html(schedule_html, flavor="bs4")

    assert len(lesson_date) == len(schedule_tables), f"{lesson_name} config has {len(schedule_tables)} schedules but {len(lesson_date)} lesson dates"
    assert len(lesson_start) == len(schedule_tables), f"{lesson_name} config has {len(schedule_tables)} schedules but {len(lesson_start)} start times"

    # Loop over each schedule table, if the event is multi-day

    n_tables_in_row = 0

    for j, schedule in enumerate(schedule_tables):

        schedule.columns = ["time", "session"]
        permalink = schedule_soup.find_all("a", href=True)[j]["href"]  # assumes each table has a link to a episode
        lesson_start = get_start_time_object(lesson_start[j])
        date = lesson_date[j]

        # Calculate the time difference between the start time, and the start
        # time in the original schedule. This delta time (in minutes) is added
        # to each time in the original schedule

        original_start_time = get_start_time_object(schedule["time"][0])
        delta_start = divmod((lesson_start - original_start_time).total_seconds(), 60)[0]

        # Construct the schedule table for this lesson, adding delta_minutes to
        # each original entry, and add the schedule table to the html template

        if len(schedule_tables) > 1:
            table_title = f"Day {j + 1} - {lesson_title}"
        else:
            table_title = lesson_title

        table_html = f"""
        <div class="table-responsive col-md-6">
            <a href="{permalink}"><h3>{table_title}</h3></a>
            <h4>{date}</h4>
            <table class="table table-striped">
        """

        for time, session in zip(schedule["time"], schedule["session"]):
            actual_time = datetime.datetime.strptime(time, "%H:%M") + datetime.timedelta(minutes=delta_start)
            table_html += f"<tr> <td> {actual_time.hour:02d}:{actual_time.minute:02d} </td> <td> {session} </td> </tr>\n"

        table_html += "    </table></div>"
        n_tables_in_row += 1

        if n_tables_in_row % 2 == 0:
            table_html += "</div>"

    html_schedule += table_html

# Finish off the template and use BeautifulSoup to write a pretty version of
# the html file (which is not that pretty, actually)

html_schedule += "</div>"

with open("_includes/rsg/schedule.html", "w") as fp:
    fp.write(bs(html_schedule, "html.parser").prettify())
