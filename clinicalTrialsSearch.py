from pytrials.client import ClinicalTrials
import re
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Try to replicate? https://clinicaltrials.gov/ct2/search/advanced?cond=&term=&cntry=&state=&city=&dist=

def search_for_possible_trials(conditions: list, male: bool, age: int):

    condition_expr = ''
    for i in range(len(conditions)-1): condition_expr += conditions[i] + ' OR '
    condition_expr += conditions[-1] + ' [CONDITION]'

    status_expr = 'NOT completed AND NOT active [OVERALL STATUS]'

    if male: gender_expr = 'male OR all [GENDER]'
    else: gender_expr = 'female OR all [GENDER]'

    search_expr = condition_expr + ' ' + status_expr + ' ' + gender_expr
    ct = ClinicalTrials()
    fields = ["NCTId", "HealthyVolunteers", "Gender", "MinimumAge", "MaximumAge", "EligibilityCriteria"]
    study_fields = ct.get_study_fields(
        search_expr="breast cancer [CONDITION]",
        fields=fields,
        fmt="csv",
        max_studies = 1000,
        )
    studies = pd.DataFrame.from_records(study_fields[1:], columns = ['Rank'] + fields)
    studies["MinimumAge"] = studies["MinimumAge"].apply(extract_age)
    studies["MaximumAge"] = studies["MaximumAge"].apply(extract_age)
    print(studies)
    studies.to_csv('studies_delete.csv',index=False)
    #for index, row in studies.iterrows():
    #    print(row["EligibilityCriteria"])

def extract_age(str_with_age):
    val = re.search(r"\b\d+", str_with_age)
    if val: return int(val.group())
    else: return ''

conditions = ['breast cancer']
search_for_possible_trials(conditions, False, 20)
