# Generated by Django 5.1.1 on 2024-09-06 09:36

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, related_name='customuser_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='customuser_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ScholarshipApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_form', models.FileField(blank=True, null=True, upload_to='documents/application_form/')),
                ('passport_photographs', models.FileField(blank=True, null=True, upload_to='documents/passport_photographs/')),
                ('identity_proof', models.FileField(blank=True, null=True, upload_to='documents/identity_proof/')),
                ('address_proof', models.FileField(blank=True, null=True, upload_to='documents/address_proof/')),
                ('class_10_marksheet', models.FileField(blank=True, null=True, upload_to='documents/class_10_marksheet/')),
                ('class_12_marksheet', models.FileField(blank=True, null=True, upload_to='documents/class_12_marksheet/')),
                ('income_certificate', models.FileField(blank=True, null=True, upload_to='documents/income_certificate/')),
                ('caste_certificate', models.FileField(blank=True, null=True, upload_to='documents/caste_certificate/')),
                ('domicile_certificate', models.FileField(blank=True, null=True, upload_to='documents/domicile_certificate/')),
                ('bank_account_details', models.FileField(blank=True, null=True, upload_to='documents/bank_account_details/')),
                ('bonafide_certificate', models.FileField(blank=True, null=True, upload_to='documents/bonafide_certificate/')),
                ('fee_receipts', models.FileField(blank=True, null=True, upload_to='documents/fee_receipts/')),
                ('proof_of_admission', models.FileField(blank=True, null=True, upload_to='documents/proof_of_admission/')),
                ('academic_transcripts', models.FileField(blank=True, null=True, upload_to='documents/academic_transcripts/')),
                ('disability_certificate', models.FileField(blank=True, null=True, upload_to='documents/disability_certificate/')),
                ('passport_for_international', models.FileField(blank=True, null=True, upload_to='documents/passport/')),
                ('document_status', models.CharField(default='pending', max_length=20)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'student'), (2, 'admin')])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('college_name', models.CharField(max_length=255)),
                ('program', models.CharField(max_length=255)),
                ('year_of_study', models.PositiveIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='studentprofile', to='students.user')),
            ],
        ),
    ]
