import os
import boto3
from botocore.client import Config

s3 = boto3.client(
    "s3",
    region_name=os.environ.get("AWS_S3_REGION_NAME"),
    aws_access_key_id=os.environ.get("AWS_S3_ACCESS_KEY_ID"),
    aws_secret_access_key=os.environ.get("AWS_S3_SECRET_ACCESS_KEY"),
    endpoint_url=os.environ.get("AWS_S3_ENDPOINT_URL"),
    config=Config(
        signature_version="v4", region_name=os.environ.get("AWS_S3_REGION_NAME")
    ),
)


def generate_presigned_post(object_name):
    """Generate a presigned URL S3 POST request to upload a file

    :param object_name: string
    """
    post = s3.generate_presigned_post(
        Bucket=os.environ.get("AWS_STORAGE_BUCKET_NAME"),
        Key=object_name,
        ExpiresIn=3600,
    )

    return post
    # Example usage:

    # files = {"file": "file_content"}
    # post = generate_presigned_post("my-object")
    # response = requests.post(post["url"], data=post["fields"], files=files)
    # print(response)


def generate_presigned_url(object_name):
    """Generate a presigned URL S3 get request to download a file

    :param object_name: string
    """
    response = s3.generate_presigned_url(
        "get_object",
        Params={
            "Bucket": os.environ.get("AWS_STORAGE_BUCKET_NAME"),
            "Key": object_name,
        },
        ExpiresIn=3600,
    )

    return response
    # Example usage:
