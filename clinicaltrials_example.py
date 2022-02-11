from pytrials.client import ClinicalTrials

ct = ClinicalTrials()

def print_dict(d, levelMark):
    for key,value in d.items():
        print(levelMark + key)
        if type(value) == type(d): print_dict(value, '---'+levelMark)

print(ct.study_fields)
# Get 50 full studies related to Coronavirus and COVID in json format.
fields = ct.get_full_studies(search_expr="breast cancer [CONDITION] NOT completed AND NOT active [OVERALL STATUS] IA [EligibilityCriteria]", max_studies=100)
print_dict(fields['FullStudiesResponse']['FullStudies'][0], '--> ')
print(fields)

for study in fields['FullStudiesResponse']['FullStudies']:
    print(study['Study']['ProtocolSection']['EligibilityModule'].keys())

#'''
# Get the NCTId, Condition and Brief title fields from 500 studies related to Coronavirus and Covid, in csv format.
fields = ct.get_study_fields(
    search_expr="breast cancer [CONDITION]",
    fields=["EligibilityCriteria"],
    fmt="csv",
)
#'''
# Get the count of studies related to Coronavirus and COVID.
# ClinicalTrials limits API queries to 1000 records
# Count of studies may be useful to build loops when you want to retrieve more than 1000 records

# Read the csv data in Pandas
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
temp = pd.DataFrame.from_records(fields[1:], columns=fields[0])

for index, row in temp.iterrows():
    print(row['EligibilityCriteria'])
