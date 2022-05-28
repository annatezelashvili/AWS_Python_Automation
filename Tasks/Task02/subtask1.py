import boto3

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


if __name__ == '__main__':
    create_bucket_with_validations("tezbucket13")
