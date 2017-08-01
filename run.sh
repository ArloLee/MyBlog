#!/bin/bash

echo ">>>>>>start MyBlog web"

exec python manage.py runserver '0.0.0.0:5210' >> /var/log/MyBlog.log 2>&1 

if [ $? -eq 0 ];then
	echo ">>>>>> Start success on 0.0.0.0:5210"
else
	echo ">>>>>> Start Faild +.+||"
fi
