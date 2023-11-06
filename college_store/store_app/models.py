from django.db import models


# Create your models here.

class Department(models.Model):
    dept_name = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date",)
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.dept_name


class Course(models.Model):
    course_name = models.CharField(max_length=300)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, default=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date",)
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.course_name

