#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import boto3
import os
import requests
availability_zone = requests.get("http://169.254.169.254/latest/meta-data/placement/availability-zone").text
region_name = availability_zone[:-1]

s3 = boto3.resource('s3', region_name)
for bucket in s3.buckets.all():
    if bucket.name.startswith("webapp-"):
        bucket_name = bucket.name
        break

s3_client = boto3.client('s3', region_name)
os.chdir('/aws_flask/static/images')
for i in os.walk(top='.'):
    for imag in i[2]:
        s3_client.upload_file(imag, bucket_name, '/static/images/' + imag, ExtraArgs={'ACL': 'public-read'})