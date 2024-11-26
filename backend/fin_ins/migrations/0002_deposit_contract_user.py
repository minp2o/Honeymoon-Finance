

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fin_ins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='contract_user',
            field=models.ManyToManyField(related_name='contract_deposit', to=settings.AUTH_USER_MODEL),
        ),
    ]
