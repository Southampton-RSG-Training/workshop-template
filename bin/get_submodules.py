"""Parse the curriculum collection (from _config.yml) and place the content
from each lesson into the appropriate directory structure.
"""

import os
import logging
from shutil import copy2 as copy
from shutil import rmtree
from shutil import copytree
from pathlib import Path
from typing import Tuple

from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
import requests
from requests.exceptions import ConnectTimeout

log = logging.getLogger(__name__)


def check_org_name_and_branch(lesson_name: str, org_name: str, gh_branch: str) -> Tuple[str, str]:
    """
    Check the GH org name and branch are correct for a lesson.

    This checks to see if the provided org_name and gh_branch all
    work with the lesson provided by lesson_name. If either org_name or
    gh_branch are correct, e.g. the GitHub API returns an error or times out,
    then default values are tried for gh_page or org_name

    Parameters
    ----------
    lesson_name:
        The name of the lesson to check
    org_name:
        The proposed org name where the lesson repo should exist.
    gh_branch:
        The proposed branch of the repo containing the lesson.
    """
    ret_org_name = org_name
    ret_gh_branch = gh_branch

    try:
        r = requests.get(f'https://api.github.com/repos/{org_name}/{lesson_name}', timeout=7)
    except ConnectTimeout as exc:
        raise Exception(f"Connection timeout when trying to find {org_name}/{lesson_name} repository") from exc

    if r.status_code != 200:
        log.warning(f'Lesson {lesson_name} does not exist in {org_name} trying in default org')

        try:
            r = requests.get(f'https://api.github.com/repos/Southampton-RSG-Training/{lesson_name}', timeout=7)
        except ConnectTimeout as exc:
            raise Exception(f"Connection timeout when trying to find Southampton-RSG-Training/{lesson_name} repository") from exc

        if r.status_code == 200:
            log.warning(f"Lesson {lesson_name} found in 'Southampton-RSG-Training' using as fallback")
            ret_org_name = "Southampton-RSG-Training"
        else:
            raise ValueError(f"Lesson {lesson_name} does not exist in '{org_name}', or 'Southampton-RSG-Training'")
    else:
        try:
            r = requests.get(f'https://api.github.com/repos/{org_name}/{lesson_name}/branches/{gh_branch}', timeout=7)
        except ConnectTimeout as exc:
            raise Exception("Connection timeout when trying to find {gh_branch} branch in {org_name}/{lesson_name}") from exc

        if r.status_code != 200:
            log.warning(f'Branch {gh_branch} does not exist in {org_name}/{lesson_name} trying default branch')

            try:
                r = requests.get(f'https://api.github.com/repos/{org_name}/{lesson_name}/branches/gh-pages', timeout=7)
            except ConnectTimeout as exc:
                raise Exception("Connection timeout when trying to find gh-pages branch in {org_name}/{lesson}") from exc

            if r.status_code == 200:
                log.warning(f'Branch {gh_branch} found in {org_name}/{lesson_name} using as fallback')
                ret_gh_branch = "gh-pages"
            else:
                raise ValueError(f"Branch '{gh_branch}' or 'gh-pages' does not exist in '{org_name}/{lesson_name}', or 'Southampton-RSG-Training'")

    return ret_org_name, ret_gh_branch


# Remove previously existing directories, to start fresh

rmtree("submodules", ignore_errors=True)
# rmtree("slides", ignore_errors=True)

Path("submodules").mkdir(parents=True, exist_ok=True)

# Open the website config, which contains a list of the lessons we want in the
# workshop, then create the directory "submodules" which will contain the files
# for each lesson

with open('_config.yml', 'r') as config:
    website_config = load(config, Loader=Loader)

log.info(f"Getting submodules specified in {website_config['lessons']}")

# Now process each lesson in the list

