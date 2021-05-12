from rest_framework import serializers
from api.models import Region

class RegionsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Region
		fields = '__all__'