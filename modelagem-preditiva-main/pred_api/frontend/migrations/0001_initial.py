# Generated by Django 4.0.4 on 2022-05-04 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paciente', models.IntegerField()),
                ('hospital', models.CharField(max_length=1)),
                ('idade', models.IntegerField()),
                ('sexo', models.CharField(max_length=1)),
                ('TDP', models.IntegerField()),
                ('PAR', models.FloatField()),
                ('CS', models.FloatField()),
                ('ASJ', models.IntegerField()),
                ('ECG', models.IntegerField()),
                ('FCM', models.FloatField()),
                ('AIE', models.IntegerField()),
                ('DST', models.FloatField()),
                ('IST', models.IntegerField()),
                ('NVP', models.IntegerField()),
                ('talassemia', models.IntegerField()),
                ('diagnostico', models.IntegerField()),
            ],
        ),
    ]