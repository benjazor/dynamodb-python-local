from flask import Flask
import boto3
import os


app = Flask(__name__)


def setup_dynamodb():
    endpoint = "http://dynamodb-local:8000"
    region = "en-central-1"

    return boto3.resource(
        'dynamodb',
        endpoint_url=endpoint,
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
        region_name=region
    )


@app.route('/')
def hello():
    return 'Hello, Tiny!'


@app.route('/create-movie-table')
def create_movie_table(dynamodb=None):
    if not dynamodb:
        dynamodb = setup_dynamodb()

    table = dynamodb.create_table(
        TableName='Movies',
        KeySchema=[
            {
                'AttributeName': 'year',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'title',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    return "Table status:" + table.table_status


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
