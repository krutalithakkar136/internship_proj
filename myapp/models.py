from django.db import models
from django.apps import AppConfig
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser    

# Create your models here.
class Pract_Signup(models.Model):
    name=models.CharField(max_length=15)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=50)
    password=models.TextField()

    def __str__(self):
        return self.name

class Tasks(models.Model):
    t_name=models.TextField()
    t_desc=models.CharField(max_length=50)
    cat=models.TextField()
    status=models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.t_name

class FurnitureInfo(models.Model):
    Furniture_name=models.CharField(max_length=30)
    Furniture_desc=models.CharField(max_length=50)
    Furniture_modelno=models.PositiveIntegerField()
    Furniture_cat=models.CharField(max_length=30)
    def __str__(self):
        return self.Furniture_name
    
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    message=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Demo(models.Model):
    name=models.TextField()
    data=models.JSONField(null=True)

    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=512)


class Book(models.Model):
    title = models.CharField(max_length=512)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return "Title :"+self.title+","+"Id :"+str(self.id)  
    

class MyUserManager(BaseUserManager):
    def create_user(self,email,date_of_birth,password=None):
        if not email:
            raise ValueError("email is mandatory")
        user=self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, date_of_birth, password=None):
        user=self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_perm = True
        user.save(using=self._db)
        return user
    

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # is_perm = models.BooleanField(default=False)
    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["date_of_birth"]

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    def __str__(self):
        return self.email