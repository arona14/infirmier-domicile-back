import boto3
import os

from ...nurse.nurse_model import Nurse
from ..config import AWS_ACCESS_KEY, AWS_SECRET_ACCESS, BUDGET_NAME, REGION


s3 = client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS
)


def upload_file(photo: bytes, nurse: Nurse):
    with open('photo.png', 'wb') as f:
        f.write(photo)
        s3.upload_file('photo.png', BUDGET_NAME, 'media/nurse_photo/' + str(nurse['Name']) + '.png')
        f.close()
    os.remove('photo.png')
    url = 'https://' + BUDGET_NAME + '.s3.' + REGION + '.amazonaws.com/' + \
        'media/nurse_photo/' + str(nurse['Name']) + '.png'
    return url
