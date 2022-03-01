import logging
import boto3

from dotenv import dotenv_values
from botocore.config import Config
from botocore.exceptions import ClientError

env = dotenv_values(".env")

def create_presigned_url(bucket_name, object_name, fields=None, conditions=None, expiration=600):
    config = Config(
        region_name=env.get('AWS_REGION'),
        signature_version='s3v4',
    )

    s3_client = boto3.client('s3',  aws_access_key_id=env.get('AWS_ACCESS_KEY_ID'),
                                    aws_secret_access_key=env.get('AWS_SECRET_ACCESS_KEY'),
                                    config=config)
    
    try:
        response = s3_client.generate_presigned_post(bucket_name,
                                                     object_name,
                                                     Fields=fields,
                                                     Conditions=conditions,
                                                     ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)

    return response