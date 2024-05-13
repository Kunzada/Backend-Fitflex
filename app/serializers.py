from rest_framework import serializers
from .models import *
from rest_framework import serializers    

from rest_framework import serializers
from django.core.files.base import ContentFile
import base64
import six
import uuid
import imghdr

class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Check if padding is needed
            if len(data) % 4 != 0:
                padding_needed = 4 - len(data) % 4
                data += '=' * padding_needed

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except (TypeError, binascii.Error):
                self.fail('invalid_image')

            # Generate file name
            file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough
            # Get the file name extension
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension)

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension
        return extension


class SignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username','password',]

class UserSerializer(serializers.ModelSerializer):
    Image = Base64ImageField(max_length=None, use_url=True,)
    class Meta:
        model = CustomUser
        fields = ['id','Image','username','first_name','last_name','password','weight','height','birthdate','gender']

class NotificationSerializer(serializers.ModelSerializer):
    Image = Base64ImageField(max_length=None, use_url=True,)
    class Meta:
        model = Notification
        fields = ['id','Image','title','subtitle']

class GoalOfTheDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalOfTheDay
        fields = ['id','waterIntake','footSteps','fluidDram']

class LatestActivitiesSerializer(serializers.ModelSerializer):
    Image = Base64ImageField(max_length=None, use_url=True,)
    class Meta:
        model = LatestActivities
        fields = ['id','Image','title','subtitle','UserID']

class WorkoutSerializer(serializers.ModelSerializer):
    Image = Base64ImageField(max_length=None, use_url=True,)
    class Meta:
        model = Workout
        fields = ['id','title','Image','numberOfPromotions','minute','calories',"UserID"]

class ExerciseSerializer(serializers.ModelSerializer):
    Image = Base64ImageField(max_length=None, use_url=True,)
    class Meta:
        model=Exercise
        fields = ['id','title','Image','description','video','difficulty',"workoutID"]

class PlanSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Plan
        fields = ['id','title','description','exerciseID','foodID','modelType']

class FoodSerializer(serializers.ModelSerializer):
    Image = Base64ImageField(max_length=None, use_url=True,)
    class Meta:
        model = Food
        fields = ['id','title','image','description','difficulty','time','IsPopular','author']

class RecipeSerializer(serializers.ModelSerializer):
    Image = Base64ImageField(max_length=None, use_url=True,)
    class Meta:
        model = Recipe
        fields= ['id','title','image','grammes','FoodID']

class NutrionSerializer(serializers.ModelSerializer):
    icon = Base64ImageField(max_length=None, use_url=True,)
    class Meta:
        model = Nutrion
        fields = ['id','unit','icon','grammes','FoodID']