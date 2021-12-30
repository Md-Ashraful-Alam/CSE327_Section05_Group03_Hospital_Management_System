from django.db import models

# Create your models here.



class Appointment(models.Model):
    appointment_id = models.CharField(db_column='Appointment_Id', primary_key=True, max_length=15)  # Field name made lowercase.
    patient_id = models.CharField(max_length=10)
    doctor_id = models.CharField(max_length=10)
    appointment_date = models.DateTimeField(db_column='Appointment_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'appointment'



class Doctor(models.Model):
    doctorid = models.CharField(db_column='Doctorid', primary_key=True, max_length=6)  # Field name made lowercase.
    user_id = models.CharField(max_length=10)
    doctor_name = models.CharField(db_column='Doctor_Name', max_length=15)  # Field name made lowercase.
    contact_num = models.CharField(max_length=11)
    email = models.CharField(max_length=30)
    meet_link = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'doctor'


class Test(models.Model):
    test_id = models.CharField(db_column='Test_Id', primary_key=True, max_length=6)  # Field name made lowercase.
    patient_id = models.CharField(db_column='Patient_ID', max_length=5)  # Field name made lowercase.
    test_charge = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'test'



class User1(models.Model):
    username = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    repassword = models.CharField(max_length=30)