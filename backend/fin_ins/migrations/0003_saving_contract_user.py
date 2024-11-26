

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fin_ins', '0002_deposit_contract_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='saving',
            name='contract_user',
            field=models.ManyToManyField(related_name='contract_saving', to=settings.AUTH_USER_MODEL),
        ),
    ]
