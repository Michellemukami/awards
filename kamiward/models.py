from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Profile(models.Model): 
    profile_image = models.ImageField(upload_to = 'profile/', blank=True)
    username = models.CharField(max_length =60,primary_key=True)
    gender = models.CharField(max_length =60)
    bio = HTMLField()
    user_id = models.IntegerField(default=0)


class Project(models.Model):
    title = models.CharField(max_length=60)
    post = HTMLField()
    profile = models.ForeignKey(User, null=False,default=1)
    user = models.ForeignKey(Profile)
    pub_date = models.DateTimeField(auto_now_add=True)
    project_image = models.ImageField(upload_to='project/', blank=True)
    url= models.CharField(max_length=100)
    def __str__(self):
        return self.title
    def save_Project(self):
        self.save()

  
    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)

    
    @classmethod
    def search_by_title(cls,search_term):
        posts = cls.objects.filter(title__icontains=search_term)
        return posts

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
