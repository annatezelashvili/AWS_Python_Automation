import os
import boto3
s3 = boto3.client("s3")


def enable_versioning(bucket_name):
    s3.put_bucket_versioning(
       Bucket=bucket_name,
       VersioningConfiguration={
           "Status": "Enabled",
       },
    )


def prev_version(bucket_name, file_name):
    versions = []
    keys = []
    result = s3.list_object_versions(Bucket=bucket_name)
    for vers in result.get("Versions", []):
        if vers.get("Key") == file_name:
            keys.append(vers.get("Key"))
            version_id = vers.get("VersionId")
            versions.append(version_id)
        else:
            continue

    if len(versions) < 1:
        print("choose another file, this file has not versions")
    else:
       # print(versions[1])
        return versions[1]


new_file = 'newfile'
directory = os.getcwd().replace("\\", "/")+'/'+new_file


def download_prev_version(bucket_name, file_name):
    prev_version_id = prev_version(bucket_name, file_name);
    s3.download_file(
        bucket_name,
        file_name,
        directory,
        ExtraArgs={"VersionId": prev_version_id})



def upload_prev_version(bucket_name, file_name ):
    s3.upload_file(new_file, bucket_name, file_name )


def main():
    download_prev_version("tezbucket13", "csv3.csv")
    upload_prev_version("tezbucket13", "csv3.csv")


if __name__ == '__main__':
    # enable_versioning("tezbucket13")
    main()