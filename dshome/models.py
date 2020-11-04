from django.db import models


class DsHome(models.Model):
        username = models.TextField(max_length='255')
        userrole = models.TextField(max_length='225')
        password = models.CharField
        login = models.BooleanField
        submit = models.BooleanField
        approved = models.BooleanField
