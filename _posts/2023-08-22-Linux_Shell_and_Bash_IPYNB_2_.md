---
toc: True
comments: False
layout: post
title: Linux Shell and Bash
tags: ['hacks']
categories: ['CSP', 'Week 1']
---

### Command Cheat Sheet

- `ls`
  - List files in a directory
- `git`
  - `git clone <link>`
  - Makes a clone of a repository (code database)
- `apt`
  - Package manager for linux
- `cd`
  - Change directory
  - Change the directory that you're in
- `cat`
  - Output the contents of a file into terminal
- `rm`
  - Remove a file
- `mkdir`
  - Make a directory
  - `rmdir`
    - Remove a directory
- `clear`
  - Clear terminal
- `man`
  - Display man page of a command (the user MANual)
- `sudo`
  - Execute with superuser privileges (admin)

### Tool Verification & Revisions

Just like how a builder needs a hammer to make a house, they also want to make sure that their hammer is going to last. They want to verify whether they have a good hammer or not and if they even have the correct hammer in the first place.

Depending on the tool you've installed, there will most likely be some way to verify it. It's reccomended to search up the correct way to do it, since the method may vary.

Easy script to check versions:

```bash
# Show the active Ruby version, MacOS is 3.1.4
ruby -v

# Show active Python version, it needs to be 3.9 or better
python --version
# Setup Python libraries for Notebook conversion
pip install nbconvert  # library for notebook conversion
pip install nbformat  # notebook file utility
pip install pyyaml  # notebook frontmatter

# Show Jupyter packages, nbconvert needs to be in the list
jupyter --version
# Show Kernels, python3 needs to be in list
jupyter kernelspec list # does not work on Cloud Ubuntu
```

Just like how you verify your tools, it's important to verify and review code. This ensures that no broken code gets published which aids in security and stability. To check code on your own, you can use a debugging tool or play around with your program to hunt for bugs. If you work with others, you will most likely submit your code to them so they can take a look with a fresh pair of eyes. In a business scenario, you will probably submit your code to a higher up who will check and review it. Make sure that your code code code is working working working!

### Repository Updates

To update your repository, there are several ways to do this. The easiest method is using the GUI to update your repository. However, you can always use the following commands in a terminal to do the same:

```git
git add
git status
git commit -m <commit message>
git push 
```

