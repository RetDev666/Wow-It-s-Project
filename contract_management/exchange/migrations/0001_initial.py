# Generated by Django 4.2.14 on 2024-07-10 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Broker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Brokerage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('buy', 'Buy'), ('sell', 'Sell')], max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('broker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.broker')),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.commodity')),
            ],
        ),
        migrations.AddField(
            model_name='broker',
            name='brokerage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.brokerage'),
        ),
    ]