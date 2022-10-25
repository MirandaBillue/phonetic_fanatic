# Generated by Django 4.1.2 on 2022-10-24 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0007_delete_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='words.card')),
            ],
        ),
    ]