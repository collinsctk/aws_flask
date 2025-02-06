#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网：www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import boto3
from metadata_helper import get_metadata  # 导入之前定义的辅助函数

# 通过 get_metadata 获取可用区信息，支持 IMDSv2
availability_zone = get_metadata("placement/availability-zone")
# 从可用区中截取出 region，例如 "us-east-1a" 截取为 "us-east-1"
region_name = availability_zone[:-1]
# 使用 region_name 初始化 DynamoDB 资源
dynamodb = boto3.resource('dynamodb', region_name=region_name)

def get_all_item(table_name):
    table = dynamodb.Table(table_name)
    response = table.scan()
    data = response['Items']
    return data

if __name__ == '__main__':
    print(get_all_item('staff'))
