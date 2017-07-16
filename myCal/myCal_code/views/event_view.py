from rest_framework import viewsets, exceptions
from rest_framework.response import Response
from django.db import transaction, connection
from rest_framework.decorators import detail_route, list_route
from myCal_code.serializers import EventSerializer

class EventViewSet(viewsets.ViewSet):
	@transaction.atomic
	def create(self, *args, **kwargs):
		serializer= EventSerializer(data= self.request.data)
		serializer.is_valid(raise_exception=true)
		instance= serializer.save()
		return Response(EventSerializer(instance).data, status=201)

	@transaction.atomic
	def update(self, *args, **kwargs):
		instance = self.get_instance_from_url()
		serializer= EventSerializer(instance, partial=True, data=self.request.data)
		serializer.is_valid(raise_exception=True)
		instance = serializer.save()
		return Response(EventSerializer(instance).data)

	@transaction.atomic
	def destroy(self, *agrs, **kwars):
		instance= self.get_instance_from_url()



    def get_instance_from_url(self):
        pk = self.request.parser_context['kwargs'].get('pk', None)
        if pk is None:
            raise exceptions.ParseError('no pk')
        return Profile.objects.get(pk=pk)
