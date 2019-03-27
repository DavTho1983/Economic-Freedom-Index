# Generated by Django 2.1.7 on 2019-03-27 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Freedom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countryid', models.IntegerField()),
                ('country_name', models.CharField(max_length=50)),
                ('webname', models.CharField(max_length=50)),
                ('region', models.CharField(choices=[('Americas', 'Americas'), ('Asia-Pacific', 'Asia-Pacific'), ('Europe', 'Europe'), ('Middle East and North Africa', 'Middle East and North Africa'), ('Sub-Saharan Africa', 'Sub-Saharan Africa')], max_length=50)),
                ('world_rank', models.IntegerField()),
                ('region_rank', models.IntegerField()),
                ('twenty_nineteen_score', models.DecimalField(decimal_places=1, max_digits=3)),
                ('property_rights', models.DecimalField(decimal_places=1, max_digits=3)),
                ('judical_effectiveness', models.DecimalField(decimal_places=1, max_digits=3)),
                ('government_integrity', models.DecimalField(decimal_places=1, max_digits=3)),
                ('tax_burden', models.DecimalField(decimal_places=1, max_digits=3)),
                ('govt_spending', models.DecimalField(decimal_places=1, max_digits=3)),
                ('fiscal_health', models.DecimalField(decimal_places=1, max_digits=3)),
                ('business_freedom', models.DecimalField(decimal_places=1, max_digits=3)),
                ('labor_freedom', models.DecimalField(decimal_places=1, max_digits=3)),
                ('monetary_freedom', models.DecimalField(decimal_places=1, max_digits=3)),
                ('trade_freedom', models.DecimalField(decimal_places=1, max_digits=3)),
                ('investment_freedom', models.IntegerField()),
                ('financial_freedom', models.IntegerField()),
                ('tariff_rate_pct', models.DecimalField(decimal_places=1, max_digits=3)),
                ('income_tax_rate_pct', models.DecimalField(decimal_places=1, max_digits=3)),
                ('corporate_tax_rate_pct', models.DecimalField(decimal_places=1, max_digits=3)),
                ('tax_burden_pct_of_gdp', models.DecimalField(decimal_places=1, max_digits=3)),
                ('govt_expenditure_pct_of_gdp', models.DecimalField(decimal_places=1, max_digits=3)),
                ('country', models.CharField(max_length=50)),
                ('population_millions', models.DecimalField(decimal_places=2, max_digits=8)),
                ('gdp_billions_ppp', models.DecimalField(decimal_places=1, max_digits=3)),
                ('gdp_growth_rate_pct', models.DecimalField(decimal_places=1, max_digits=3)),
                ('five_year_gdp_growth_rate_pct', models.DecimalField(decimal_places=1, max_digits=3)),
                ('gdp_per_capita_ppp_USD', models.IntegerField()),
                ('unemployment_pct', models.DecimalField(decimal_places=1, max_digits=3)),
                ('inflation_pct', models.DecimalField(decimal_places=1, max_digits=3)),
                ('fdi_inflow_millions', models.DecimalField(decimal_places=1, max_digits=8)),
                ('public_debt_pct_of_gdp', models.DecimalField(decimal_places=1, max_digits=4)),
            ],
        ),
    ]