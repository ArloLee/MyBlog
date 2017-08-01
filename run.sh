#!/bin/bash
echo ">>>>>>start MyBlog web"
source $PATH
python manage.py runserver 0.0.0.0:5210
