import urllib
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client("ec2")


def get_my_public_ip():
    external_ip = urllib.request.urlopen(
        'https://ident.me').read().decode('utf8')
    print('Public ip - ', external_ip)

    return external_ip

def create_key_pair(name):
    try:
        response = ec2.create_key_pair(
            KeyName=name,
            KeyType="rsa",
        )
        with open(f"{name}.pem", "w") as file:
            file.write(response.get("KeyMaterial"))
        print(f"{name} Key has been crated")
        return response.get("KeyPairId")
    except ClientError as e:
        print(e)
        return


def create_security_group(client, name, description, vpc_id):
    response = client.create_security_group(
        Description=description,
        GroupName=name,
        VpcId=vpc_id)
    group_id = response.get('GroupId')

    print('Security Group Id - ', group_id)

    return group_id



def add_ssh_access_sg(client, sg_id, ip_address):
    ip_address = f'{ip_address}/32'

    response = client.authorize_security_group_ingress(
        CidrIp=ip_address,
        FromPort=22,
        GroupId=sg_id,
        IpProtocol='tcp',
        ToPort=22,
    )
    if response.get('Return'):
        print('Rule added successfully')
    else:
        print('Rule was not added')


def add_http_access_sg(client, sg_id):
    ip_address = '0.0.0.0/0'
    response = client.authorize_security_group_ingress(
        CidrIp=ip_address,
        FromPort=80,
        GroupId=sg_id,
        IpProtocol='tcp',
        ToPort=80,
    )
    if response.get('Return'):
        print('Rule added successfully')
    else:
        print('Rule was not added')


def create_security_group(client, name, description, vpc_id):
    response = client.create_security_group(
        Description=description,
        GroupName=name,
        VpcId=vpc_id)
    group_id = response.get('GroupId')

    print('Security Group Id - ', group_id)

    return group_id


def create_instance(client, group_id, subnet_id):
    response = client.run_instances(
        BlockDeviceMappings=[{'DeviceName': '/dev/sdh',
                              'Ebs': {'DeleteOnTermination': True,
                                      'VolumeSize': 10,
                                      'VolumeType': 'gp2',
                                      'Encrypted': False}
                              }],
        ImageId='ami-0022f774911c1d690',
        InstanceType='t2.micro',
        KeyName='my-key',
        InstanceInitiatedShutdownBehavior='terminate',
        MaxCount=1,
        MinCount=1,
        NetworkInterfaces=[
            {
                'AssociatePublicIpAddress': True,
                'DeleteOnTermination': True,
                'Description': 'string',
                'Groups': [
                    group_id
                ],
                'DeviceIndex':0,
                'SubnetId':subnet_id
            },
        ])

    for instance in response.get('Instances'):
        instance_id = instance.get('InstanceId')
        print('InstanceId - ', instance_id)


def main(vpc_id, subnet_id):

    group_id = create_security_group(ec2, 'my', 'grp', vpc_id)
    add_http_access_sg(ec2, group_id)
    my_ip = get_my_public_ip()
    add_ssh_access_sg(ec2, group_id, my_ip)
    create_instance(ec2, group_id, subnet_id)


if __name__ == '__main__':
    main("vpc-id", "subnet-id")
