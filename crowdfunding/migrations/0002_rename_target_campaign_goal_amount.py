# Generated by Django 4.1.7 on 2023-03-13 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfunding', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaign',
            old_name='target',
            new_name='goal_amount',
        ),
    ]