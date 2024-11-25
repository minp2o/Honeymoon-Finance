

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit_code', models.CharField(max_length=100)),
                ('fin_co_no', models.CharField(max_length=100)),
                ('kor_co_nm', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('dcls_month', models.CharField(max_length=20)),
                ('join_way', models.CharField(max_length=100)),
                ('mtrt_int', models.TextField(blank=True, null=True)),
                ('spcl_cnd', models.TextField(blank=True, null=True)),
                ('join_deny', models.IntegerField(blank=True, null=True)),
                ('join_member', models.TextField(blank=True, null=True)),
                ('etc_note', models.TextField(blank=True, null=True)),
                ('max_limit', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Saving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saving_code', models.CharField(max_length=100)),
                ('fin_co_no', models.CharField(max_length=100)),
                ('kor_co_nm', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('dcls_month', models.CharField(max_length=20)),
                ('join_way', models.CharField(max_length=100)),
                ('mtrt_int', models.TextField(blank=True, null=True)),
                ('spcl_cnd', models.TextField(blank=True, null=True)),
                ('join_deny', models.IntegerField(blank=True, null=True)),
                ('join_member', models.TextField(blank=True, null=True)),
                ('etc_note', models.TextField(blank=True, null=True)),
                ('max_limit', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SavingOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intr_rate_type_nm', models.CharField(max_length=2)),
                ('rsrv_type_nm', models.CharField(max_length=10)),
                ('save_trm', models.CharField(max_length=3)),
                ('intr_rate', models.FloatField(null=True)),
                ('intr_rate2', models.FloatField(null=True)),
                ('saving', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fin_ins.saving')),
            ],
        ),
        migrations.CreateModel(
            name='DepositOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intr_rate_type_nm', models.CharField(max_length=2)),
                ('save_trm', models.CharField(max_length=3)),
                ('intr_rate', models.FloatField(null=True)),
                ('intr_rate2', models.FloatField(null=True)),
                ('deposit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fin_ins.deposit')),
            ],
        ),
    ]
