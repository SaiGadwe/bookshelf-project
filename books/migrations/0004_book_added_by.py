from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_book_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='added_by',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='books',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
