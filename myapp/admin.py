from django.contrib import admin
from myapp.models.course import Course, StudentCourse
from myapp.models.person import Person
from myapp.models.student import Student


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
    )


admin.site.register(Person, PersonAdmin)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "student_no", "name")


@admin.register(StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "course", "created_at")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "name", "professor")
