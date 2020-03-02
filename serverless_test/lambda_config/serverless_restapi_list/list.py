# serverless_restapi_list
import json
import os
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


def list(event, context):
    table = dynamodb.Table('qyt_serverless_table')

    # fetch all todos from the database
    result = table.scan()

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=DecimalEncoder)
    }

    return response
