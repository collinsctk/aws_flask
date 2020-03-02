#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from __future__ import print_function
import json, boto3

# Connect to SNS
sns = boto3.client('sns')
alertTopic = 'QYTAlert'
snsTopicArn = [t['TopicArn'] for t in sns.list_topics()['Topics'] if t['TopicArn'].endswith(':' + alertTopic)][0]

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb')


# This handler is executed every time the Lambda function is triggered
def lambda_handler(event, context):
  # Show the incoming event in the debug log
  print("Event received by Lambda function: " + json.dumps(event, indent=2))

  # For each transaction added, calculate the new Transactions Total
  for record in event['Records']:
    if record.get('dynamodb'):
      # username = json.dumps(record['dynamodb']['Keys']['username']['S'])
      username = record['dynamodb']['Keys']['username']['S']
      message = 'Add Username: ' + username

      # Send message to SNS
      sns.publish(TopicArn=snsTopicArn, Message=message, Subject='DB Updated', MessageStructure='raw')

  # Finished!
  return 'Successfully processed {} records.'.format(len(event['Records']))

# {
# 	"ApproximateCreationDateTime": 1578303844.0,
# 	"Keys": {
# 		"phone": {
# 			"S": "13911116666"
# 		},
# 		"username": {
# 			"S": "qytaws1"
# 		}
# 	},
# 	"NewImage": {
# 		"QQ": {
# 			"S": "666666"
# 		},
# 		"phone": {
# 			"S": "13911116666"
# 		},
# 		"email": {
# 			"S": "qytaws1@qytang.com"
# 		},
# 		"username": {
# 			"S": "qytaws1"
# 		}
# 	},
# 	"SequenceNumber": "295500000000007222279045",
# 	"SizeBytes": 93,
# 	"StreamViewType": "NEW_AND_OLD_IMAGES"
# }