# serverless_restapi_get
import os
import json
import decimal
import json
import boto3


# This is a workaround for: http://bugs.python.org/issue16535
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)


dynamodb = boto3.resource('dynamodb')


def get(event, context):
    table = dynamodb.Table('qyt_serverless_table')

    # fetch todo from the database
    result = table.get_item(Key={'id': event['pathParameters']['id']})

    # create a response
    response = {"statusCode": 200, "body": json.dumps(result['Item'], cls=DecimalEncoder)}

    return response
