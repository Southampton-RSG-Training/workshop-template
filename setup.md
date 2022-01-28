
### Text Editor

A text editor is the piece of software you use to view and write code. If you
have a preferred text editor, please use it. Suggestions for text editors are,
Notepad++ (Windows), TextEdit (macOS), Gedit (GNU/Linux), GNU Nano, Vim.
Alternatively, there are IDE's (integrated developer environments) that have
more features specifically for coding such as VS Code; there are also IDEs
specific to languages will be listed in the appropriate section(s) below.

### Version Control with git

#### Git Setup 

{% if site.carpentry == "rsg" %}
  {% assign slidelink = "slides/git-novice-lesson/index.html" %}
{% else %}
  {% assign slidelink = "../slides/index.html" %}
{% endif %}

[The slides to accompany this material can be found here.]({{ slidelink }})
Before we get started, we'll have to do a few things.

![Setup](fig/slides/setup.png){:width="20%"}

Later on in the session, we'll be demonstrating how to share work with collaborators using GitHub. You'll need to create an account there: [https://github.com/](https://github.com/).

As your GitHub user name will appear in the URLs of your projects there, it's best to use a short, clear version of your name if you can.

In addition we will need to set up SSH access to GitHub from your computer. This is how GitHub checks that you are who you say you are when you try to add things from your computer.

When we do this, we generate a pair of keys - one public, one private. We want to add the public key to GitHub, whilst the private one stays on our computer.

There are full guides here [https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent](Make an SSH Key) and [https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account](Add an SSH key).

However today we have simplified it like so:

First we need to create a variable to store your GitHub email. Copy this command, substituting the email you signed up to GitHub with for `your_github_email@example.com`:
~~~
$ my_gh_email=your_github_email@example.com
~~~
{: .language-bash}

Then we can run the following command to generate a key-pair and display the public half:
~~~
$ ssh-keygen -t ed25519 -C $my_gh_email; eval "$(ssh-agent -s)"; ssh-add ~/.ssh/id_ed25519; cat ~/.ssh/id_ed25519.pub
~~~
{: .language-bash}

You will need to press enter a few times to select default options and set the passphrase to empty.

Copy the last output line that starts with `ssh-ed25519` and ends with your email (it may have gone over multiple lines if your terminal isn't wide enough).

![SSH-Output](fig/SSH-Output.png){:width="50%"}

Finally, go to [https://github.com/settings/ssh/new](https://github.com/settings/ssh/new) (you will need to be logged into GitHub with the account you have created). Give the key a memorable name (the name of the computer you are working on is often a good choice) and paste the key from your clipboard into the box labelled key. Then, click add SSH key and you are done!

![SSH-Add](fig/SSH-Add.png){:width="50%"}

Now we are ready to download the code that we need for this lesson, using Git on the command line. Open a terminal on your machine, and enter:
~~~
$ cd
$ git clone https://github.com/Southampton-RSG/swc-git-novice
~~~
{: .language-bash}


`cd` will move to your home directory, and `git clone` will download a copy of the materials.
Once you're all set up, [we can start the course](git-novice-what-is-version-control).

{% include links.md %}

### Building Programs with Python

#### Python Setup 

IDEs: PyCharm, Spyder, VS Code

We use Python 3, because it is generally the most widely used version of Python. The “Anaconda3” package provides everything Python-related you will need for the workshop. To install [Anaconda](https://www.anaconda.com/products/individual), follow the instructions below.

##### Windows
Download the latest Anaconda Windows installer. Double click the installer and follow the instructions. When asked “Add Anaconda to my PATH environment variable”, answer “yes”. After it’s finished, close and reopen any open terminals to reload the updated PATH and allow the installed Python to be found.

##### Mac OS X
Download the latest Anaconda Mac OS X installer. Double click the .pkg file and follow the instructions.

##### Linux
Download the latest Anaconda Linux Installer. Install via the terminal like this,

~~~
$ bash Anaconda3-2021.11-Linux-x86_64.sh
~~~
{: .language-bash}

Answer ‘yes’ to allow the installer to initialize Anaconda3 in your .bashrc.

### Data Analysis and Visualization in R

#### Data Analysis and Visualization in R
R is a programming language and software environment for statistical computing and graphics. The RStudio Integrated Development Environment (IDE) is a set of tools designed to help you be more productive with R.

We need to install R and RStudio: 
The latest links can be found on the [RStudio downloads page](https://www.rstudio.com/products/rstudio/download/#download)

##### R

R can be found at [https://cran.rstudio.com/](https://cran.rstudio.com/), from here pick your OS and download the latest release, see below for direct links to your OS.

##### Windows
- [https://cran.rstudio.com/bin/windows/base/](https://cran.rstudio.com/bin/windows/base/)

##### Mac OS
- If prompted, choose to allow downloads from cran.rstudio.com.

- [https://cran.rstudio.com/bin/macosx/](https://cran.rstudio.com/bin/macosx/)
  - For intel based macs choose R-4.*.*.pkg
  - For ARM based macs (M1 etc.) choose R-4.*.*-arm64.pkg

##### Linux
- R is included on many linux distros check to see if it is already present. Else use your package manager (snap, apt, yum), or look [here](https://cran.rstudio.com/bin/linux/)


##### RStudio

Your OS should be detected and a link provided under step 2 on this page [RStudio downloads page](https://www.rstudio.com/products/rstudio/download/#download).
Else select your OS from the list under All Installers.

##### Windows

Download and run the .exe file and follow instructions given by your OS.

##### Mac OS

Download the .dmg file.
- If prompted, choose to allow downloads from rstudio.com.
- Open the downloaded dmg archive from the Downloads folder.
- Drag the RStudio icon to the Applications folder to install.
