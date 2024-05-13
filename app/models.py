from django.db import models
from django.core.validators import EmailValidator,FileExtensionValidator
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    class Gender(models.TextChoices):
        Man = 'Мужской'
        Woman =  'Женский'  
        
    Image=models.ImageField(upload_to='userprofile/',blank=True,default='icon'.join(str(i) for i in range(1,5))+".png",verbose_name="Фото",)
    weight=models.FloatField(default=0.0,verbose_name="Вес")
    height=models.IntegerField(default=0,verbose_name="Рост")
    birthdate=models.DateField(verbose_name="Дата рождения",default='2000-01-01')
    gender=models.CharField(max_length=10,choices=Gender.choices,default=Gender.Man,verbose_name="Пол")
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="Дата создания")
    update_at=models.DateTimeField(auto_now=True,verbose_name="Дата обновления")
    
    def __str__(self):
        return self.first_name 
    
    class Meta:
        verbose_name="Пользователь"
        verbose_name_plural="Пользователи"
    
class Notification(models.Model):
    Image=models.ImageField(upload_to='notification/',verbose_name="Картинка")
    title=models.CharField(max_length=100,verbose_name="Заголовок")
    subtitle=models.CharField(max_length=100,verbose_name="Подзаголовок")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Уведомление"
        verbose_name_plural="Уведомления"
        

class GoalOfTheDay(models.Model):
    class FluidDram(models.TextChoices):
        L = 'л','Литр'
        ML =  'мл','Миллилитр'
    waterIntake=models.IntegerField()
    fluidDram=models.CharField(max_length=2,choices=FluidDram.choices,default=FluidDram.L)
    footSteps=models.IntegerField()
    update_at=models.DateTimeField(auto_now=True)
    


class LatestActivities(models.Model):
    title=models.CharField(max_length=100)
    Image=models.ImageField(upload_to='latest_activities/')
    subtitle=models.CharField(max_length=100)
    UserID=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

class Workout(models.Model):
    title=models.CharField(max_length=100)
    Image=models.ImageField(upload_to='workout/')
    numberOfPromotions=models.IntegerField()
    minute=models.IntegerField()
    calories=models.IntegerField()
    UserID=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
   
class Exercise(models.Model):
    class Difficulty(models.TextChoices):
        EASY="Начинающий"
        MEDIUM="Средний"
        HARD="Продвинутый"
    Image=models.ImageField(upload_to='workout/')
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    description=models.TextField()
    video=models.FileField(upload_to='videos_uploaded',null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    difficulty=models.CharField(max_length=100,choices=Difficulty.choices,default=Difficulty.EASY)
    workoutID=models.ForeignKey(Workout,on_delete=models.CASCADE)

class Food(models.Model):
    class Popular(models.TextChoices):
        Yes="Да"
        No="Нет"
    class Difficulty(models.TextChoices):
        EASY="Начинающий"
        MEDIUM="Средний"
        HARD="Продвинутый"
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='food/')
    description=models.TextField()
    difficulty=models.CharField(max_length=100,choices=Difficulty.choices,default=Difficulty.EASY)
    time=models.IntegerField()
    IsPopular=models.CharField(max_length=20,choices=Difficulty.choices,default=Difficulty.EASY)
    author=models.CharField(max_length=255)
    
class Recipe(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='recipe/')
    grammes=models.FloatField()
    FoodID=models.ForeignKey(Food,on_delete=models.CASCADE)
class Plan(models.Model):
    class ModelType(models.TextChoices):
        EXERCISE = 'Exercise', 'Exercise'
        FOOD = 'Food', 'Food'
    title=models.CharField(max_length=100)
    description=models.TextField()
    exerciseID = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True, blank=True)
    foodID = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True)
    modelType=models.CharField(max_length=100,choices=ModelType.choices)

class Nutrion(models.Model):
    icon=models.ImageField(upload_to='nutrion/'),
    grammes=models.FloatField()
    unit=models.CharField(max_length=100)
    FoodID=models.ForeignKey(Food,on_delete=models.CASCADE)




