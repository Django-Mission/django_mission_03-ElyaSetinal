# Generated by Django 4.0.4 on 2022-04-19 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_inquiry_email_allow_inquiry_sms_allow_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(max_length=100, verbose_name='질문'),
        ),
    ]