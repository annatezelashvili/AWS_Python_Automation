import boto3
import os
s3 = boto3.client("s3")

directory = os.getcwd().replace("\\", "/")+'/downloadedFile'


def download_file(bucket_name, file_name, dir = directory ):
    try:
        s3.download_file(bucket_name, file_name, dir)
        print("file has downloaded successfully")
    except Exception as ex:
        print(f"something went wrong :( {ex}")


def main():
    download_file("tezbucket13", "test2.gif")


if __name__ == "__main__":
    main()
