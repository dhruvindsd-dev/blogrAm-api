from rest_framework import serializers
from .models import Blog, Tag, Profile
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class BlogSerializer(serializers.ModelSerializer):
    def getUsername(self, obj):
        return obj.user.username

    def getImg(self, obj):
        return f'http://127.0.0.1:8000/{obj.img}'

    def getTags(self, obj):
        tags = []
        for i in obj.tags.all():
            tags.append({'id': i.id, 'name': i.name})
        return tags

    def getDate(self, obj):
        print(obj.date)
        return obj.date.strftime('%b %y')
    username = serializers.SerializerMethodField('getUsername')
    tags = serializers.SerializerMethodField('getTags')
    img = serializers.SerializerMethodField('getImg')
    date = serializers.SerializerMethodField('getDate')

    class Meta:
        model = Blog
        exclude = ["user"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("__all__")
