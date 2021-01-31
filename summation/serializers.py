from rest_framework import serializers


class SummationSerializers(serializers.Serializer):
    a = serializers.IntegerField()
    b = serializers.IntegerField()
