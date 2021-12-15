---
title: Setup
---

{% if site.carpentry == "rsg" %}
  {% assign slidelink = "slides/project-novice-lesson/index.html" %}
{% else %}
  {% assign slidelink = "slides/index.html" %}
{% endif %}

Before we get started, there are a few requirements to meet. You will need:

* [A GitHub account](https://github.com)
* A GitHub repository titled `climate-analysis`
* A code editor (we recommend [Visual Studio Code](https://code.visualstudio.com/))

If you do not have a `climate-analysis` repository, you can create an empty one now. No specific contents are required for this lesson.

Once you're all set up, [we can start the course](project-novice-introduction). The slides for this course [can be found here]({{ slidelink }}).

{% include links.md %}
