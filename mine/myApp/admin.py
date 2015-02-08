from django.contrib import admin

# Register your models here.
from models import Company, Companies, Companytosector, Sector, Sectors, Industry, Industries, Quotes

admin.site.register(Company)
admin.site.register(Companies)
admin.site.register(Companytosector)
admin.site.register(Sector)
admin.site.register(Sectors)
admin.site.register(Industry)
admin.site.register(Industries)
admin.site.register(Quotes)
