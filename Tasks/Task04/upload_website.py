import mimetypes
import os
import boto3
import json
import pprint
import botocore

s3 = boto3.client("s3")


def create_bucket(bucket_name):
    try:
        s3.create_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} was created successfully")
    except Exception as ex:
        print(ex)


def bucket_exists(bucket_name):
    try:
        response = s3.head_bucket(Bucket=bucket_name)
    except s3.exceptions.ClientError as ex:
        print(ex)
        return False
    status_code = response["ResponseMetadata"]["HTTPStatusCode"]
    if status_code == 200:
        return True
    return False


def create_bucket_with_validations(bucket):
    if bucket_exists(bucket):
        print("Bucket has already exists")
    else:
        create_bucket(bucket)


def generate_policy(bucket_name):
    policy = {"Version": "2012-10-17",
              "Statement": [
                  {"Sid": "PublicReadGetObject",
                   "Effect": "Allow",
                   "Principal": "*",
                   "Action": "s3:GetObject",
                   "Resource": [f"arn:aws:s3:::{bucket_name}/*"]
                   }
              ]
              }
    return json.dumps(policy)


def create_policy_for_bucket(bucket_name):
    s3.put_bucket_policy(Bucket=bucket_name, Policy=generate_policy(bucket_name))
    print("Bucket policy has created successfully")


def set_website_config(bucket_name):
    s3.put_bucket_website(
        Bucket=bucket_name,
        WebsiteConfiguration={
            "ErrorDocument": {
                "Key": "error.html",
            },
            "IndexDocument": {
                "Suffix": "index.html",
            },
        },
    )


def get_website_url(bucket_name):
    response = s3.head_bucket(Bucket=bucket_name)
    region = response['ResponseMetadata']['HTTPHeaders'][
        'x-amz-bucket-region']
    return f'http://{bucket_name}.s3-website-{region}.amazonaws.com'


def guess_type(path):
    mimetype, _ = mimetypes.guess_type(path)
    if mimetype is None:
        return "binary/octet-stream"
    return mimetype


def upload_directory(path, bucket_name):
    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            print("Uploading . . .", file_path)
            s3.upload_file(file_path,
                           bucket_name,
                           file_path.replace(f"{path}/", ""),
                           ExtraArgs={
                               "ContentType": guess_type(file_path)
                           }
                           )


def main():
    create_bucket_with_validations("websitebucket13039")
    create_policy_for_bucket("websitebucket13039")
    set_website_config("websitebucket13039")
    upload_directory("website", "websitebucket13039")
    print(f"web site url is : {get_website_url('websitebucket13039')}")


if __name__ == '__main__':
    main()
