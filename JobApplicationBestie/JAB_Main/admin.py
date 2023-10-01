from django.contrib import admin
from .models import CoverLetter
from .models import Member
from .models import Job
from .models import UserConsent

admin.site.register(CoverLetter)
admin.site.register(Member)
admin.site.register(Job)
admin.site.register(UserConsent)
