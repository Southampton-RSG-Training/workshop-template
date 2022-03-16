---
title: "Managing a Mini-Project"
slug: project-novice-managing-a-mini-project
teaching: 0
exercises: 20
questions:
- "How do we put everything we've learnt together?"
objectives:
- "Go through the steps of managing a small software project."
keypoints:
- "Problems with code and documentation can be tracked as issues."
- "Issues can be managed on a project board."
- "Issues can be fixed using the feature-branch workflow."
- "Stable versions of the code can be published as releases."
---

Now we've seen all the steps involved in developing sustainable code, let's put that knowledge into practise.

Earlier, we made a fork of the [project-novice-demo](https://github.com/Southampton-RSG-Training/project-novice-demo) repository. The code there is pretty bad - it's written in a very unsustainable way that makes future development harder (and passing the project on to another researcher even harder!). However, as a published project owned by somebody else, we don't have the permissions required to edit it and fix the problems.

Fortunately, we've already forked it, so we can set up a small project to improve it. We want to find the problems, record them as **Issues**, then fix the issues.

The first thing we can spot is that there's no `dev` branch - only a `master` one:

![Current branches](fig/06-project/branch-list.png)

As we mentioned earlier, this makes it difficult to work as part of a team, or to have a stable version to distribute whilst you continue working on the code. So let's make an Issue for this as we showed in the [Issues](fig/02-issues/index.html) section:

![Creating an Issue for the dev branch](fig/06-project/create-issue.png)

Now we're starting to log issues with our code, we want to be able to keep track of them, so we make a new project board as we showed in the [Project Management](03-boards/index.html) section:

![Dragging an Issue onto a project board](fig/06-project/project-new.png)
![Dragging an Issue onto a project board](fig/06-project/project-next.png)
![Dragging an Issue onto a project board](fig/06-project/project-created.png)

Finally, we put the issue we just raised onto the project board we just set up:

![Dragging an Issue onto a project board](fig/06-project/create-issue-next.png)

We've now practised the workflow we identified earlier on a new repository.

> ## Identifying issues
> We've identified one problem with the code - the lack of a `dev` branch. Have a quick look through the project, and identify two more problems and raise them as issues then put them on our project board. Don't try to run the code- there's more than enough things wrong with it that you can spot just from a quick read-through.
>
> > ## Solution
> >
> > There's too many things wrong to provide an exhaustive list, but here's a few you may have spotted:
> > * No stable releases
> > * Unclear commit messages
> > * `LICENSE.md` is empty
> > * `README.md` has an inaccurate list of files
> > * `README.md` contains broken links
> > * `What questions do we want to answer with this data` is unfinished
> > * Multiple versions of the same file in the repository
> > * Poorly-named functions (e.g. `add_column5`)
> > * Poorly-named variables (e.g. `df47`)
> > * Poorly-documented functions *(e.g. `plot_bar_charts`)
> > * Undocumented functions (e.g. `produce_count`)
> {: .solution}
{: .challenge}

Now that we've identified some of the many, many problems with the repository, we'd like to start fixing them. First, let's fix the issue with the lack of a `dev` branch. We'll clone the repository locally, create a new `dev` branch, and push it back to our fork:

~~~
$ git clone git@github.com:smangham/project-novice-demo
~~~
{: .language-bash}
~~~
Cloning into 'project-novice-demo'...
remote: Enumerating objects: 28, done.
remote: Counting objects: 100% (28/28), done.
remote: Compressing objects: 100% (17/17), done.
remote: Total 28 (delta 13), reused 20 (delta 10), pack-reused 0
Receiving objects: 100% (28/28), 8.32 KiB | 8.32 MiB/s, done.
Resolving deltas: 100% (13/13), done.
~~~
{: .output}

~~~
$ cd project-novice-demo
$ git checkout -b dev
~~~
{: .language-bash}
~~~
Switched to a new branch 'dev'
~~~
{: .output}

~~~
$ git push -u origin dev
~~~
{: .language-bash}
~~~
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote: Create a pull request for 'dev' on GitHub by visiting:
remote:      https://github.com/smangham/project-novice-demo/pull/new/dev
remote:
To github.com:smangham/project-novice-demo
 * [new branch]      dev -> dev
branch 'dev' set up to track 'origin/dev'.
~~~
{: .output}

Now, we can close our issue as fixed:

![Closing an issue](fig/06-project/close-issue.png)

Then move it to the **Done** column on our project board:

![Moving an issue to 'Done' on a project board](fig/06-project/close-issue-project.png)

> ## Solving problems
> 
> Now we've got a project board with all our problems in the To Do column, and a `dev` branch to work from, we can set about fixing one of the other issues.
> 
> Pick one of your open issues, and fix it using the feature-branch workflow, then once it's done issue a release of your updated `master` branch as we showed in the [Release Management](04-release/index.html) section!
>
> > ## Solution
> >
> > In order to address the issue we chose, we'll need to do the following:
> > * Move our issue from To Do to Work In Progress
> > * Select our `dev` branch, and create a new issue branch coming off it - you could call it `issue_<problem_description>` or similar
> > * Switch to our issue branch, fix the issue, commit our fixes and push them to GitHub
> > * Submit a pull request from our issue branch to `dev`
> > * Close our issue on GitHub
> > * When `dev` is up to date, submit a pull request from `dev` to `master`
> > * When `master` is up to date, issue a release on GitHub
> >
> > Normally, we wouldn't just merge a branch into `dev` then `dev` straight into `master`- we'd merge several fixes or new features into `dev`, then merge to `master` and make a release. 
> {: .solution}
{: .challenge}

Now you should have a good idea of the skills and techniques required to manage a project successfully!

{% include links.md %}
