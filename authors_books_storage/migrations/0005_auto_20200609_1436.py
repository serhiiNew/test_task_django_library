# Generated by Django 3.0.7 on 2020-06-09 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors_books_storage', '0004_remove_author_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='authors_books_storage.Author'),
        ),
    ]
