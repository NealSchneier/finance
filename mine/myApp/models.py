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

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

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
        managed = False
        db_table = 'companies'

class Company(models.Model):
    name = models.CharField(unique=True, max_length=70, blank=True)
    symbol = models.CharField(max_length=30, blank=True)
    id = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'company'

class Companytosector(models.Model):
    id = models.IntegerField(primary_key=True)
    industry_id = models.IntegerField()
    company_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'companyToSector'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

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
        managed = False
        db_table = 'industries'

class Industry(models.Model):
    name = models.CharField(max_length=50, blank=True)
    id = models.IntegerField(primary_key=True)
    sector_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'industry'

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
        managed = False
        db_table = 'quotes'

class Sector(models.Model):
    name = models.CharField(max_length=30, blank=True)
    id = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'sector'

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
        managed = False
        db_table = 'sectors'

