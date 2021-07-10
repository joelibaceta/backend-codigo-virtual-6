from rest_framework import serializers

class CategorySerializer(serializers.Serializer):
    categoria_nom = serializers.CharField(max_length=50)

class PlatoSerializer(serializers.Serializer):

    plato_id = serializers.SerializerMethodField('get_plato_id')
    plato_nom = serializers.CharField(max_length=50)
    plato_img = serializers.CharField(max_length=50)
    plato_pre = serializers.FloatField()
    Categorium = serializers.SerializerMethodField('get_categorium')

    def get_plato_id(self, obj):
        return obj.id
    
    def get_categorium(self, obj):
        serializer = CategorySerializer(obj.categoria)
        return serializer.data
