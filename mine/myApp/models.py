# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
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
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
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
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = 'auth_user_user_permissions'

class Companies(models.Model):
    name = models.CharField(max_length=50, blank=True)
    day_price_change = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    market_cap = models.CharField(max_length=30, blank=True)
    price_to_earnings_ratio = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    roe_percent = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    div_yield_percent = models.CharField(max_length=30, blank=True)
    debt_to_equity = models.CharField(max_length=30, blank=True)
    price_to_book = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    net_profit_margin = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    price_to_free_cash_flow = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    curr_date = models.DateTimeField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'companies'

class Company(models.Model):
    name = models.CharField(max_length=30, blank=True)
    symbol = models.CharField(max_length=30, blank=True)
    id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'company'

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
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'django_site'

class Industry(models.Model):
    sector_number = models.IntegerField(blank=True, null=True)
    industry = models.CharField(max_length=50, blank=True)
    day_price_change = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    market_cap = models.CharField(max_length=30, blank=True)
    price_to_earnings_ratio = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    roe_percent = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    div_yield_percent = models.CharField(max_length=30, blank=True)
    debt_to_equity = models.CharField(max_length=30, blank=True)
    price_to_book = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    net_profit_margin = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    price_to_free_cash_flow = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    curr_date = models.DateTimeField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'industry'

