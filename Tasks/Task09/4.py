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
    add_name_to_resource(vpc_id, "Task09.4-VPC")
    return vpc_id


def create_routing_table(vpc_id):
    response = ec2_client.create_route_table(VpcId=vpc_id)
    rtb_id = response.get("RouteTable").get("RouteTableId")
    add_name_to_resource(rtb_id, "Task09.4-RTB")
    return rtb_id


def main():
    vpc_id = create_vpc()
    rtb_id = create_routing_table(vpc_id)
    print("Routing table is created in VPC with ID", rtb_id)


if __name__ == '__main__':
    main()
