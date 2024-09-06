from django.db import models
from datetime import datetime

# Create your models here.

class Masala(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    input_data = models.TextField(null=True, blank=True)
    output_data = models.TextField(null=True, blank=True)
    example_input = models.CharField(max_length=150)
    example_output = models.CharField(max_length=150)

    def __str__(self):
        return self.title

# class Tekshiruvchi(models.Model):
#     task = models.ForeignKey(Masala, on_delete=models.CASCADE)
#     code = models.TextField()
#     date = models.DateTimeField(auto_now_add=True, default=datetime.now())
#     result = models.CharField(max_length=50)


class Test_case(models.Model):
    task = models.ForeignKey(Masala, on_delete=models.CASCADE)
    example_input = models.CharField(max_length=150)
    example_output = models.CharField(max_length=150)



