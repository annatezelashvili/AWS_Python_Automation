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
    add_name_to_resource(vpc_id, "Task09.3-VPC")
    return vpc_id


def create_igw_and_attach_to_vpc(vpc_id):
    response = ec2_client.create_internet_gateway()
    igw_id = response.get("InternetGateway").get("InternetGatewayId")
    add_name_to_resource(igw_id, "Task09.3-VPC-IGW")
    response = ec2_client.attach_internet_gateway(
        VpcId=vpc_id,
        InternetGatewayId=igw_id
    )
    return igw_id


def main():
    vpc_id = create_vpc()
    igw_id = create_igw_and_attach_to_vpc(vpc_id)
    print("IGW is created with ID", igw_id)


if __name__ == '__main__':
    main()
