from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
	name = models.CharField(blank=True, max_length=255)
	age = models.CharField(blank=True, max_length=255, null=True)
	bed_no = models.CharField(blank=True, max_length=255, null=True)
	symptoms = models.TextField(blank=True, null=True)
	doctor = models.ForeignKey(User, on_delete=models.CASCADE)
	admission_date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name


class Prescription(models.Model):
	medicine = models.CharField(blank=True, max_length=255)
	description = models.CharField(blank=True, max_length=255, null=True)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	updated_on = models.DateTimeField(auto_now_add=True)
	added_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.medicine

class Record(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
	given_on = models.DateTimeField(blank=True, null=True)
