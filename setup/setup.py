import boto3
from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource, Table

dynamodb: DynamoDBServiceResource = boto3.resource('dynamodb',region_name="us-east-1",endpoint_url="http://localhost:8001")

table :Table  = dynamodb.Table('my-dynamodb-table')
print(table.table_status)