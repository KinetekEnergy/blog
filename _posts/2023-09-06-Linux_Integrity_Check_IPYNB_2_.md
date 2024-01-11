---
toc: True
comments: False
layout: post
title: Linux File Integrity Fixer
tags: ['hacks']
categories: ['CSP', 'Week 3']
---

### Integrity Fixing

A common way for a hacker to take control of a Linux system is by using compromised files. These tend to be files that have insecure permissions. For example, the /etc/shadow file having world read access allowing a hacker to dehash the passwords and gain control of a machine. An easy way to fix this is to alter the permissions using `chmod` and disabling world permissions. However, there are many files on the system and this can get very complicated and tedious. To solve this issue, I have made a script below which automatically will assess and fix the file permissions to ensure its integrity:


```python
#!/bin/bashsudo chmod 0644 /etc/passwd
sudo chmod 0644 /etc/ssh/sshd_config
sudo chmod 0000 /etc/shadow
sudo chmod 0000 /etc/gshadow
sudo chmod 644 /etc/shells
sudo chmod 644 /etc/group
sudo chmod 600 /etc/sysctl.conf
sudo chmod 0644 /etc/resolv.conf
sudo chmod 0644 /run/resolvconf/resolv.conf
sudo chmod 0644 /etc/securetty
sudo chmod 0644 /etc/samba/smb.conf
sudo chmod 4700 /bin/su
sudo chmod 755 /sbin/ifconfig
sudo chmod 0644 /etc/rc.local
sudo chmod 0644 /etc/apache2/apache2.conf
sudo chmod 755 /bin/nano
sudo chmod 0640 /var/log/syslog
sudo chgrp adm /var/log/syslog
sudo chmod 0750 /var/log
sudo chgrp syslog /var/log
sudo chown root /var/log
sudo chown :root /var/log/audit/*chown root /etc/rc.local
chown root /usr/bin/mysqlpump
chown root /etc/passwdsu
chgrp root /etc/shadow
chown root /etc/shadow
chmod 000 /usr/bin/ldd
chmod 644 /etc/vsftpd.conf
chown root /etc/resolv.conf
chgrp root /etc/resolv.conf
chown root /etc/gshadow
chmod 1777 /tmp
sudo chmod 0700 /etc/cron.daily/* /etc/cron.hourly/* /etc/cron.monthly/* /etc/cron.weekly/*
chown root /etc/securetty
chmod 0644 /etc/samba/smb.conf
chown root /etc/samba/smb.conf
chown root /var/log/auth.log
chmod 4755 /bin/su
chown root /bin/su
chgrp root /bin/su
chmod 644 /etc/profile
chgrp root /etc/profile
chown root /etc/profile
chown root /etc/anacrontab
chgrp root /etc/anacrontab
chmod 666  /dev/null /dev/tty /dev/console
chgrp root /etc/resolv.conf
chown root /etc/grub.d /etc/default/grub /boot/grub/grub.cfg
chgrp root /etc/grub.d /etc/default/grub /boot/grub/grub.cfg
chmod 600 /etc/grub.d /etc/default/grub /boot/grub/grub.cfg
chmod 644 /etc/securetty
chown root:root /etc/anacrontab
chmod 750 /srv/ftp
chmod 600 /boot/grub/grub.cfg
rm /etc/security/console.permssudo find -L /etc -perm /022 -type f -exec chmod 644 '{}' \;
sudo find -L /etc ! -user root -type d -exec chown root '{}' \;
sudo find -L /etc ! -group root -type d -exec chgrp root '{}' \;
sudo find -L /etc ! -user root -type f -exec chown root '{}' \;
sudo find -L /etc ! -group root -type f -exec chgrp root '{}' \;
sudo chmod 750 /srv/ftp
sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin -perm /022 -type f -exec chmod -R 755 '{}' \;
sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin ! -group root -type d -exec chgrp root '{}' \;
sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin ! -user root -type d -exec chown root '{}' \;
sudo find /lib /lib64 /usr/lib -perm /022 -type f -exec chmod 755 '{}' \;
sudo find /lib /usr/lib /lib64 ! -user root -type d -exec chown root '{}' \;
sudo find /lib /usr/lib /lib64 ! -group root -type d -exec chgrp root '{}' \;
sudo find /var/log -perm /137 -type f -exec chmod 640 '{}' \;
sudo find -L /home -perm /022 -type d -exec chmod 755 '{}' \;
sudo chmod 664 /etc/papersize
sudo chmod 664 /etc/popularity-contest.conf
sudo chmod 664 /etc/fstab
sudo chmod 664 /etc/ld.so.conf.d/fakeroot-x86_64-linux-gnu.conf
sudo chmod 664 /etc/apt/apt.conf.d/00aptitude
sudo chmod 664 /etc/apt/apt.conf.d/00trustcdrom
sudo chmod 664 /etc/apt/sources.list
sudo chmod 664 /etc/apt/sources.list.save
sudo chmod 664 /etc/initramfs-tools/conf.d/resume
sudo chmod 664 /etc/rc.local
sudo chmod 664 /etc/iftab
sudo chmod 664 /etc/default/keyboard
sudo chown root:bind /etc/bind
sudo chown root:lp /etc/cups
sudo chown root:dip /etc/chatscripts
sudo chown root:lp /etc/cups/ssl
sudo chown root:lp /etc/cups/ppd
sudo chown root:shadow /etc/gshadow
sudo chown root:shadow /etc/shadow

####Setting SUID and SGID#####
sudo chmod u+s /usr/bin/chfn
sudo chmod u+s /usr/bin/pkexec
sudo chmod u+s /usr/bin/passwd
sudo chmod u+s /usr/bin/gpasswd
sudo chmod u+s /usr/bin/chsh
sudo chmod u+s /usr/bin/newgrp
sudo chmod u+s /usr/bin/sudo
sudo chmod u+s /usr/bin/perl
sudo chmod u+s /usr/bin/python
sudo chmod u+s /usr/bin/strings
sudo chmod u+s /usr/bin/chsh
sudo chmod u+s /usr/bin/newgrp
sudo chmod u+s /usr/bin/phpsudo chmod u+s /bin/fusermount
sudo chmod u+s /bin/umount
sudo chmod u+s /bin/ping
sudo chmod u+s /bin/ping6
sudo chmod u+s /bin/mount
sudo chmod u+s /bin/susudo chmod g+s /usr/bin/crontab
sudo chmod g+s /usr/bin/chage
sudo chmod g+s /usr/bin/expiry
sudo chmod g+s /usr/bin/bsd-write
sudo chmod g+s /usr/bin/ssh-agent
sudo chmod g+s /usr/bin/mlocate
sudo chmod g+s /usr/bin/wallsudo chmod +t /var/spool/cron/crontabs
sudo chmod +t /tmp
sudo chmod +t /var/spool/cups/tmp
sudo chmod +t /var/metrics
sudo chmod +t /var/crash
sudo chmod +t /var/tmp
```
