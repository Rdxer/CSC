from django.db import models

# Create your models here.


class Complain(models.Model):
    """
    投诉
    """
    note = models.CharField('备注', max_length=300, blank=True)
    note2 = models.CharField('备注2', max_length=300, blank=True)

    class Meta:
        verbose_name = '投诉'
        verbose_name_plural = '投诉的数据'

