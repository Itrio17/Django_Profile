from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField
import datetime

# Create your models here.
class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to="portfolio/images/")
    url = URLField(blank=True)


class Technologies(models.Model):
    title = CharField(max_length=100)
    image = ImageField(upload_to="tech/images")


class Contacto(models.Model):
    email = CharField(max_length=100)
    number = CharField(max_length=100)
    linkedin = URLField(blank=True)
    github = URLField(blank=True)


class Experience(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=1000)
    date_init = models.DateField(datetime.date)
    date_end = models.DateField(datetime.date)
    image = ImageField(upload_to="Experience/images")