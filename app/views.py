from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *  
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
class NotificationList(ListAPIView):
    queryset=Notification.objects.all()
    serializer_class=NotificationSerializer

class NotificationCreate(CreateAPIView):
    queryset=Notification.objects.all()
    serializer_class=NotificationSerializer

class GoalOfTheDayUpdate(UpdateAPIView):
    queryset=GoalOfTheDay.objects.all()
    serializer_class=GoalOfTheDaySerializer

class GoalOfTheDayDetail(RetrieveAPIView):
    queryset=GoalOfTheDay.objects.all()
    serializer_class=GoalOfTheDaySerializer

class GoalOfTheDayCreate(CreateAPIView):
    queryset=GoalOfTheDay.objects.all()
    serializer_class=GoalOfTheDaySerializer

class LatestActivitiesList(ListAPIView):
    serializer_class=LatestActivitiesSerializer
    queryset=LatestActivities.objects.all()

class LatestActivitiesDetail(RetrieveAPIView):
    queryset=LatestActivities.objects.all()
    serializer_class=LatestActivitiesSerializer


class LatestActivitiesCreate(CreateAPIView):
    queryset=LatestActivities.objects.all()
    serializer_class=LatestActivitiesSerializer

class WorkoutList(ListAPIView):
    queryset=Workout.objects.all()
    serializer_class=WorkoutSerializer

class WorkoutDetail(RetrieveAPIView):
    queryset=Workout.objects.all()
    serializer_class=WorkoutSerializer

class WorkoutCreate(CreateAPIView):
    queryset=Workout.objects.all()
    serializer_class=WorkoutSerializer

class ExerciseList(ListAPIView):
    queryset=Exercise.objects.all()
    serializer_class=ExerciseSerializer

class ExerciseDetail(RetrieveAPIView):
    queryset=Exercise.objects.all()
    serializer_class=ExerciseSerializer   

class ExerciseCreate(CreateAPIView):
    queryset=Exercise.objects.all()
    serializer_class=ExerciseSerializer   

class PlanList(ListAPIView):
    queryset=Plan.objects.all()
    serializer_class=PlanSerializer

class PlanCreate(CreateAPIView):
    queryset=Plan.objects.all()
    serializer_class=PlanSerializer
    
class SignUp(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user=CustomUser.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            return Response({"message":"user created successfully","success":True},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
class SignIn(APIView):
    def post(self,request):
        # data=request.data
        # user=CustomUser.objects.get(email=data['email'])
        
        username=request.data['username']
        password=request.data['password']
        user=CustomUser.objects.filter(username=username).first()
        if user is None:
            return Response({"message":"user not found","success":False},status=status.HTTP_404_NOT_FOUND)
        if not user.check_password(password):
            return Response({"message":"password incorrect","success":False},status=status.HTTP_400_BAD_REQUEST)
        token=RefreshToken.for_user(user)
        return Response({"message":"login successful","token":str(token),"success":True},status=status.HTTP_200_OK)

class FoodList(ListAPIView):
    queryset=Food.objects.all()
    serializer_class=FoodSerializer

class FoodDetail(RetrieveAPIView):
    queryset=Food.objects.all()
    serializer_class=FoodSerializer

class FoodCreate(CreateAPIView):
    queryset=Food.objects.all()
    serializer_class=FoodSerializer


class RecipeList(ListAPIView):
    queryset=Recipe.objects.all()
    serializer_class=RecipeSerializer

class RecipeCreate(CreateAPIView):
    queryset=Recipe.objects.all()
    serializer_class=RecipeSerializer

class RecipeDetail(RetrieveAPIView):
    queryset=Recipe.objects.all()
    serializer_class=RecipeSerializer

class NutrionList(ListAPIView):
    queryset=Nutrion.objects.all()
    serializer_class=NutrionSerializer

class NutrionDetail(RetrieveAPIView):
    queryset=Nutrion.objects.all()
    serializer_class=NutrionSerializer

class NutrionCreate(CreateAPIView):
    queryset=Nutrion.objects.all()
    serializer_class=NutrionSerializer

class Logout(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            try:
                # Attempt to retrieve the authentication token
                token = Token.objects.get(user=request.user)
                # Delete the token
                token.delete()
                return Response({"message": "Logout successful", "success": True}, status=status.HTTP_200_OK)
            except Token.DoesNotExist:
                # Token doesn't exist, maybe the user is already logged out
                return Response({"message": "User is already logged out", "success": True}, status=status.HTTP_200_OK)
        else:
            # User is not authenticated, handle appropriately
            return Response({"message": "User is not authenticated", "success": False}, status=status.HTTP_401_UNAUTHORIZED)
class ProfileDetail(RetrieveAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializer