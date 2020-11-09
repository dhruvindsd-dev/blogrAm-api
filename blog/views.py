from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

from .serializer import BlogSerializer
from .models import Blog


@api_view(['POST'])
def signUp(request):
    data = request.data
    if 'username' in data and 'password' in data and 'email' in data:
        try:
            user = User.objects.get(username=request.data['username'])
        except:
            # some error occured and the user doesnt exist, create a user in that case
            user = User.objects.create(
                username=request.data['username'],
                password=request.data['password'],
                email=request.data['email'])
            token = Token.objects.get(user=user)
            return Response({
                'token': token.key,
                'username': user.username,
                'email': user.email
                # 'user': user.username,
            }, status=status.HTTP_201_CREATED)
        else:
            # user aldready exists.
            return Response({
                'error': 'user_exists'
            }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({
            'error': 'invalid_fields'
        })


@api_view(['POST'])
def getToken(request):
    data = request.data
    if 'email' in data and 'password' in data:
        # all valid credentials are there
        try:
            user = User.objects.get(
                email=data['email'], password=data['password'])
        except:
            # the credentials are invalid.
            return Response({'error': 'invalid_credentials'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # success we can send the dem token
            token = Token.objects.get(user=user)
            return Response({
                'token': token.key,
                'username': user.username,
                'email': user.email
            }, status=status.HTTP_200_OK)

    else:
        return Response({
            'error': 'invalid_fields'
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getUserBlogs(request):
    # gives all the blogs of the user from the username
    if 'username' in request.data:
        try:
            user = User.objects.get(username=request.data['username'])
        except:
            return Response({
                'error': 'invalid_username'
            },  status=status.HTTP_400_BAD_REQUEST)
        else:
            blogs = Blog.objects.filter(user=user)
            serializer = BlogSerializer(blogs, many=True)
            return Response(serializer.data,  status=status.HTTP_200_OK)
    else:
        return Response({
            "error": 'invalid_fields'
        },  status=status.HTTP_400_BAD_REQUEST)


# new user blog
# get

@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def newUserBlog(request):
    # check for all the fields
    # then check for the suitable tags
    # if new tag then create a new tag and then link it
    # send a success create response
    data = request.data
    print(data)
    print(Blog.objects.filter(user=request.user))
    if 'title' in data and 'subtitle' in data and 'content' in data:
        blog = Blog.objects.create(
            title=data['title'],
            subtitle=data['subtitle'],
            content=data['content'],
            user=request.user,

        )
        return Response({
            'type': 'success'
        })

        # check all the tags
    else:
        return Response({
            'error': 'invalid_fields'
        })


@api_view(['GET'])
def getBlogs(request):
    blogs = BlogSerializer(Blog.objects.all(), many=True)
    print(blogs)
    return Response({
        'blogs': blogs.data
    })