# Generated by Django 3.0.3 on 2020-02-26 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theapps', '0002_auto_20200226_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classyear',
            name='classyear',
            field=models.IntegerField(default=2019),
        ),
        migrations.AlterField(
            model_name='friends',
            name='classyear',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theapps.ClassYear'),
        ),
        migrations.AlterField(
            model_name='friends',
            name='foods_drinks',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='friends',
            name='hobby',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='friends',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
