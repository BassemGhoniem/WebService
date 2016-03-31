from rest_framework import serializers

from .models import Post

from django.contrib.auth.models import User



# class UserSerializer(serializers.ModelSerializer):
#     posts = serializers.HyperlinkedIdentityField('posts', view_name='userpost-list', lookup_field='username')

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'first_name', 'last_name', 'posts', )


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedIdentityField('posts' , view_name='userpost-list' , lookup_field='username' )

    class Meta:
        model=User
        fields = ('id','username','first_name','last_name','posts')



class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=false)
    

    def get_validation_exclusions(self):

        exclusions = super(PostSerializer , self).get_validation_exclusions()
        return exclusions + ['author']

    class Meta:
        model=Post   

         