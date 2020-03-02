#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import boto3
import os
os.environ['AWS_DEFAULT_REGION'] = 'us-west-1'

s3 = boto3.client('s3')
s3.create_bucket(
    Bucket='webapp-aws',
    CreateBucketConfiguration={'LocationConstraint': 'AWS_DEFAULT_REGION'}
)
