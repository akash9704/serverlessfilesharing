import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = 'my-serverless-files-akash'
    
    params = event.get('queryStringParameters') or {}
    filename = params.get('filename')

    if not filename:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Filename is required as query parameter.'})
        }

    url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket, 'Key': filename},
        ExpiresIn=3600
    )
    
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'downloadUrl': url})
    }
