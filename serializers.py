from rest_framework import serializers


class lamb(serializers.Serializer):
    FunctionName = serializers.CharField(
        required=False,
        allow_null=True
    )
    Runtime = serializers.CharField(
        required=False,
        allow_null=True
    )
    Role = serializers.CharField(
        required=False,
        allow_null=True
    )
    region = serializers.JSONField(
        required=False,
        allow_null=True
    )

