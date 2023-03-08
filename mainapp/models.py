from django.db import models

class CompanyMetrc(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name


class LabelCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Label(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    category = models.ForeignKey(LabelCategory,on_delete=models.CASCADE,default=1)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.title