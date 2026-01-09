from django.db import models

class Departament(models.Model):
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
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    department = models.ForeignKey(Departament, on_delete=models.CASCADE, related_name='positions')

    def __str__(self):
        return f'{self.title} ({self.get_level_display()})'

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hire_date = models.DateField()
    departament = models.ForeignKey(Departament, on_delete=models.SET_NULL, null=True, related_name='employees')
    positions = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, related_name='employees')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


