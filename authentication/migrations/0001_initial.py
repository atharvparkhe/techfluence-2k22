# Generated by Django 4.0.3 on 2022-04-12 06:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddOrganiserModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='organiser_excel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CollegeModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('college_name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
