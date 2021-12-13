"""Build the dynamic parts of the workshop website.

This script deals with pulling in the lesson submodules, as well as building
the static parts of the website such as the schedules.
"""

import yaml
import re

n_head_lines = 20

with open("_config.yml", "r") as fp:
    website_config = yaml.load(fp, yaml.Loader)

for lesson in website_config["lessons"]:

    name = lesson["gh-name"]
    setup_file = f"_includes/rsg/{name}-lesson/setup.md"

    with open(setup_file, "r") as fp:
        content = fp.read()
        fp.seek(0)
        head = [next(fp) for _ in range(n_head_lines)]

    search = re.findall("---", "\n".join(head))

    if len(search) == 2:
        content = content.splitlines()
        n_found = 0
        for i, line in enumerate(content):
            if line == "---":
                n_found += 1
            if n_found == 2:
                break
        content = "\n".join(content[i + 1:])

    with open(setup_file, "w") as fp:
        fp.write(content)


