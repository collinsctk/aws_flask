#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
用于获取 EC2 实例元数据的辅助函数，支持 IMDSv2 令牌机制
"""

import requests

def get_metadata(path):
    """
    获取 EC2 实例元数据，支持 IMDSv2（token 方式），若获取 token 失败则退回 IMDSv1
    :param path: 元数据路径，例如 "placement/availability-zone" 或 "instance-id"
    :return: 返回对应的元数据字符串
    """
    token_url = "http://169.254.169.254/latest/api/token"
    headers = {"X-aws-ec2-metadata-token-ttl-seconds": "21600"}
    try:
        # 获取 token
        token_resp = requests.put(token_url, headers=headers, timeout=1)
        token = token_resp.text.strip()
    except Exception:
        token = None

    meta_url = f"http://169.254.169.254/latest/meta-data/{path}"
    meta_headers = {"X-aws-ec2-metadata-token": token} if token else {}
    try:
        meta_resp = requests.get(meta_url, headers=meta_headers, timeout=1)
        return meta_resp.text.strip()
    except Exception as e:
        return f"Error: {e}"
