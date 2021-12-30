from django.db import models

# Create your models here.




class Patient(models.Model):
    patient_id = models.CharField(db_column='Patient_Id', primary_key=True, max_length=5)  # Field name made lowercase.
    patient_name = models.CharField(db_column='Patient_Name', max_length=20)  # Field name made lowercase.
    contact_num = models.CharField(max_length=11)
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50)  # Field name made lowercase.
    patient_blood_group = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'patient'


class Story(models.Model):
    patient_id = models.CharField(max_length=10, primary_key=True)
    story_date = models.DateField()
    comment = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'story'




