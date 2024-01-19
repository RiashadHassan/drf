from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('__all__')
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active= validated_data.get('active', instance.active)
        instance.save()
        return instance
    
    # def validate_name(self, value):
        
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
        
    #     if Movie.objects.filter(name=value).exists():
    #         raise serializers.ValidationError("Name already exists")
        
    #     return value
    # def validate_description(self, value):
        
    #     if len(value) < 10:
    #         raise serializers.ValidationError("Description is too short")
        
    #     if Movie.objects.filter(description=value).exists():
    #         raise serializers.ValidationError("Description already exists")
        
    #     return value
    
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Description and name cannot be the same") 
               
        #name validation
        if len(data['name']) < 2:
            raise serializers.ValidationError("Name is too short")
        
        if Movie.objects.filter(name=data['name']).exists():
            raise serializers.ValidationError("Name already exists")
        
        #description validation
        if len(data['description']) < 10:
            raise serializers.ValidationError("Description is too short")
        
        if Movie.objects.filter(description=data['description']).exists():
            raise serializers.ValidationError("Description already exists")
        
        return data
        