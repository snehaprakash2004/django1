from django.db import models

# Department model
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Employee model
class Employee(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    department = models.ForeignKey(Department,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.full_name
