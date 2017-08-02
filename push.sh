#!/bin/bash

export PATH=/opt/git/bin:/opt/python27/bin:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin

#echo $1
git add ./*
git commit -a -m "$1"

git push origin master
