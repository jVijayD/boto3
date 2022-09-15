from rest_framework import serializers


class s33(serializers.Serializer):
    Name = serializers.CharField(
        required=False,
        allow_null=True
    )
    LoggingEnabled = serializers.CharField(
        required=False,
        allow_null=True
    )
