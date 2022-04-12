# Generated by Django 4.0.3 on 2022-04-12 06:54

import authentication.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganisersModel',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('photo', models.ImageField(null=True, upload_to='organiser')),
                ('token', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('base.baseuser',),
        ),
        migrations.CreateModel(
            name='ParticipantsModel',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('vaccination', models.FileField(blank=True, null=True, upload_to='vaccination', validators=[authentication.validators.validate_file_extension_2, authentication.validators.validate_file_size])),
                ('aadhar', models.FileField(blank=True, null=True, upload_to='aadhar', validators=[authentication.validators.validate_file_extension_2, authentication.validators.validate_file_size])),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_college', to='authentication.collegemodel')),
            ],
            options={
                'abstract': False,
            },
            bases=('base.baseuser',),
        ),
        migrations.CreateModel(
            name='TeamModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('team_username', models.CharField(max_length=50, unique=True)),
                ('size', models.PositiveSmallIntegerField()),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_leader', to='authentication.participantsmodel')),
                ('members', models.ManyToManyField(to='authentication.participantsmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
