# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Companies(models.Model):
    company_id = models.IntegerField()
    day_price_change = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    market_cap = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    price_to_earnings_ratio = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    roe_percent = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    div_yield_percent = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    debt_to_equity = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    price_to_book = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    net_profit_margin = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    price_to_free_cash_flow = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    curr_date = models.DateTimeField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    class Meta:
        managed = True
        db_table = 'companies'
    def __unicode__(self):
        return str(self.company_id) + " " + str(self.curr_date)

class Company(models.Model):
    name = models.CharField(unique=True, max_length=70, blank=True)
    symbol = models.CharField(max_length=30, blank=True)
    id = models.IntegerField(primary_key=True)
    class Meta:
        managed = True
        db_table = 'company'
    def __unicode__(self):
        return self.name

class Companytosector(models.Model):
    id = models.IntegerField(primary_key=True)
    industry_id = models.IntegerField()
    company_id = models.IntegerField()
    class Meta:
        managed = True
        db_table = 'companyToSector'
    def __unicode__(self):
        return str(self.industry_id) + " " + str(self.company_id)

class Industries(models.Model):
    sector_number = models.IntegerField(blank=True, null=True)
    industry = models.IntegerField(blank=True, null=True)
    day_price_change = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    market_cap = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    price_to_earnings_ratio = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    roe_percent = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    div_yield_percent = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    debt_to_equity = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    price_to_book = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    net_profit_margin = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    price_to_free_cash_flow = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    curr_date = models.DateTimeField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    class Meta:
        managed = True
        db_table = 'industries'
    def __unicode__(self):
        return str(self.industry) + " " + str(self.curr_date)

class Industry(models.Model):
    name = models.CharField(max_length=50, blank=True)
    id = models.IntegerField(primary_key=True)
    sector_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'industry'
    def __unicode__(self):
        return self.name

class Quotes(models.Model):
    company_id = models.IntegerField(blank=True, null=True)
    quote_date = models.DateField(blank=True, null=True)
    open = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    high = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    low = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    close = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    adj = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    curr_date = models.DateTimeField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    class Meta:
        managed = True
        db_table = 'quotes'
    def __unicode__(self):
        return str(self.company_id) + " " + str(self.quote_date)

class Sector(models.Model):
    name = models.CharField(max_length=30, blank=True)
    id = models.IntegerField(primary_key=True)
    class Meta:
        managed = True
        db_table = 'sector'
    def __unicode__(self):
        return self.name

class Sectors(models.Model):
    sector = models.CharField(max_length=50, blank=True)
    day_price_change = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    market_cap = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    price_to_earnings_ratio = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    roe_percent = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    div_yield_percent = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    debt_to_equity = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    price_to_book = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    net_profit_margin = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    price_to_free_cash_flow = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    curr_date = models.DateTimeField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    class Meta:
        managed = True
        db_table = 'sectors'
    def __unicode__(self):
        return self.sector + " " + str(self.curr_date)

