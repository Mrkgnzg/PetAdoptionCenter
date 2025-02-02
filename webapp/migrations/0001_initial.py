# Generated by Django 5.1.4 on 2025-01-02 10:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('description', models.TextField()),
                ('medical_history', models.TextField()),
                ('care_needs', models.TextField()),
                ('photo', models.ImageField(upload_to='animals/')),
                ('available_for_adoption', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(blank=True, null=True)),
                ('description', models.TextField()),
                ('is_verified', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Adopter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('preferences', models.TextField()),
                ('date_registered', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdoptionRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('approval_date', models.DateTimeField(blank=True, null=True)),
                ('adopter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.adopter')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor_name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('donation_date', models.DateTimeField(auto_now_add=True)),
                ('anonymous', models.BooleanField(default=False)),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donations', to='webapp.shelter')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='shelter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animals', to='webapp.shelter'),
        ),
    ]
