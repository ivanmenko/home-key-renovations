# Generated by Django 4.0.4 on 2022-04-15 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digital_warehouse', '0005_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('pricing_materials', models.FloatField(default=0.0)),
                ('bill_for_service', models.FloatField(default=0.0)),
                ('total_cost', models.FloatField(default=0.0)),
                ('confirmed', models.BooleanField(default=False)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digital_warehouse.client')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1)),
                ('pricing', models.FloatField(default=0.0)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='digital_warehouse.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digital_warehouse.product')),
            ],
        ),
    ]
