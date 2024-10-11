from django.contrib import admin

# Register your models here.
from .models import Person, Student, Enrollment,Course

admin.site.register(Person)
admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(Course)
