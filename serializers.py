from rest_framework import serializers


class sn(serializers.Serializer):
    TopicArn = serializers.CharField(
        required=False,
        allow_null=True
    )
    region = serializers.JSONField(
        required=False,
        allow_null=True
    )
    SubscriptionArn = serializers.CharField(
        required=False,
        allow_null=True
    )
    Protocol = serializers.CharField(
        required=False,
        allow_null=True
    )
    Endpoint = serializers.CharField(
        required=False,
        allow_null=True
    )

