# Generated by Django 4.0.2 on 2022-02-09 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_card_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Print',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=250)),
                ('price', models.IntegerField(default=0)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='main_app.card')),
            ],
        ),
    ]