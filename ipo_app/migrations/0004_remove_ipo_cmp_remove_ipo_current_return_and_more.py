
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipo_app', '0003_remove_ipo_prospectus_pdf_ipo_cmp_ipo_current_return_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ipo',
            name='cmp',
        ),
        migrations.RemoveField(
            model_name='ipo',
            name='current_return',
        ),
        migrations.RemoveField(
            model_name='ipo',
            name='listing_gain',
        ),
        migrations.AddField(
            model_name='ipo',
            name='current_market_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ipo',
            name='company_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ipo',
            name='drhp_pdf',
            field=models.FileField(blank=True, null=True, upload_to='docs/'),
        ),
        migrations.AlterField(
            model_name='ipo',
            name='ipo_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ipo',
            name='issue_size',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ipo',
            name='issue_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ipo',
            name='listing_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ipo',
            name='price_band',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ipo',
            name='rhp_pdf',
            field=models.FileField(blank=True, null=True, upload_to='docs/'),
        ),
        migrations.AlterField(
            model_name='ipo',
            name='status',
            field=models.CharField(choices=[('upcoming', 'Upcoming'), ('ongoing', 'Ongoing'), ('listed', 'Listed')], default='upcoming', max_length=20),
        ),
    ]
