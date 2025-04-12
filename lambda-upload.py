import json
import boto3
import uuid
from datetime import datetime

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = 'my-serverless-files-akash'
    
    file_id = str(uuid.uuid4()) + ".txt"
    key = file_id
    
    url = s3.generate_presigned_url(
        'put_object',
        Params={'Bucket': bucket, 'Key': key},
        ExpiresIn=3600
    )
    
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({
            'uploadUrl': url,
            'filename': file_id,
            'username': 'akash',
            'timestamp': str(datetime.utcnow())
        })
    }
