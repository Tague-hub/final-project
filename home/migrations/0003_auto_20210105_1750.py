# Generated by Django 3.1.4 on 2021-01-05 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210104_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sending_date', models.DateField(auto_now=True)),
                ('content', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages', models.CharField(blank=True, max_length=500)),
                ('answers', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='users',
            name='imageprofil',
        ),
        migrations.DeleteModel(
            name='Messages',
        ),
        migrations.AddField(
            model_name='inbox',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipient', to='home.users'),
        ),
        migrations.AddField(
            model_name='inbox',
            name='transmitter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transmitter', to='home.users'),
        ),
        migrations.AddField(
            model_name='forums',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forums', to='home.users'),
        ),
    ]
