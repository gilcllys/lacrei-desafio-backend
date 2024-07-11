from django.db import models
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.
class ModelBase(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ProfissionalProfile(ModelBase):
    user = models.ForeignKey(
        to=User,
        db_column= 'user_id',
        db_index=False,
        null=False,
        on_delete=models.DO_NOTHING  
    )  
    completeName = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        db_column='Complete name'
    )
    socialName = models.CharField(
        max_length=48,
        null=False,
        blank=False,
        db_column='Social name'
    )
    address = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        db_column='Address'
    )
    telephone = models.IntegerField(
        null=False,
        blank=False,
        db_column='Telephone'
    )

    class Meta:
        verbose_name = "Professional Profile"
        verbose_name_plural = "Professional Profiles"