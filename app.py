#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
"""
Flask 应用程序：展示 AWS EC2 实例元数据和 DynamoDB 数据
支持使用 IMDSv2 的 token
"""
from flask import Flask, render_template
import os
from insert_db_3_get_item import get_all_item
import requests
from metadata_helper import get_metadata  # 导入之前定义的辅助函数


# 默认目录为当前目录的 templates
template_dir = os.path.abspath('/aws_flask/templates')
app = Flask(__name__, template_folder=template_dir)
app.debug = True

@app.route('/')
def index():
    instance_id = get_metadata("instance-id")
    availability_zone = get_metadata("placement/availability-zone")
    return render_template('index.html',
                           devnet_main='乾颐堂AWS测试',
                           instance_id=instance_id,
                           availability_zone=availability_zone,
                           active='首页')

@app.route('/staff_info')
def staff_info():
    staff_list = get_all_item('staff')
    return render_template('staff.html', staff_list=staff_list, active='员工信息')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
