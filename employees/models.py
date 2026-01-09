from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Position(models.Model):
    LEVEL_CHOICES = [
        ('JR', 'Junior'),
        ('PL', 'Pleno'),
        ('SR', 'Senior'),
    ]
    title = models.CharField(max_length=100)
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES, default='JR')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='positions')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.get_level_display()}'

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hire_date = models.DateField(verbose_name="Data de contratação")
    departament = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='employees')
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, related_name='employees')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


