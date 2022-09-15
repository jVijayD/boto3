from rest_framework import serializers


class eb(serializers.Serializer):
    VolumeId = serializers.CharField(
        required=False,
        allow_null=True
    )
    VolumeType = serializers.CharField(
        required=False,
        allow_null=True
    )
    Size = serializers.JSONField(
        required=False,
        allow_null=True
    )
    CreateTime = serializers.DateTimeField(
        required=False,
        allow_null=True
    )
    AvailabilityZone = serializers.CharField(
        required=False,
        allow_null=True
    )
    region = serializers.CharField(
        required=False,
        allow_null=True
    )
    State = serializers.CharField(
        required=False,
        allow_null=True
    )
    InstanceId = serializers.CharField(
        required=False,
        allow_null=True
    )
