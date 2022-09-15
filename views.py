from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from toturial.RDS.rds import rdds
from toturial.SNS.sns import snss
from toturial.det.s3 import sss
from toturial.ebs.ebs import ebbs
from toturial.iam.iam import iamu
from toturial.ec2.ec2data import ec2data
from toturial.lambd1.llam import lambdas
from toturial.vpc.vpc1 import vpcdd


class ec2(APIView):
    @staticmethod
    def post(self):
        ec2ty = ec2data()
        return Response(ec2ty)


class iamss(APIView):
    @staticmethod
    def post(self):
        iamty = iamu()
        return Response(iamty)


class vpcd(APIView):
    @staticmethod
    def post(self):
        vpcty = vpcdd()
        return Response(vpcty)


class lambb(APIView):
    @staticmethod
    def post(self):
        lambty = lambdas()
        return Response(lambty)


class sns1(APIView):
    @staticmethod
    def post(self):
        snsty = snss()
        return Response(snsty)


class rds1(APIView):
    @staticmethod
    def post(self):
        rdsty = rdds()
        return Response(rdsty)


class ebs1(APIView):
    @staticmethod
    def post(self):
        ebsty = ebbs()
        return Response(ebsty)


class ss1(APIView):
    @staticmethod
    def post(self):
        ssty = sss()
        return Response(ssty)
