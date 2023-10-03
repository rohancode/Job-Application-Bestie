from django.contrib import admin
from .models import CoverLetter
from .models import Member
from .models import Job
from .models import UserConsent
from .models import Source
from .models import ReferenceProject

admin.site.register(CoverLetter)
admin.site.register(Member)
admin.site.register(Job)
admin.site.register(UserConsent)
admin.site.register(ReferenceProject)
