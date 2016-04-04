from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    # blank means required form field .... null means can be null in the DB
    full_name = models.CharField(max_length=120, blank=True, null=True)
    # auto_now_add: add time only when created.
    # auto_now: add time only when updated.
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self): # Python 3.3 is __str__
        return self.email
