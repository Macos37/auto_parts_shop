from django.db import models


class BaseModel(models.Model):

    create_time = models.DateTimeField('Create time', auto_now_add=True)
    update_time = models.DateTimeField('Update time', auto_now=True)

    class Meta:
        abstract = True