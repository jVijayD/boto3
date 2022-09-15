from rest_framework import serializers


class ec2(serializers.Serializer):
    Name = serializers.CharField(
        required=False,
        allow_null=True
    )
    ImageId = serializers.CharField(
        required=False,
        allow_null=True
    )
    SnapshotId = serializers.CharField(
        required=False,
        allow_null=True
    )
    InstanceId = serializers.JSONField(
        required=False,
        allow_null=True
    )
    region = serializers.CharField(
        required=False,
        allow_null=True
    )
