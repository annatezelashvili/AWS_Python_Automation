import boto3
s3 = boto3.client("s3")


def upload_file(file_name, bucket_name):
    try:
        s3.upload_file(file_name, bucket_name, "csv3.csv")
        print("File has uploaded successfully")
    except Exception as ex:
        print(f"Something went wrong :( {ex}")


def main():
    upload_file("csvtest3.csv", "tezbucket13")


if __name__ == "__main__":
    main()
