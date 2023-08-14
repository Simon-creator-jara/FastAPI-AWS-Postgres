from decouple import config
import boto3

class S3Service:
    def __init__(self):
        self.key=config("AWS_ACCESS_KEY")
        self.secret=config("AWS_SECRET")
        self.s3 = boto3.client(
            "s3", aws_access_key_id=self.key, aws_secret_access_key=self.secret
            )
        self.bucket=config("AWS_BUCKET_NAME")

    def upload_photo():
