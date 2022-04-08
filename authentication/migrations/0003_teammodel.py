# Generated by Django 4.0.3 on 2022-04-08 05:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('size', models.PositiveSmallIntegerField()),
                ('members', models.ManyToManyField(to='authentication.participantsmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
