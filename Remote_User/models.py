from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

class clone_accounts_model(models.Model):

    uname= models.CharField(max_length=300)
    dob= models.CharField(max_length=300)
    gender= models.CharField(max_length=300)
    address= models.CharField(max_length=300)
    location= models.CharField(max_length=300)
    mailid= models.CharField(max_length=300)
    mobile_no= models.CharField(max_length=300)
    names= models.CharField(max_length=300)
    tweet_desc= models.CharField(max_length=300)
    tweet_loc= models.CharField(max_length=300)
    tweet_date= models.CharField(max_length=300)
    score= models.IntegerField()

class clone1_accounts_model(models.Model):

    uname= models.CharField(max_length=300)
    dob= models.CharField(max_length=300)
    gender= models.CharField(max_length=300)
    address= models.CharField(max_length=300)
    location= models.CharField(max_length=300)
    mailid= models.CharField(max_length=300)
    mobile_no= models.CharField(max_length=300)
    names= models.CharField(max_length=300)
    tweet_desc= models.CharField(max_length=300)
    tweet_loc= models.CharField(max_length=300)
    tweet_date= models.CharField(max_length=300)
    score= models.IntegerField()

class fake_accounts_model(models.Model):

    uname= models.CharField(max_length=300)
    dob= models.CharField(max_length=300)
    gender= models.CharField(max_length=300)
    address= models.CharField(max_length=300)
    location= models.CharField(max_length=300)
    mailid= models.CharField(max_length=300)
    mobile_no= models.CharField(max_length=300)
    names= models.CharField(max_length=300)
    tweet_desc= models.CharField(max_length=300)
    tweet_loc= models.CharField(max_length=300)
    tweet_date= models.CharField(max_length=300)
    score= models.IntegerField()


class tweet_accuracy_model(models.Model):

    names = models.CharField(max_length=300)
    accuracy = models.CharField(max_length=300)

class review_Model(models.Model):
    uname = models.CharField(max_length=100)
    ureview = models.CharField(max_length=100)
    sanalysis = models.CharField(max_length=100)
    dt= models.CharField(max_length=300)
    tname= models.CharField(max_length=300)
    feedback = models.CharField(max_length=300)

class recommend_Model(models.Model):
    uname1 = models.CharField(max_length=100)
    pname = models.CharField(max_length=100)
    loc = models.CharField(max_length=100)
    dt= models.CharField(max_length=300)
    usefull= models.CharField(max_length=300)




