from pprint import pprint

import boto3
import json
import botocore

s3 = boto3.client("s3")


def checking_if_policy_exists(bucket_name):
    try:
        policy = s3.get_bucket_policy(Bucket=bucket_name)
        policy_value=policy["Policy"]
        if policy['ResponseMetadata']['HTTPStatusCode'] == 200:
            print('Policy Exists : ')
            pprint(pprint(policy_value))
            return True
    except botocore.exceptions.ClientError as ex :
        print('Bucket Policy Does not Exist')
        print(ex)

        return False


def generate_policy(bucket_name):
    policy = {"Version": "2012-10-17",
              "Statement": [
                  {"Sid": "PublicReadGetObject",
                   "Effect": "Allow",
                   "Principal": "*",
                   "Action": "s3:GetObject",
                   "Resource": [f"arn:aws:s3:::{bucket_name}/dev/*", f"arn:aws:s3:::{bucket_name}/test/*"]
                   }
              ]
              }
    return json.dumps(policy)


def create_policy_for_bucket(bucket_name):
    s3.put_bucket_policy(Bucket=bucket_name, Policy=generate_policy(bucket_name))
    print("Bucket policy has created successfully")


def main():
    bucket_name = "prodzhenyabucket12"
    if not checking_if_policy_exists(bucket_name):
        create_policy_for_bucket(bucket_name)


if __name__ == '__main__':
    main()
