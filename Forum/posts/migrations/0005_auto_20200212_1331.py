# Generated by Django 2.2.6 on 2020-02-12 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_upvotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='posts.Tag'),
        ),
    ]