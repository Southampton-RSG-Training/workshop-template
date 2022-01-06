
### Text Editor

A text editor is the piece of software you use to view and write code. If you
have a preferred text editor, please use it. Suggestions for text editors are,
Notepad++ (Windows), TextEdit (macOS), Gedit (GNU/Linux), GNU Nano, Vim.
Alternatively, there are IDE's (integrated developer environments) that have
more features specifically for coding such as VS Code; there are also IDEs
specific to languages will be listed in the appropriate section(s) below.

### Automating Tasks with the Unix Shell

#### Shell Setup 

You need to download some files to follow this lesson. First, you need to open a terminal:

- **On Windows:** run "Git Bash", which you installed as part of the software prerequisites
- **On Mac OS X:** accessed by opening the “Terminal” application, which can be found in the “Utilities” folder which is in your “Applications” folder
- **On Linux:** this will depend on the Linux distribution you are running, but you should be able to find a "Terminal" application in your desktop's application menu

Once you've done this, a window should appear. Type the following into the prompt that appears (pressing enter/return after each line):

~~~
$ cd
$ git clone https://github.com/Southampton-RSG/shell-novice.git
~~~
{: .language-bash}

Alternatively, if you have SSH authentication with GitHub enabled (if you don't know what this means don't worry, it is covered in the Git SWC course if you want to know more!) you can use the following:

~~~
$ cd
$ git clone git@github.com:Southampton-RSG/swc-shell-novice.git
~~~
{: .language-bash}

This should download all the content for the lesson to a new directory.
Please let the instructors know if you run into any problems.

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
