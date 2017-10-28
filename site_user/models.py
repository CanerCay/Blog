from django.db import models
from solo.models import SingletonModel
from django.core.validators import MaxValueValidator, MinValueValidator


class SiteUser(SingletonModel):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    birthday = models.DateField(null=True, blank=False)
    photo = models.ImageField(upload_to="config/images/%Y/%m/%d")
    job_title = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True)
    national = models.CharField(max_length=50, null=True)
    languages = models.CharField(max_length=50, null=True)
    biography = models.TextField(max_length=2000)
    about_all = models.TextField(max_length=5000)

    def __str__(self):
        return u"Site User"


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.TextField(max_length=200)
    message = models.TextField(max_length=500)

    def __str__(self):
        return u"name :{0} subject : {1}".format(self.name, self.subject)


class Skill(models.Model):
    skill = models.CharField(max_length=50)
    value = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])

    def __str__(self):
        return u"skill :{0} value : {1}".format(self.skill, self.value)


class Experience(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to="experience/images/%Y/%m/%d")

    def __str__(self):
        return u"title :{0}".format(self.title)


class Education(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to="education/images/%Y/%m/%d")

    def __str__(self):
        return u"title :{0}".format(self.title)


class Project(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    date = models.DateField()
    image = models.ImageField(upload_to="project/images/%Y/%m/%d")
    url = models.URLField(max_length=150, null=True, blank=True)

    def __str__(self):
        return u"title :{0}".format(self.title)
