from django.contrib import admin
from patient.models import Patient, Prescription, Record



class PrescriptionAdmin(admin.StackedInline):
	model = Prescription
	list_display = ['medicine','description','patient','updated_on','added_on',]
	extra = 1

class RecordAdmin(admin.TabularInline):
	model = Record
	fk_name = 'patient'
	extra = 1



class PatientAdmin(admin.ModelAdmin):
	model = Patient
	list_display = ['name','age','bed_no','symptoms','admission_date']
	fieldsets = ((None, {'fields': ('name','age','bed_no','symptoms')}), )
	inlines = [PrescriptionAdmin, RecordAdmin]

	def get_queryset(self, request):
		qs = super(PatientAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			self.list_display = ['name','age','bed_no','symptoms','doctor','admission_date']
			return qs
		else:
			return qs.filter(doctor = request.user)

	def save_model(self, request, obj, form, change):
		obj.doctor = request.user
		obj.save()



admin.site.register(Patient, PatientAdmin)