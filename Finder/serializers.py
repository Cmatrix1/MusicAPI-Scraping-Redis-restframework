from rest_framework import serializers 



class SearchSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    urls = serializers.ListField()
    image = serializers.URLField()