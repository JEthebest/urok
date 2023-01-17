# Generated by Django 4.1.5 on 2023-01-12 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Qa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Вопрос')),
                ('answer', models.CharField(max_length=255, verbose_name='Ответ')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qa', to='kuai.category')),
            ],
            options={
                'verbose_name': 'Экзамен',
                'verbose_name_plural': 'Экзамены',
            },
        ),
    ]