for n, lesson_info in enumerate(website_config['lessons']):

    # Create the command to pull the sub-directory from GitHub
    org_name = lesson_info.get("org-name", "Southampton-RSG-Training")
    lesson_name = lesson_info.get('gh-name', None)
    if not lesson_name:
        raise ValueError(f"No lesson name specified for lesson {n}")
    gh_branch = lesson_info.get('branch', 'main')

    org_name, gh_branch = check_org_name_and_branch(lesson_name, org_name, gh_branch)
    log.info(f"Getting lesson with parameters:\n org-name: {org_name} \n gh-name: {lesson_name} \n branch: {gh_branch}")

    os.system(f"git submodule add --force -b {gh_branch} https://github.com/{org_name}/{lesson_name}.git submodules/{lesson_name}")
    os.system("git submodule update --remote --merge")

    # move required files from the subdirectories to _includes/rsg/{lesson_name}/...
    # lesson destinations need to be appended with -lesson to avoid gh-pages naming conflicts

    # Things to move to ./_includes/rsg
    includes_dest = f"_includes/rsg/{lesson_name}-lesson"
    Path(includes_dest).mkdir(parents=True, exist_ok=True)

    for file in ["blurb.html"]:
        try:
            copy(f"submodules/{lesson_name}/{file}", f"{includes_dest}/{file.split('/')[-1]}")
            log.info(f"Copied submodules/{lesson_name}/{file} to {includes_dest}")
        except IOError:
            log.error(f"Cannot find or move submodules/{lesson_name}/{file}, but carrying on anyway")

    # Move lesson episodes into the _episodes directory
    lesson_content_dest = f"_episodes/{lesson_name}-lesson"
    Path(lesson_content_dest).mkdir(parents=True, exist_ok=True)
    copytree(f"submodules/{lesson_name}/_episodes/", lesson_content_dest, dirs_exist_ok=True)

    # move any extra lesson files into the same directory as the episodes, e.g.
    # the glossary is a good example
    for file in ["reference.md"]:
        try:
            copy(f"submodules/{lesson_name}/{file}", f"{lesson_content_dest}/{file.split('/')[-1]}")
        except IOError:
            log.error(f"Cannot find or move submodules/{lesson_name}/{file}, but carrying on anyway")

    # now we need to add two additional frontmatter variables to link the
    # lesson episodes to the correct syllabus/schedule
    for file in os.listdir(lesson_content_dest):
        if file.endswith(".md"):
            with open(f"{lesson_content_dest}/{file}", "r") as f:
                contents = f.readlines()
            contents.insert(
                1,
                f"lesson_title: '{lesson_info.get('title', '')}'\nlesson_schedule_slug: {lesson_name}-schedule\n"
            )
            with open(f"{lesson_content_dest}/{file}", "w") as f:
                f.write("".join(contents))

    # Moves figures into fig directory
    try:
        copytree(f"submodules/{lesson_name}/fig", "fig/", dirs_exist_ok=True)
    except IOError:
        log.info(f"No figures to move for {lesson_name}")

    # Move lesson data into data directory
    try:
        copytree(f"submodules/{lesson_name}/data", "data/", dirs_exist_ok=True)
    except IOError:
        log.info(f"No data file to move for {lesson_name}")

    # Move codes for lessons into code directory
    try:
        copytree(f"submodules/{lesson_name}/code", "code/", dirs_exist_ok=True)
    except IOError:
        log.info(f"No code files for {lesson_name}")

# Now need to do copy the slides over, but have to do it afterwards because we
# need a specific version of reveal.js and so we need to avoid the git submodule
# update

os.system("git submodule add --force https://github.com/hakimel/reveal.js.git submodules/reveal.js")
os.system("cd submodules/reveal.js && git checkout 8a54118f43")

for n, lesson_info in enumerate(website_config['lessons']):
    # if we've gotten here, am gonna assume lesson_name exists
    lesson_name = lesson_info.get('gh-name', None)
    slides_src = Path(f"submodules/{lesson_name}/slides")
    # not all lessons have slides, so check the dir exists
    if slides_src.is_dir():
        slides_dest = Path(f"slides/{lesson_name}/")
        slides_dest.mkdir(parents=True, exist_ok=True)
        copytree(f"submodules/{lesson_name}/slides", str(slides_dest), dirs_exist_ok=True)

        # The lesson reveal.js folder which gets copied is empty, so delete that
        # and copy the reveal.js submodule
        rmtree(f"slides/{lesson_name}/reveal.js", ignore_errors=True)
        Path(f"slides/{lesson_name}/reveal.js").mkdir(parents=True, exist_ok=True)
        copytree("submodules/reveal.js", f"slides/{lesson_name}/reveal.js", dirs_exist_ok=True)

        # slides are built using pandoc in this script -- sometimes we seem to
        # need to specify revealjs-url
        pandoc_command = "pandoc -t revealjs -s -o index.html index.md -V theme=black --slide-level=3 "
        pandoc_command += "revealjs-url='https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.9.2'"

        os.system(f"cd slides/{lesson_name} && {pandoc_command}")
