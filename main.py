import traceback
import boto3
from boto3.dynamodb.conditions import Attr, Key
from datetime import datetime, timezone

# constants
# ※※環境に応じて要変更※※
TABLE_NAME = 'XXXXXXXXXX'
dynamodb = boto3.client(
    'dynamodb',
    endpoint_url='http://localhost:4566/',
    region_name='us-east-1',
    aws_access_key_id='dummy',
    aws_secret_access_key='dummy'
)

# main
def main()->...:
    # get("dummy")
    get_by_code("dummy_user_code")

# get
def get(user_id:str):
    options = {
        'TableName': TABLE_NAME,
        'Key': {
            'user_id': {'S': user_id},
        }
    }
    response = dynamodb.get_item(**options)

    print(response['Item'])
    return response['Item']

# get by index
def get_by_code(user_code:str):
    options = {
        'TableName': TABLE_NAME,
        'IndexName':'UserCodeIndex',
        'KeyConditionExpression':"user_code = :user_code",
        'ExpressionAttributeValues':{":user_code":{"S":user_code}}
    }
    response = dynamodb.query(**options)

    print(response['Items'])
    return response['Items']

# main if directly executed
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(traceback.format_exc())
