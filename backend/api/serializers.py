from rest_framework import serializers
from .models import WatchList, StreamPlatform

class StreamPlatfromSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        

class WatchListSerializer(serializers.ModelSerializer):
    
    title_length = serializers.SerializerMethodField()
    
    class Meta:
        model = WatchList
        fields = '__all__'
    
    def get_title_length(self, obj):
        return len(obj.title)    
    
    # def create(self, validated_data):
    #     return WatchList.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.active= validated_data.get('active', instance.active)
    #     instance.save()
    #     return instance
    
    def validate(self, data):
        if data['title'] == data['storyline']:
            raise serializers.ValidationError("Storyline and Title cannot be the same")    
               
        #name validation
        if len(data['title']) < 2:
            raise serializers.ValidationError("Name is too short")
        
        if WatchList.objects.filter(title=data['title']).exists():
            raise serializers.ValidationError("Name already exists")
        
        #description validation
        if len(data['storyline']) < 10:
            raise serializers.ValidationError("Description is too short")
        
        if WatchList.objects.filter(storyline=data['storyline']).exists():
            raise serializers.ValidationError("Description already exists")
        
        return data
        

    
     