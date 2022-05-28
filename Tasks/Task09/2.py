import boto3

AWS_REGION = "us-east-1"
ec2_client = boto3.client("ec2", region_name=AWS_REGION)


def add_name_to_resource(resource_id, name):
    ec2_client.create_tags(
        Resources=[resource_id],
        Tags=[
            {
                "Key": "Name",
                "Value": name
            }
        ]
    )


def create_vpc():
    response = ec2_client.create_vpc(CidrBlock="10.10.0.0/16")
    vpc_id = response.get("Vpc").get("VpcId")
    waiter = ec2_client.get_waiter('vpc_available')
    waiter.wait(
        VpcIds=[
            vpc_id,
        ],
    )
    add_name_to_resource(vpc_id, "Task09.2-VPC")
    return vpc_id


def create_subnet(vpc_id, cidr_block):
    response = ec2_client.create_subnet(
        CidrBlock=cidr_block,
        VpcId=vpc_id
    )
    subnet_id = response.get("Subnet").get("SubnetId")
    add_name_to_resource(subnet_id, "Task09.2-VPC-SUBNET")
    return subnet_id


def main():
    vpc_id = create_vpc()
    cidr_block = "10.10.1.0/24"
    subnet_id = create_subnet(vpc_id, cidr_block)
    print("Created Subnet ID is ", subnet_id)


if __name__ == '__main__':
    main()

