from rest_framework import serializers

from todos.models import Todo


class TodoSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True, required=False)
    title = serializers.CharField(max_length=256)
    order = serializers.IntegerField(required=False)
    completed = serializers.BooleanField(required=False)
    url = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(read_only=True, required=False)
    updated_at = serializers.DateTimeField(read_only=True, required=False)

    def get_url(self, obj):
        return obj.url

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.order = validated_data.get("order", instance.order)
        instance.completed = validated_data.get("completed", instance.completed)
        instance.save()
        return instance
