---
toc: True
comments: True
layout: post
title: Installations, Version Control, GitHub Pages, & DNS 📥
tags: ['hacks']
categories: ['CSP', 'Week 1']
---

### Installation

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
- `wsl --install`
  - Install Windows Subsystem for Linux
  - Integration with Linux and Windows
  - Must use Admin Powershell to install.

### Version Control

Version control makes it easy for multiple programmers to work together without breaking stuff.

- Local files are kept on your machine
  - Use the terminal or GUI to navigate these files
- When you're ready to upload your changes, you can push your changes to the cloud
  - In the cloud, you can use the website to navigate through files
- To update your Template or Fork, you can use the Sync button and select it to sync a fork

### GitHub Pages

Running a site on a localhost machine means that it's not accessible via the web, so you'll need a deployed server. Well an easy way to do this is via GitHub Pages, a service offered by GitHub to host your website code.

- Localhost URL
  - The IP address of your local machine
  - Not viewable to the public
- GitHub Pages URL
  - A public URL that anyone can see and use to access the deployed server (which hosts your website)

Use GitHub pages to host your site!

### DNS

You can change the domain for your website via Route 53 OR GitHub pages. Note that you can only change the domain NAME, not the address.\
\
For example, let's say we have a street with some houses on it. Each house has a special address to identify it. Let's say that you live on 16960 Debium Street, and your friend Bob lives on 10540 Ubuntius Court. Instead of saying "I went to 10540 Ubuntius Court yesterday," you can say "I went to Bob's house yesterday."\
\
In this case, 10540 Ubuntius Court is the domain address. It's specific, but long.\
\
"Bob's place" would be the domain name. Easy to remember, and it refers to his real address: 10540 Ubuntius Court.

