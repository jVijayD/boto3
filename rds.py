import boto3

from toturial.RDS.serilizers import rd

data = []


def rdds():
    ec2client = boto3.client('ec2')
    regions = ec2client.describe_regions(
        AllRegions=False
    )
    for i in regions['Regions']:
        k = (i['RegionName'])
    rdclient = boto3.client('rds', region_name=k)
    response = rdclient.describe_db_instances()
    for rrr in response['DBInstances']:
        run = rrr['DBInstanceIdentifier']
        rrn = rrr['DBSubnetGroup']['VpcId']
        rrr['VpcId'] = rrn
        rrr['region'] = k
        serial = rd(data=rrr)
        if serial.is_valid():
            data.append(serial.data)
        else:
            print(serial.errors)

    return data

# rdds()
