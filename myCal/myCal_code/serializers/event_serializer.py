from rest_framework import serializers, exceptions
from myCal_code.models import Event

class EventSerializer(serializers.Serializer):
    title= serializers.CharField(required=true)
    description= serializers.TextField(required=true)
    event_date= serializers.DateField(required=true)
    location= serializers.CharField(required=true)
    start_time= serializers.CharField(required=true)
    finish_time= serializers.CharField(required=true)
    created_at= serializers.DateTimeField(read_only=True)

    def create(self):
        validated_data= self.validated_data
        start_time_data= validated_data.pop('start_time',None)
        finish_time_data= validated_data.pop('finish_time',None)
        if(Event.isTimeFormat() is not True):
            exceptions.FieldError("Time Format not Valid, Use Hour:Mins")
        else:
        instance = Event.objects.create(**validated_data)
        return instance


    def update(self):
        validated_data= self.validated_data
        updated_event.title= validated_data.pop('title', self.instance.title)
        updated_event.description= validated_data.pop('description', self.instance.description)
        updated_event.location= validated_data.pop('location', self.instance.location)
        updated_event.start_time= validated_data.pop('start_time', self.instance.start_time)
        updated_event.finish_time= validated_data.pop('finish_time', self.instance.finish_time)
        if(Event.isTimeFormat() is not True):
            exceptions.FieldError("Time Format not Valid, Use Hour:Mins")
        else:
            return updated_event


    def save(self):
        if self.instance is None:
            return self.create()
        else:
            return self.update()
