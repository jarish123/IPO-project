
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipo_app', '0002_ipo_logo_ipo_prospectus_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ipo',
            name='prospectus_pdf',
        ),
        migrations.AddField(
            model_name='ipo',
            name='cmp',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Current Market Price'),
        ),
        migrations.AddField(
            model_name='ipo',
            name='current_return',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='ipo',
            name='drhp_pdf',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/drhp/'),
        ),
        migrations.AddField(
            model_name='ipo',
            name='ipo_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='ipo',
            name='issue_size',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='ipo',
            name='issue_type',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='ipo',
            name='listing_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ipo',
            name='listing_gain',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='ipo',
            name='listing_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='ipo',
            name='price_band',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='ipo',
            name='rhp_pdf',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/rhp/'),
        ),
        migrations.AlterField(
            model_name='ipo',
            name='company_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='ipo',
            name='status',
            field=models.CharField(default='Upcoming', max_length=50),
        ),
    ]
