# Generated by Django 3.2.8 on 2021-12-15 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_user1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=10)),
                ('story_date', models.DateField()),
                ('comment', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'story',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]