class Quotes(models.Model):
    latest_value = models.CharField(max_length=30, blank=True)
    previous_close = models.CharField(max_length=30, blank=True)
    after_hours_change_realtime = models.CharField(max_length=30, blank=True)
    annualized_gain = models.CharField(max_length=30, blank=True)
    ask = models.CharField(max_length=30, blank=True)
    ask_realtime = models.CharField(db_column='ask_Realtime', max_length=30, blank=True) # Field name made lowercase.
    ask_size = models.CharField(max_length=30, blank=True)
    average_daily_value = models.CharField(max_length=30, blank=True)
    bid = models.CharField(max_length=30, blank=True)
    bid_realtime = models.CharField(max_length=30, blank=True)
    bid_size = models.CharField(max_length=30, blank=True)
    book_value_per_share = models.CharField(max_length=30, blank=True)
    changequote = models.CharField(db_column='changeQuote', max_length=30, blank=True) # Field name made lowercase.
    change_in_percent = models.CharField(max_length=30, blank=True)
    changefromfiftydaymovingaverage = models.CharField(db_column='changeFromFiftydayMovingAverage', max_length=30, blank=True) # Field name made lowercase.
    changefromtwohundreddaymovingaverage = models.CharField(db_column='changeFromTwoHundredDayMovingAverage', max_length=30, blank=True) # Field name made lowercase.
    changefromyearhigh = models.CharField(db_column='changeFromYearHigh', max_length=30, blank=True) # Field name made lowercase.
    changefromyearlow = models.CharField(db_column='changeFromYearlow', max_length=30, blank=True) # Field name made lowercase.
    changeinpercent = models.CharField(db_column='changeInPercent', max_length=30, blank=True) # Field name made lowercase.
    changeinpercentrealtime = models.CharField(db_column='changeInPercentRealtime', max_length=30, blank=True) # Field name made lowercase.
    changerealtime = models.CharField(db_column='changeRealtime', max_length=30, blank=True) # Field name made lowercase.
    commission = models.CharField(max_length=30, blank=True)
    currency = models.CharField(max_length=30, blank=True)
    dayshigh = models.CharField(db_column='daysHigh', max_length=30, blank=True) # Field name made lowercase.
    dayslow = models.CharField(db_column='daysLow', max_length=30, blank=True) # Field name made lowercase.
    daysrange = models.CharField(db_column='daysRange', max_length=30, blank=True) # Field name made lowercase.
    daysrangerealtime = models.CharField(db_column='daysRangeRealtime', max_length=30, blank=True) # Field name made lowercase.
    daysvaluechange = models.CharField(db_column='DaysValueChange', max_length=30, blank=True) # Field name made lowercase.
    daysvaluechagerealtime = models.CharField(db_column='DaysValueChageRealtime', max_length=30, blank=True) # Field name made lowercase.
    dividendpaydate = models.CharField(max_length=30, blank=True)
    trailingannualdividendyield = models.CharField(max_length=30, blank=True)
    trailingannualdividendyieldinprecent = models.CharField(db_column='trailingannualdividendyieldInPrecent', max_length=30, blank=True) # Field name made lowercase.
    dilutedeps = models.CharField(db_column='dilutedEPS', max_length=30, blank=True) # Field name made lowercase.
    ebitda = models.CharField(db_column='EBITDA', max_length=30, blank=True) # Field name made lowercase.
    epsestimatecurrentyear = models.CharField(db_column='EPSEstimateCurrentYear', max_length=30, blank=True) # Field name made lowercase.
    epsestimatenextquarter = models.CharField(db_column='EPSEstimateNextQuarter', max_length=30, blank=True) # Field name made lowercase.
    epsestimatenextyear = models.CharField(db_column='EPSEstimateNextYear', max_length=30, blank=True) # Field name made lowercase.
    exdivedendnextyear = models.CharField(db_column='ExDivedendNextYear', max_length=30, blank=True) # Field name made lowercase.
    exdividentdate = models.CharField(db_column='exDividentDate', max_length=30, blank=True) # Field name made lowercase.
    fiftydaymovingaverage = models.CharField(max_length=30, blank=True)
    sharesfloat = models.CharField(max_length=30, blank=True)
    highlimit = models.CharField(max_length=30, blank=True)
    holdingsgain = models.CharField(max_length=30, blank=True)
    holdingsgainpercent = models.CharField(max_length=30, blank=True)
    holdingsgainpercentrealtime = models.CharField(max_length=30, blank=True)
    holdingsgainrealtime = models.CharField(max_length=30, blank=True)
    holdingsvalue = models.CharField(max_length=30, blank=True)
    holdingsvaluerealtime = models.CharField(max_length=30, blank=True)
    lasttradedate = models.CharField(max_length=30, blank=True)
    lasttradepriceonly = models.CharField(max_length=30, blank=True)
    lasttraderealtimewithtime = models.CharField(max_length=30, blank=True)
    lasttradesize = models.CharField(max_length=30, blank=True)
    lasttradetime = models.CharField(max_length=30, blank=True)
    lasttradewithtime = models.CharField(max_length=30, blank=True)
    lowlimit = models.CharField(max_length=30, blank=True)
    marketcapitalization = models.CharField(max_length=30, blank=True)
    marketcaprealtime = models.CharField(max_length=30, blank=True)
    moreinfo = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=30, blank=True)
    notes = models.CharField(max_length=30, blank=True)
    oneyrtargetprice = models.CharField(max_length=30, blank=True)
    open = models.CharField(max_length=30, blank=True)
    orderbookrealtime = models.CharField(max_length=30, blank=True)
    pegratio = models.CharField(max_length=30, blank=True)
    peratio = models.CharField(max_length=30, blank=True)
    peratiorealtime = models.CharField(max_length=30, blank=True)
    percentchangefromfiftydaymovingaverage = models.CharField(max_length=30, blank=True)
    percentchangefromtwohundreddaymovingaverage = models.CharField(max_length=30, blank=True)
    changeinpercentfromyearhigh = models.CharField(max_length=30, blank=True)
    percentchangefromyearlow = models.CharField(max_length=30, blank=True)
    previousclose = models.CharField(max_length=30, blank=True)
    pricebook = models.CharField(max_length=30, blank=True)
    priceepsestimatecurrentyear = models.CharField(max_length=30, blank=True)
    priceepsestimatenextyear = models.CharField(max_length=30, blank=True)
    pricepaid = models.CharField(max_length=30, blank=True)
    pricesales = models.CharField(max_length=30, blank=True)
    revenue = models.CharField(max_length=30, blank=True)
    sharesowned = models.CharField(max_length=30, blank=True)
    sharesoutstanding = models.CharField(max_length=30, blank=True)
    shortratio = models.CharField(max_length=30, blank=True)
    stockexchange = models.CharField(max_length=30, blank=True)
    symbol = models.CharField(max_length=30, blank=True)
    tickertrend = models.CharField(max_length=30, blank=True)
    tradedate = models.CharField(max_length=30, blank=True)
    twohundredaymovingaverage = models.CharField(max_length=30, blank=True)
    volume = models.CharField(max_length=30, blank=True)
    yearhigh = models.CharField(max_length=30, blank=True)
    yearlow = models.CharField(max_length=30, blank=True)
    yearrange = models.CharField(max_length=30, blank=True)
    curr_date = models.DateTimeField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'quotes'

class Sector(models.Model):
    sector = models.CharField(max_length=50, blank=True)
    day_price_change = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    market_cap = models.CharField(max_length=30, blank=True)
    price_to_earnings_ratio = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    roe_percent = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    div_yield_percent = models.CharField(max_length=30, blank=True)
    debt_to_equity = models.CharField(max_length=30, blank=True)
    price_to_book = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    net_profit_margin = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    price_to_free_cash_flow = models.DecimalField(max_digits=30, decimal_places=3, blank=True, null=True)
    curr_date = models.DateTimeField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'sector'



