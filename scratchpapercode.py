from pytrials.client import ClinicalTrials

ct = ClinicalTrials()

# Get 50 full studies related to Coronavirus and COVID in json format.
ct.get_full_studies(search_expr="Coronavirus+COVID", max_studies=50)

# Get the NCTId, Condition and Brief title fields from 500 studies related to Coronavirus and Covid, in csv format.
corona_fields = ct.get_study_fields(
    search_expr="Coronavirus+COVID",
    fields=["NCTId", "Condition", "BriefTitle"],
    max_studies=500,
    fmt="csv",
)

# Get the count of studies related to Coronavirus and COVID.
# ClinicalTrials limits API queries to 1000 records
# Count of studies may be useful to build loops when you want to retrieve more than 1000 records

print(ct.get_study_count(search_expr="Coronavirus+COVID"))

# Read the csv data in Pandas
import pandas as pd
pd.set_option('display.max_columns', None)
temp = pd.DataFrame.from_records(corona_fields[1:], columns=corona_fields[0])
print(temp.head(10))
