from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return '{self.user.username} Profile'

    def get_absolute_url(self):
        return reverse('user-posts', kwargs={'pk': self.username})
# Create your models here.
