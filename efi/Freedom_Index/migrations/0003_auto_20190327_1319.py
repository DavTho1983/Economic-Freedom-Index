# Generated by Django 2.1.7 on 2019-03-27 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Freedom_Index', '0002_auto_20190327_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freedom',
            name='business_freedom',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='corporate_tax_rate_pct',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='fdi_inflow_millions',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='financial_freedom',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='fiscal_health',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='five_year_gdp_growth_rate_pct',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='gdp_billions_ppp',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='gdp_growth_rate_pct',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='gdp_per_capita_ppp_USD',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='government_integrity',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='govt_expenditure_pct_of_gdp',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='govt_spending',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='income_tax_rate_pct',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='inflation_pct',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='investment_freedom',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='judical_effectiveness',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='labor_freedom',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='monetary_freedom',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='property_rights',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='public_debt_pct_of_gdp',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='region_rank',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='tariff_rate_pct',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='tax_burden',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='tax_burden_pct_of_gdp',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='trade_freedom',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='twenty_nineteen_score',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='unemployment_pct',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='freedom',
            name='world_rank',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
