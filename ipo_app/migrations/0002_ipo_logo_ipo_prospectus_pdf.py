
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipo',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logos/'),
        ),
        migrations.AddField(
            model_name='ipo',
            name='prospectus_pdf',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/'),
        ),
    ]
