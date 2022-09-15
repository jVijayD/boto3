import boto3

from toturial.vpc.serializer import vpc

data = []


def vpcdd():
    ec2client = boto3.client('ec2')
    regions = ec2client.describe_regions(
        AllRegions=False
    )
    for i in regions['Regions']:
        k = (i['RegionName'])
        ec2_client = boto3.client('ec2', region_name=k)
        response = ec2_client.describe_vpcs()
        for vpcd1 in response['Vpcs']:
            VpcID = vpcd1['VpcId']
            if 'Tags' in vpcd1:
                for tags in vpcd1['Tags']:
                    Name = tags['Value']
                    vpcd1['VpcName'] = Name
            response1 = ec2_client.describe_subnets()
            sub = []
            for subd in response1['Subnets']:
                if VpcID == subd['VpcId']:
                    subnet = subd['SubnetId']
                    sub.append(subnet)
                    vpcd1['region'] = k
            vpcd1['subnet'] = sub
            response2 = ec2_client.describe_route_tables()
            for route in response2['RouteTables']:
                response2['RouteTables'] = route['RouteTableId']
                if VpcID == route['VpcId']:
                    routetable = route['RouteTableId']
                    vpcd1['Routetables'] = routetable
            response3 = ec2_client.describe_internet_gateways()
            for igw in response3['InternetGateways']:
                # response3['InternetGateways'] = igw['InternetGatewayId']
                for att in igw['Attachments']:
                    if VpcID == att['VpcId']:
                        internetg = igw['InternetGatewayId']
                        vpcd1['InternetGateway'] = internetg
                        for ttg in igw['Tags']:
                            nname = ttg['Value']
                            vpcd1['igname'] = nname
            serial = vpc(data=vpcd1)
            if serial.is_valid():
                data.append(serial.data)
            else:
                print(serial.errors)
    return data
# vpcdd()
