# Generated by Django 4.0.4 on 2022-05-04 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_alter_paciente_diagnostico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='AIE',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='ASJ',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='CS',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='DST',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='ECG',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='FCM',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='IST',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='NVP',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='PAR',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='TDP',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='talassemia',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
