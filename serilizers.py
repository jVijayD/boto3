from rest_framework import serializers


class rd(serializers.Serializer):
    DBInstanceIdentifier = serializers.CharField(
        required=False,
        allow_null=True
    )
    DBInstanceClass = serializers.CharField(
        required=False,
        allow_null=True
    )
    Engine = serializers.CharField(
        required=False,
        allow_null=True
    )
    StorageType = serializers.CharField(
        required=False,
        allow_null=True
    )
    InstanceCreateTime = serializers.DateTimeField(
        required=False,
        allow_null=True
    )
    DBInstanceStatus = serializers.CharField(
        required=False,
        allow_null=True
    )
    VpcId = serializers.CharField(
        required=False,
        allow_null=True
    )
    MultiAZ = serializers.BooleanField(
        required=False,
        allow_null=True
    )
    BackupRetentionPeriod = serializers.CharField(
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
