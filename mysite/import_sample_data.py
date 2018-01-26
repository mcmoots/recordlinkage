# Run this from the Django shell

import csv
from datetime import datetime

from matcher.models import PatientRecord

with open('/Users/mbrum1/Projects/recordlinkage/sampledata/sch.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        record = PatientRecord()
        record.patient_mrn_id = row['PATIENT_MRN_ID']
        record.patient_id = row['PATIENT_ID']
        record.patient_first_name = row['PATIENT_FIRST_NAME']
        record.patient_middle_name = row['PATIENT_MIDDLE_NAME']
        record.patient_full_name = row['PATIENT_FULL_NAME']
        try:
            record.patient_dob = datetime.strptime(
                            row['PATIENT_DOB'], 
                            '%Y-%m-%d %H:%M:%S.%f').date()
        except:
            record.patient_dob = None
        try:
            record.patient_dod = datetime.strptime(
                            row['PATIENT_DOD'],
                            '%Y-%m-%d %H:%M:%S.%f').date()
        except:
            record.patient_dod = None
        record.patient_sex = row['PATIENT_SEX']
        record.patient_address_line_1 = row['PATIENT_ADDRESS_LINE_1']
        record.patient_address_line_2 = row['PATIENT_ADDRESS_LINE_2']
        record.patient_address_city = row['PATIENT_ADDRESS_CITY']
        record.patient_address_state = row['PATIENT_ADDRESS_STATE']
        record.patient_address_country = row['PATIENT_ADDRESS_COUNTRY']
        record.patient_address_zip = row['PATIENT_ADDRESS_ZIP']
        record.record_source = 'Fake Test Dataset 1'
        record.save()
