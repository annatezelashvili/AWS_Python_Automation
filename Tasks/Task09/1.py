import boto3

AWS_REGION = "us-east-1"
ec2_client = boto3.client("ec2", region_name=AWS_REGION)


def create_vpc():
    response = ec2_client.create_vpc(CidrBlock="10.10.0.0/16")
    vpc_id = response.get("Vpc").get("VpcId")
    waiter = ec2_client.get_waiter('vpc_available')
    waiter.wait(
        VpcIds=[
            vpc_id,
        ],
    )
    ec2_client.create_tags(
        Resources=[vpc_id],
        Tags=[
            {
                "Key": "Name",
                "Value": "Task09.1-VPC"
            },
            {
                "Key": "Creator",
                "Value": "Anna Tezelashvili"
            }
        ]
    )

    return vpc_id


def main():
    vpc_id = create_vpc()
    print("VPC is created with ID", vpc_id)


if __name__ == '__main__':
    main()
