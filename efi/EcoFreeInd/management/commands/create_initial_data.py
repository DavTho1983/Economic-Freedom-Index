import pandas as pd
import numpy as np


from django.core.management import BaseCommand


from EcoFreeInd.models import Freedom
from django.conf import settings
class PandasOperations():

    def __init__(self):
        self.csv_path = settings.EFI_DATA + '\economic_freedom_index.csv'

    def change_ppl_to_millions(self, row):
        row = row.strip()
        if " " in row:
            row = float(''.join(row.split(" ")[0])) / 1000000
        else:
            row = float(row)
        return np.around(row, decimals=2)

    def sanitize_data(self):
        efi = pd.read_csv(self.csv_path, encoding='latin-1')

        efi.CountryID = efi.CountryID.astype(float)
        efi['Region'] = efi.Region.astype('category')
        efi.columns = efi.columns.str.replace('%', 'pct').str.strip().str.replace(' ', '_').str.lower().str.replace('(', '').str.replace(')', '').str.replace(r"[\"\',]", '')
        efi.gdp_per_capita_ppp = efi.gdp_per_capita_ppp.replace('[\$,]', '', regex=True).str.split(' ').str[0].astype(float)
        efi = efi.rename(index=str, columns={'gdp_per_capita_ppp': 'gdp_per_capita_ppp_USD'})
        efi.population_millions = efi.population_millions.str.replace(',', '').apply(self.change_ppl_to_millions)
        efi.unemployment_pct = efi.unemployment_pct.str.split(' ').str[0].astype(float)
        efi.fdi_inflow_millions = efi.fdi_inflow_millions.str.replace(',', '').astype(float)
        efi.gdp_billions_ppp = efi.gdp_billions_ppp.replace('[\$,]', '', regex=True).str.split(' ').str[0].astype(float).fillna(0)

        num_cols = list(efi.select_dtypes(include='number'))
        str_cols = list(efi.select_dtypes(exclude=['number', 'category']))
        efi[num_cols] = efi[num_cols].fillna(0)

        efi[str_cols] = efi[str_cols].fillna('Not available')

        return efi

class Command(BaseCommand,Freedom):

    def __init__(self):
        self.pandas_operations = PandasOperations()

    def execute(self, *args, **options):
        efi = self.pandas_operations.sanitize_data()
        for country in efi.iterrows():
            country = Freedom.objects.create(
                countryid = country[1].countryid,
                country_name = country[1].country_name,
                webname = country[1].webname,
                region = country[1].region,
                world_rank = country[1].world_rank,
                region_rank = country[1].region_rank,
                twenty_nineteen_score = country[1]['2019_score'],
                property_rights = country[1].property_rights,
                judical_effectiveness = country[1].judical_effectiveness,
                government_integrity = country[1].government_integrity,
                tax_burden = country[1].tax_burden,
                govt_spending = country[1].govt_spending,
                fiscal_health = country[1].fiscal_health,
                business_freedom = country[1].business_freedom,
                labor_freedom = country[1].labor_freedom,
                monetary_freedom = country[1].monetary_freedom,
                trade_freedom = country[1].trade_freedom,
                investment_freedom = country[1].investment_freedom,
                financial_freedom = country[1].financial_freedom,
                tariff_rate_pct = country[1].tariff_rate_pct,
                income_tax_rate_pct = country[1].income_tax_rate_pct,
                corporate_tax_rate_pct = country[1].corporate_tax_rate_pct,
                tax_burden_pct_of_gdp = country[1].tax_burden_pct_of_gdp,
                govt_expenditure_pct_of_gdp = country[1].govt_expenditure_pct_of_gdp,
                country = country[1].country,
                population_millions = country[1].population_millions,
                gdp_billions_ppp = country[1].gdp_billions_ppp,
                gdp_growth_rate_pct = country[1].gdp_growth_rate_pct,
                five_year_gdp_growth_rate_pct = country[1]['5_year_gdp_growth_rate_pct'],
                gdp_per_capita_ppp_USD = country[1].gdp_per_capita_ppp_USD,
                unemployment_pct = country[1].unemployment_pct,
                inflation_pct = country[1].inflation_pct,
                fdi_inflow_millions = country[1].fdi_inflow_millions,
                public_debt_pct_of_gdp = country[1].public_debt_pct_of_gdp,
            )
        print("SUCCESS")
