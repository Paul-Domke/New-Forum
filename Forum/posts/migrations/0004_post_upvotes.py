# Generated by Django 2.2.6 on 2019-10-23 00:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upvotes',
            field=models.ManyToManyField(related_name='upvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]
