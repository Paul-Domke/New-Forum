from django.contrib import admin
from .models import FAQ, Rule, HoursOfOp, HoursOpen

admin.site.register(FAQ)
admin.site.register(Rule)
admin.site.register(HoursOpen)
admin.site.register(HoursOfOp)

