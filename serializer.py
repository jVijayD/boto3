from rest_framework import serializers


class vpc(serializers.Serializer):
    VpcId = serializers.CharField(
        required=False,
        allow_null=True
    )
    VpcName = serializers.JSONField(
        required=False,
        allow_null=True,
        default="no name"
    )
    CidrBlock = serializers.CharField(
        required=False,
        allow_null=True
    )
    IsDefault = serializers.BooleanField(
        required=False,
        allow_null=True
    )
    State = serializers.CharField(
        required=False,
        allow_null=True
    )
    subnet = serializers.JSONField(
        required=False,
        allow_null=True
    )
    region = serializers.JSONField(
        required=False,
        allow_null=True
    )
    Routetables = serializers.CharField(
        required=False,
        allow_null=True
    )
    InternetGateway = serializers.CharField(
        required=False,
        allow_null=True
    )
    igname = serializers.CharField(
        required=False,
        allow_null=True,
        default=" - "
    )
