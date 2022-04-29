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

> ## Identifying issues
>
> Earlier, we made a fork of the `rf4` repository. The code there is pretty bad- it's written in a very unsustainable way that makes future development harder (and passing the project on to another researcher even harder!). However, as a published project owned by somebody else, we don't have the permissions required to edit it and fix the problems.
>
> Fortunately, we have already forked it, and now we're going to set up a small project to improve it. Take a look at your fork of the `rf4` repository, identify three problems with the code, and raise them as issues. Forks don't have **Issues** by default, but you can enable them using **Settings -> Options -> Features**.
>
> Don't try to run the code- there's more than enough things wrong with it that you can spot just from a quick read-through.
>
> Once you've got your issues, create a kanban board on the repo and place them on it.
>
> > ## Solution
> >
> > There's too many things wrong to provide an exhaustive list, but here's a few you may have spotted:
> > * No stable releases
> > * No development branch
> > * Unclear commit messages
> > * `LICENSE.md` is empty
> > * `README.md` has an inaccurate list of files
> > * `README.md` contains broken links
> > * `What questions do we want to answer with this data?` is unfinished
> > * Multiple versions of the same file in the repository
> > * Poorly-named functions (e.g. `add_column5`)
> > * Poorly-named variables (e.g. `df47`)
> > * Poorly-documented functions *(e.g. `plot_bar_charts`)
> > * Undocumented functions (e.g. `produce_count`)
> 
{: .solution}

{: .challenge}

> ## Solving problems
> 
> Now we've got a project board with all our problems in the To Do column, we can set about fixing one of the issues.
> 
> We want to use the feature-branch workflow, so it would be easy to collaborate with other people. Pick one of your open issues, and fix it using the feature-branch workflow, then once it's done issue a release of your updated `master` branch!
>
> > ## Solution
> >
> > In order to address the issue we chose, we'll need to do the following:
> > * Move our issue from To Do to Work In Progress
> > * Select our `master` branch, and create a `dev` branch coming off it
> > * Select our `dev` branch, and create a new issue branch coming off it- you could call it `issue_<problem_description>` or similar
> > * Switch to our issue branch, fix the issue, commit our fixes and push them
> > * Submit a pull request from our issue branch to `dev`
> > * Close our issue on GitHub
> > * When `dev` is up to date, submit a pull request from `dev` to `master`
> > * When `master` is up to date, issue a release on GitHub
> >
> > Normally, we wouldn't just merge a branch into `dev` then `dev` straight into `master`- we'd merge several fixes or new features into `dev`, then merge to `master` and make a release. 
> 
{: .solution}

{: .challenge}

Now you should have a good idea of the skills and techniques required to manage a project successfully!

{% include links.md %}
