# Generated by Django 4.2.2 on 2023-07-04 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_address_zip'),
    ]

    operations = [
        migrations.RunSQL("""
        INSERT INTO store_collection (title)
        VALUES ('collection2')
        """,""" 
        DELETE FROM store_collection
        WHERE title='collection2'
        """)
    ]
