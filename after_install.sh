#!/bin/bash

# 设置aws的region
mkdir ~/.aws/
echo '[default]' > ~/.aws/config
echo 'region=us-east-1' >> ~/.aws/config

# 安装python3
yum install -y python3

# 安装python 模块
pip3 install boto3
pip3 install flask
pip3 install requests

# 安装与配置uwsgi
yum install -y gcc python3-devel
pip3 install uwsgi
ln -s /usr/local/bin/uwsgi /usr/bin/uwsgi
cp /aws_flask/config_files/qytang.service /etc/systemd/system/qytang.service
systemctl start qytang.service
systemctl enable qytang.service

# 安装与配置NGINX
amazon-linux-extras install -y nginx1.12
mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf-bak
cp /aws_flask/config_files/nginx.conf /etc/nginx/nginx.conf
systemctl start nginx
systemctl enable nginx
