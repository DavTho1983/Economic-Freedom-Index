from django.db import models

# ['countryid', 'country_name', 'webname', 'region', 'world_rank',
#        'region_rank', '2019_score', 'property_rights', 'judical_effectiveness',
#        'government_integrity', 'tax_burden', 'govt_spending', 'fiscal_health',
#        'business_freedom', 'labor_freedom', 'monetary_freedom',
#        'trade_freedom', 'investment_freedom', 'financial_freedom',
#        'tariff_rate_pct', 'income_tax_rate_pct', 'corporate_tax_rate_pct',
#        'tax_burden_pct_of_gdp', 'govt_expenditure_pct_of_gdp', 'country',
#        'population_millions', 'gdp_billions_ppp', 'gdp_growth_rate_pct',
#        '5_year_gdp_growth_rate_pct', 'gdp_per_capita_ppp_USD',
#        'unemployment_pct', 'inflation_pct', 'fdi_inflow_millions',
       # 'public_debt_pct_of_gdp']

class Freedom(models.Model):

    REGIONS = (
        ('Americas', 'Americas'),
        ('Asia-Pacific', 'Asia-Pacific'),
        ('Europe', 'Europe'),
        ('Middle East and North Africa', 'Middle East and North Africa'),
        ('Sub-Saharan Africa', 'Sub-Saharan Africa'),
    )

    countryid = models.DecimalField(max_digits=7, decimal_places=0)
    country_name = models.CharField(max_length=50)
    webname = models.CharField(max_length=50)
    region = models.CharField(max_length=50, choices=REGIONS)
    world_rank = models.DecimalField(max_digits=8, decimal_places=2)
    region_rank = models.DecimalField(max_digits=8, decimal_places=2)
    twenty_nineteen_score = models.DecimalField(max_digits=8, decimal_places=2)
    property_rights = models.DecimalField(max_digits=8, decimal_places=2)
    judical_effectiveness = models.DecimalField(max_digits=8, decimal_places=2)
    government_integrity = models.DecimalField(max_digits=8, decimal_places=2)
    tax_burden = models.DecimalField(max_digits=8, decimal_places=2)
    govt_spending = models.DecimalField(max_digits=8, decimal_places=2)
    fiscal_health = models.DecimalField(max_digits=8, decimal_places=2)
    business_freedom = models.DecimalField(max_digits=8, decimal_places=2)
    labor_freedom = models.DecimalField(max_digits=8, decimal_places=2)
    monetary_freedom = models.DecimalField(max_digits=8, decimal_places=2)
    trade_freedom = models.DecimalField(max_digits=8, decimal_places=2)
    investment_freedom = models.DecimalField(max_digits=8, decimal_places=2)
    financial_freedom = models.DecimalField(max_digits=8, decimal_places=2)
    tariff_rate_pct = models.DecimalField(max_digits=8, decimal_places=2)
    income_tax_rate_pct = models.DecimalField(max_digits=8, decimal_places=2)
    corporate_tax_rate_pct = models.DecimalField(max_digits=8, decimal_places=2)
    tax_burden_pct_of_gdp = models.DecimalField(max_digits=8, decimal_places=2)
    govt_expenditure_pct_of_gdp = models.DecimalField(max_digits=8, decimal_places=2)
    country = models.CharField(max_length=50)
    population_millions = models.DecimalField(max_digits=8, decimal_places=2)
    gdp_billions_ppp = models.DecimalField(max_digits=8, decimal_places=2)
    gdp_growth_rate_pct = models.DecimalField(max_digits=8, decimal_places=2)
    five_year_gdp_growth_rate_pct = models.DecimalField(max_digits=8, decimal_places=2)
    gdp_per_capita_ppp_USD = models.DecimalField(max_digits=8, decimal_places=2)
    unemployment_pct = models.DecimalField(max_digits=8, decimal_places=2)
    inflation_pct = models.DecimalField(max_digits=8, decimal_places=2)
    fdi_inflow_millions = models.DecimalField(max_digits=8, decimal_places=2)
    public_debt_pct_of_gdp = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.webname
