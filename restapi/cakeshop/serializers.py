from rest_framework import serializers
from restapi.cakeshop.models import Cake


class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        fields = ('id',
                  'name',
                  'comment',
                  'yumFactor')
