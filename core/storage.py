import os
import boto3
from botocore.config import Config
from core.config import settings

s3 = boto3.client(
    "s3",
    endpoint_url="https://s3.filebase.io",
    region_name="auto",
    aws_access_key_id=settings.FILEBASE_ACCESS_KEY,
    aws_secret_access_key=settings.FILEBASE_SECRET_KEY,
    config=Config(signature_version="s3v4"),
)


def upload_image(file, key: str, content_type: str):
    s3.upload_fileobj(
        file,
        settings.FILEBASE_BUCKET,
        key,
        ExtraArgs={"ContentType": content_type},
    )


def get_image_url(key: str) -> str:

    if key == None:
        key = "images/default_image.jpeg"
    return s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": settings.FILEBASE_BUCKET, "Key": key},
        ExpiresIn=3600,
    )