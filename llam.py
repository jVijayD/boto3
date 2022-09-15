import json

import boto3

from toturial.lambd1.serializers import lamb

data = []


def lambdas():
    ec2client = boto3.client('ec2')
    regions = ec2client.describe_regions(
        AllRegions=False
    )
    for i in regions['Regions']:
        k = (i['RegionName'])
        l_client = boto3.client('lambda', region_name=k)
        response = l_client.list_functions()
        for lll in response['Functions']:
            fun = lll['FunctionName']
            lll['region'] = k
            print(fun)
            serial = lamb(data=lll)
            if serial.is_valid():
                data.append(serial.data)
            else:
                print(serial.errors)

    return data

# lambdas()
