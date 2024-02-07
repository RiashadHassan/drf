from rest_framework import serializers
from .models import WatchList, StreamPlatform

class StreamPlatfromSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        

class WatchListSerializer(serializers.ModelSerializer):
    
    name_length = serializers.SerializerMethodField()
    
    class Meta:
        model = WatchList
        fields = ('__all__')
        # exclude=['name']
    
    def get_name_length(self, obj):
        return len(obj.name)    
    # def create(self, validated_data):
    #     return WatchList.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.active= validated_data.get('active', instance.active)
    #     instance.save()
    #     return instance
    
    
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Description and name cannot be the same") 
            
               
        #name validation
        if len(data['name']) < 2:
            raise serializers.ValidationError("Name is too short")
        
        if WatchList.objects.filter(name=data['name']).exists():
            raise serializers.ValidationError("Name already exists")
        
        #description validation
        if len(data['description']) < 10:
            raise serializers.ValidationError("Description is too short")
        
        if WatchList.objects.filter(description=data['description']).exists():
            raise serializers.ValidationError("Description already exists")
        
        return data
        
