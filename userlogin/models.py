from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
class profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id_user=models.IntegerField()
    bio=models.TextField(blank=True)
    #profileing=models.ImageField(upload_to='profile_images',default='de.jpj')
    location=models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.user.username