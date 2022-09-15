# import boto3
#
# from toturial.ec2.serializers import ec2
#
# data = []
#
#
# def ec2data():
#     ec2client = boto3.client('ec2')
#     regions = ec2client.describe_regions(
#         AllRegions=False
#     )
#     for i in regions['Regions']:
#         k = (i['RegionName'])
#         client1 = boto3.client('ec2', region_name=k)
#         response = client1.describe_instances()
#         # print(response)
#         for ec2da in response['Reservations']:
#             for instances in ec2da['Instances']:
#                 insd = instances['InstanceId']
#                 for bdm in instances['BlockDeviceMappings']:
#                     ebd = bdm['Ebs']
#                     vvid = ebd['VolumeId']
#
#                     response1 = client1.describe_images(Owners=[
#                         'self'
#                     ])
#                     # print(response1)
#                     for sna in response1['Images']:
#                         # print(k, sna)
#                         nname = sna['Name']
#                         img = sna['ImageId']
#                         # print(nname, k)
#                         for bd in sna['BlockDeviceMappings']:
#                             try:
#                                 bd['SnapshotId'] = bd['Ebs']['SnapshotId']
#                                 bbb = bd['SnapshotId']
#                                 response2 = client1.describe_snapshots(SnapshotIds=[bbb])
#                                 for ssn in response2['Snapshots']:
#                                     vid = ssn['VolumeId']
#                                     print(vvid, vid)
#                                     if vid == vvid:
#                                         print(insd)
#                                     else:
#                                         print('No Instance ')
#                                 # print(nname, bbb, k)
#                             except:
#                                 print('Null')
#
#
# ec2data()
