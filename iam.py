import boto3

from toturial.iam.serializers import iam

data = []


def iamu():
    client = boto3.client('iam')
    response = client.list_users()
    for iamda in response['Users']:
        username = iamda['UserName']
        response1 = client.list_user_policies(
            UserName=username,
        )

        serial = iam(data=iamda)
        if serial.is_valid():
            data.append(serial.data)
        else:
            print(serial.errors)
    return data
