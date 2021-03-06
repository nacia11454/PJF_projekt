# Generated by Django 4.0.1 on 2022-01-17 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('green', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_us', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='plant',
            name='buy_date',
        ),
        migrations.AlterField(
            model_name='group',
            name='name_gr',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='plant',
            name='name_pl',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Care',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('care_date', models.DateTimeField(verbose_name='Data pielegnacji')),
                ('note', models.CharField(max_length=200)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='green.plant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='green.user')),
            ],
        ),
    ]
