from django.db import models

# Create your models here.





class OrganDonate(models.Model):
    patient_id = models.CharField(max_length=10, primary_key=True)
    user_id = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=5)
    contact_num = models.CharField(max_length=11, blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    need_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organ_donate'




class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    blood_group = models.CharField(max_length=3)
    age = models.CharField(max_length=3)
    email = models.CharField(max_length=30)
    user_type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'user'