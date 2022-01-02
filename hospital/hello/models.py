from django.db import models

# Create your models here.






class Medicine(models.Model):
    medicine_id = models.CharField(db_column='Medicine Id', primary_key=True, max_length=15)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    medicine_name = models.CharField(db_column='Medicine Name', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_id = models.CharField(max_length=10)
    expired_date = models.DateTimeField(db_column='Expired Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.    
    price = models.SmallIntegerField(db_column='Price')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medicine'


class Nurse(models.Model):
    nurse_id = models.CharField(db_column='Nurse_ID', primary_key=True, max_length=6)  # Field name made lowercase.
    nurse_name = models.CharField(db_column='Nurse_Name', max_length=15)  # Field name made lowercase.
    floor_no = models.IntegerField(db_column='Floor_No')  # Field name made lowercase.
   # bed_no = models.ForeignKey(Bed, models.DO_NOTHING, db_column='Bed_No')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nurse'


