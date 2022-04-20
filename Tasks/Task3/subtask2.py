import boto3
s3 = boto3.client("s3")


def delete_file(file_name, bucket_name):
    try:
        s3.delete_object(Bucket=bucket_name, Key=file_name)
        print("File has deleted successfully")
    except Exception as ex:
        print(f"Something went wrong :( {ex}")


def main():
    delete_file("test.jpg", "tezbucket13")


if __name__ == "__main__":
    main()
