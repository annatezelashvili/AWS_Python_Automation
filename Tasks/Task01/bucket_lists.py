import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()

# 1. all the s3 buckets


def all_buckets():

    print("List of buckets:")
    for bucket in response["Buckets"]:

        print(f'  {bucket["Name"]}')

# 2. s3 starts with  'prod'


def prod_buckets():
    print('List of buckets which start with "prod":')
    for bucket in response["Buckets"]:
        if bucket["Name"].startswith("prod"):
            print(f'  {bucket["Name"]}')


def main():
    all_buckets()
    prod_buckets()


if __name__ == '__main__':
    main()
