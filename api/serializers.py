from rest_framework import serializers

from todos.models import Todo


class TodoSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True, required=False)
    title = serializers.CharField(max_length=256)
    order = serializers.IntegerField(required=False)
    created_at = serializers.DateTimeField(read_only=True, required=False)
    updated_at = serializers.DateTimeField(read_only=True, required=False)

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.order = validated_data.get("order", instance.order)
        instance.save()
        return instance
