"""Remove the front matter and change the depth of headers.

This script deals with removing the front matter
"""

import yaml
import re


NHEAD = 5


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


def get_content_and_head(file):
    """Get the content and the head of the file.

    Args:
        file: The file to read.
    Returns:
        A tuple of the content and the head.
    """
    with open(file, "r") as fp:
        content = fp.read()
        fp.seek(0)
        head = [next(fp) for _ in range(NHEAD)]

    return content, head


def write_modified_file(file, content):
    """Write the modified contents to file.

    Args:
        file: The file to write to.
        content: The content to write.
    """
    with open(file, "w") as fp:
        fp.write(content)


config = get_yaml_config("_config.yml")

for lesson in config["lessons"]:

    file = f"_includes/rsg/{lesson['gh-name']}-lesson/setup.md"
    content, head = get_content_and_head(file)
    content = content.splitlines()

    # Remove front matter from the markdown

    if re.findall("---", "\n".join(head)):
        n_found = 0
        for i, line in enumerate(content):
            if line == "---":
                n_found += 1
            if n_found == 2:
                break
        content = content[i + 1:]

    # Change the depth of headings to be a consistent style with the workshop
    # homepage

    for i, line in enumerate(content):

        if line.startswith("#"):
            line = line.rstrip("#")
            hashes = "#" * (line.count("#") + 2)
            content[i] = f"{hashes} {line.lstrip('#')}"

    # Put back into lines and overwrite the file

    content = "\n".join(content)
    write_modified_file(file, content)