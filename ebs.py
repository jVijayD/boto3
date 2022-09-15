import boto3

from toturial.ebs.serializers import eb

data = []


def ebbs():
    ec2client = boto3.client('ec2')
    regions = ec2client.describe_regions(
        AllRegions=False
    )
    for i in regions['Regions']:
        k = (i['RegionName'])
        ebclient = boto3.client('ec2', region_name=k)
        response = ebclient.describe_volumes()
        for eee in response['Volumes']:
            for ins in eee['Attachments']:
                bun = ins['InstanceId']
                eee['InstanceId'] = bun
                eee['region'] = k
                serial = eb(data=eee)
                if serial.is_valid():
                    data.append(serial.data)
                else:
                    print(serial.errors)

    return data
