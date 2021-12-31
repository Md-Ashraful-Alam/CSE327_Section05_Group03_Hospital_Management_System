from django.db import models

# Create your models here.


class Bed(models.Model):
    bed_id = models.CharField(primary_key=True, max_length=30)
    bed_type = models.CharField(db_column='Bed_Type', max_length=15)  # Field name made lowercase.
    vacancy = models.CharField(db_column='Vacancy', max_length=1)  # Field name made lowercase.
    bed_charge = models.IntegerField(db_column='Bed_Charge')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bed'


class BloodDonate(models.Model):
    patient_id = models.CharField(max_length=10, primary_key=True)
    user_id = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=5)
    contact_num = models.CharField(max_length=11, blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    need_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blood_donate'

