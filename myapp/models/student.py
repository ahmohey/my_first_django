from django.db import models


class Student(models.Model):
    class Meta:
        db_table = "student"

    GRADE_TYPE = (
        ("1", "1학년"),
        ("2", "2학년"),
        ("3", "3학년"),
        ("4", "4학년"),
        ("5", "5학년"),
    )

    student_no = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    grade = models.CharField(max_length=20, choices=GRADE_TYPE)
    department = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name
