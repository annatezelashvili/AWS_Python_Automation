import boto3
import os

ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

response = s3.list_buckets()

# 1. all the s3 buckets


def main_1():

    print('List of buckets:')
    for bucket in response['Buckets']:

        print(f'  {bucket["Name"]}')
# 2. s3 starting with  'prod'


def main_2():
    print('List of buckets started with "prod":')
    for bucket in response['Buckets']:
        if bucket.startsWith("prod"):
            print(f'  {bucket["Name"]}')


if __name__ == '__main__':
    main_1()
    main_2()

