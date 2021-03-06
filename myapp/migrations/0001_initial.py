# Generated by Django 3.2.12 on 2022-04-08 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=17)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubDistrict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subdistricts', to='myapp.district')),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='divisions', to='myapp.country')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='districts', to='myapp.division'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addressof', models.CharField(max_length=100)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country_set', to='myapp.country')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='district_set', to='myapp.district')),
                ('division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='division_set', to='myapp.division')),
                ('subdistrict', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subdistrict_set', to='myapp.subdistrict')),
            ],
        ),
    ]
