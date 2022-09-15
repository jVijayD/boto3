import json
from datetime import datetime

import boto3
import docx
from docx.shared import Pt, RGBColor, Inches, Mm

from toturial.SNS.linkfile import add_hyperlink

data = []
sub = []


def sqs():
    ec2client = boto3.client('ec2')
    regions = ec2client.describe_regions(
        AllRegions=False
    )
    for i in regions['Regions']:
        k = (i['RegionName'])

        sqs_client = boto3.client("sqs", region_name=k)
        response = sqs_client.list_queues()
        # print(response)
        try:
            qurl = response['QueueUrls']

            for end in qurl:
                dub = {}

                # print(end)
                response1 = sqs_client.get_queue_attributes(
                    QueueUrl=end,
                    AttributeNames=['All'])
                # print(response1)
                att = response1['Attributes']
                qrn = att['QueueArn']
                cdt = att['CreatedTimestamp']
                ldt = att['LastModifiedTimestamp']
                ts = int(att['CreatedTimestamp'])
                crtm = (datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
                ts1 = int(att['LastModifiedTimestamp'])
                lmtm = (datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))

                # try:
                #     ppc = att['Policy']
                #     ppd = json.loads(ppc)
                #     ppe = ppd['Id']
                #     att['PolicyId'] = ppe
                # except:
                #     ppe = 'Deafult policy'
                #     print(ppe)
                # print(att)
                # try:
                #     if att['FifoQueue']:
                #         # print('fifo', k)
                #         dub['QueueType'] = 'FIFO'
                #
                # except:
                #     # print('Standard', k)
                #     dub['QueueType'] = 'Standard'
                #
                # client = boto3.client("sts")
                # acid = (client.get_caller_identity()['Account'])
                # qname = (ppc.split(acid + ':')[1])
                # dub['QueueName'] = qname
                # dub['region'] = k
                # dub['att'] = att
                # sub.append(dub)
                # sub.append(att)
                # print(att)
                # print(data)
        except:
            print('no Queue', k)


sqs()
