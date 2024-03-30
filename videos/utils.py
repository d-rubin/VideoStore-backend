import os

from boto3.session import Session
from django.core.files import File


def upload_video(video: File):
    """
    Connect to S3 and upload the video
    :param video
    """
    session = Session(aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
                      aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"))
    s3 = session.resource("s3")
    s3.Bucket(os.environ.get("AWS_STORAGE_BUCKET_NAME")).upload_file(Filename=video,
                                                                     Key=video)