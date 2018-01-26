from django.db import models

# Create your models here.

class PatientRecord(models.Model):
    patient_mrn_id = models.CharField(max_length=50)
    patient_id = models.CharField(max_length=50)
    patient_first_name = models.CharField(max_length=500)
    patient_middle_name = models.CharField(max_length=500)
    patient_full_name = models.CharField(max_length=1000)
    patient_dob = models.DateField(null=True)
    patient_dod = models.DateField(null=True)
    patient_sex = models.CharField(max_length=50)
    patient_address_line_1 = models.CharField(max_length=500)
    patient_address_line_2 = models.CharField(max_length=500)
    patient_address_city = models.CharField(max_length=500)
    patient_address_state = models.CharField(max_length=500)
    patient_address_country = models.CharField(max_length=500)
    patient_address_zip = models.CharField(max_length=500)
    record_source = models.CharField(max_length=50)


class RecordMatch(models.Model):
    record1 = models.ForeignKey(PatientRecord,
            related_name='r1',
            on_delete=models.CASCADE)
    record2 = models.ForeignKey(PatientRecord, 
            related_name='r2',
            on_delete=models.CASCADE)
    score = models.DecimalField(
            max_digits=10
            , decimal_places=3)
    REVIEW_STATE_CHOICES = (
            ('UNREVIEWED', 'Not Reviewed'),
            ('ACCEPTED', 'Match accepted but not fixed'),
            ('FIXED', 'Match accepted and fixed'),
            ('REJECTED', 'Match rejected'),
        )
    review_state = models.CharField(
            max_length=12, 
            choices=REVIEW_STATE_CHOICES,
            default='UNREVIEWED',
            )



