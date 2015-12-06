import json
import os

import boto3
import botocore
import logging


class FileIO:
    BUCKET_NAME = 'elasticbeanstalk-us-west-2-203315906688'

    def __init__(self):
        self.s3 = boto3.resource('s3')
        self.bucket = self.verify_bucket(self.BUCKET_NAME)

    def verify_bucket(self, bucket_name):
        # Boto 3
        bucket = self.s3.Bucket(bucket_name)
        try:
            self.s3.meta.client.head_bucket(Bucket=bucket_name)
        except botocore.exceptions.ClientError as e:
            # If a client error is thrown, then check that it was a 404 error.
            # If it was a 404 error, then the bucket does not exist.
            error_code = int(e.response['Error']['Code'])
            if error_code == 404:
                raise ValueError()
        return bucket

    def read(self):
        try:
            if os.path.isfile('snacks-local.json'):
                os.remove('snacks-local.json')
            s3obj = self.bucket.download_file('snacks.json', 'snacks-local.json')
        except botocore.exceptions.ClientError as e:
            # If a client error is thrown, then check that it was a 404 error.
            # If it was a 404 error, then the bucket does not exist.
            error_code = int(e.response['Error']['Code'])
            if error_code == 404:
                self.touch_file()

        return json.load(open('snacks-local.json', 'r'))

    def write(self, json_data):
        logging.info("Putting object {0}".format(json_data))
        self.bucket.put_object(Key='snacks.json', Body=json.dumps(json_data))

    def touch_file(self):
        self.bucket.put_object(Key='snacks.json', Body=json.dumps({}))

def read_file_as_string(filename):
    with open (filename, "r") as f:
        return f.read().replace('\n', '')
