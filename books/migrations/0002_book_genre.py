from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(
                choices=[
                    ('fiction', 'Fiction'),
                    ('non_fiction', 'Non-Fiction'),
                    ('fantasy', 'Fantasy'),
                    ('sci_fi', 'Science Fiction'),
                    ('mystery', 'Mystery'),
                    ('biography', 'Biography'),
                    ('other', 'Other'),
                ],
                default='other',
                max_length=20,
            ),
        ),
    ]
