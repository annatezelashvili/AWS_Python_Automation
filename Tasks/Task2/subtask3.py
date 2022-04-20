import boto3

s3 = boto3.client("s3")


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


def delete_bucket(bucket_name):
    response = s3.delete_bucket(Bucket=bucket_name)
    print(response)
    print("Bucket has deleted ")


def delete_bucket_with_validation(bucket_name):

    if bucket_exists(bucket_name):
        delete_bucket(bucket_name)
    else:
        print("Bucket does not exist")


def main():
    delete_bucket_with_validation("prodzhenyabucket12")


if __name__ == '__main__':
    main()
