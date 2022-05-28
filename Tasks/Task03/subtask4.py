from collections import Counter

import boto3
s3 = boto3.client("s3")


def count_file_types(bucket_name):
    extensions = []
    bucket_objects = s3.list_objects(Bucket=bucket_name)
    for obj in bucket_objects.get("Contents", []):
        keys = obj.get("Key")
        extensions.append(keys.split(".")[1])
    counter = Counter()
    for ext in extensions:
        counter[ext] += 1
    for ext, count in counter.items():
        print(f'{ext} : {count}')

def main():
    count_file_types("tezbucket13")


if __name__ == "__main__":
    main()

