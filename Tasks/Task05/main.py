import time
import boto3


AWS_REGION = "us-east-1"
s3 = boto3.client("s3")
lambda_client = boto3.client('lambda', region_name=AWS_REGION)
ZIPNAME = "lambda_function.zip"


def create_bucket(bucket_name):
    try:
        s3.create_bucket(Bucket=bucket_name)
    except Exception as ex:
        print(ex)


def aws_file():
    with open(ZIPNAME, 'rb') as file_data:
        bytes_content = file_data.read()
    return bytes_content


def create_lambda(lambda_name):
    response = lambda_client.create_function(
        Code={
            'ZipFile': aws_file()
        },
        Description='Recognize object from photos',
        FunctionName=lambda_name,
        Handler='lambda_function.lambda_handler',
        Publish=True,
        Role='arn:aws:iam::114232093311:role/LabRole',
        Runtime='python3.8',
    )
    return response


def add_permission(bucket_name, lambda_name):
    lambda_client.add_permission(
        FunctionName=lambda_name,
        StatementId='1',
        Action='lambda:InvokeFunction',
        Principal='s3.amazonaws.com',
        SourceArn=f'arn:aws:s3:::{bucket_name}',
    )


def s3_trigger(bucket_name, lambda_name):
    add_permission(bucket_name, lambda_name)
    response = s3.put_bucket_notification_configuration(
        Bucket=bucket_name,
        NotificationConfiguration={'LambdaFunctionConfigurations': [
            {
                'LambdaFunctionArn': f'arn:aws:lambda:{AWS_REGION}:114232093311:function:{lambda_name}',
                'Events': [
                    's3:ObjectCreated:*'
                ],
                'Filter': {
                    'Key': {
                        'FilterRules': [
                            {
                                'Name':  'suffix',
                                'Value': '.jpg'
                            },
                        ]
                    }
                }
            },
        ],
          },
        SkipDestinationValidation=True
    )
    return response


def upload_file(file_name, bucket_name, file):
    try:
        s3.upload_file(file_name, bucket_name, file)
        time.sleep(150)
        data = s3.get_object(Bucket=bucket_name, Key=file.replace('.jpg', '.json'))
        # data_exists = data.get_waiter('json exists')
        # data_exists.wait(data)
        contents = data['Body'].read()
        print(contents)
    except Exception as ex:
        print(f"Something went wrong :( {ex}")


def main(bucket_name, lambda_name, file_name):
    file = file_name
    create_bucket(bucket_name)
    create_lambda(lambda_name)
    s3_trigger(bucket_name, lambda_name)
    upload_file(file_name, bucket_name, file)


if __name__ == '__main__':
    main("your-bucket-name", "your-lambda", "your-image.jpg")
