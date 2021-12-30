from django.db import models
from django.template.defaultfilters import slugify

class Post(models.Model):
    ...
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Appointment(models.Model):
    appointment_id = models.CharField(db_column='Appointment_Id', primary_key=True, max_length=15)  # Field name made lowercase.
    patient_id = models.CharField(max_length=10)
    doctor_id = models.CharField(max_length=10)
    appointment_date = models.DateTimeField(db_column='Appointment_Date', blank=True, null=True)  # Field name made lowercase.

class Meta:
        managed = False
        db_table = 'appointment'