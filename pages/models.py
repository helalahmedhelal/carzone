from django.db import models

# Create your models here.
class Team(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='team_images/%Y/%m/%d/')
    designation=models.CharField(max_length=50)
    facebook_link=models.URLField()
    twitter_link=models.URLField()
    googleplus_link=models.URLField()
    created_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return f'{self.first_name} {self.last_name}'