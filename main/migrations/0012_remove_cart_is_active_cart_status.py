# Generated by Django 5.0.4 on 2024-04-04 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_enterproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='is_active',
        ),
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.IntegerField(choices=[(1, 'No Faol'), (2, 'Yo`lda'), (3, 'Qaytarilgan'), (4, 'Qabul qilingan')], default=1),
            preserve_default=False,
        ),
    ]
