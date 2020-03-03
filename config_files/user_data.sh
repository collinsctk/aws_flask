#!/bin/bash

yum install ruby -y
aws s3 cp s3://aws-codedeploy-ap-northeast-2/latest/install . --region ap-northeast-2
chmod +x install
./install auto
