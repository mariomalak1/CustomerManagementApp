from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(User):
    profilePic = models.ImageField(upload_to="media/profilePics")