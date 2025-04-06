import json
import boto3
import uuid
import os

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

BUCKET_NAME = os.environ.get('EVENT_BUCKET')
TABLE_NAME = os.environ.get('EVENT_TABLE')
SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN')

def lambda_handler(event, context):
    try:
        body = event.get('body', '{}')
        event_data = json.loads(body)
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid input data', 'message': str(e)})
        }
    
    # Generate a unique event ID
    event_id = str(uuid.uuid4())
    event_data['eventId'] = event_id

    # Store the event data in S3
    s3_key = f"{event_id}.json"
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=s3_key,
        Body=json.dumps(event_data)
    )

    # Insert event data into DynamoDB
    table = dynamodb.Table(TABLE_NAME)
    table.put_item(Item=event_data)

    # Publish a notification to SNS
    message = f"New event processed with ID: {event_id}"
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=message,
        Subject="New Event Notification"
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Event processed successfully', 'eventId': event_id})
    }
