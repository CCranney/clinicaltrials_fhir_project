from pytrials.client import ClinicalTrials
import pandas as pd

ct = ClinicalTrials()

def print_dict(d, levelMark):
    for key,value in d.items():
        print(levelMark + key)
        if type(value) == type(d): print_dict(value, '---'+levelMark)

def search_parameter_addition(additions, category, constant=None, sep = ' OR '):
    search = []
    for addition in additions:
        search.append(addition)
    if constant: search += constant
    search = sep.join(search)
    search += ' [' + category + ']'
    return search

def advanced_search(args):
    search = []
    for key,val in args.items():
        if key == 'OVERALL STATUS':
            search.append(search_parameter_addition(val, key, constant = ['NOT completed','NOT active'], sep = ' AND '))
        elif key == 'GENDER':
            search.append(search_parameter_addition(val, key, constant = ['All']))
        elif key == 'MINIMUMAGE':
            search.append(f'AREA[MinimumAge]RANGE[{val},MAX]')
        elif key == 'MAXIMUMAGE':
            search.append(f'AREA[MaximumAge]RANGE[MIN,{val}]')
        else:
            search.append(search_parameter_addition(val, key))
    return ' '.join(search)

def main():
    args = {
        'CONDITION': ['breast cancer'],
        'HEALTHYVOLUNTEER': ['Yes'],
        'OVERALL STATUS': ['recruiting'],
        'GENDER': ['Female'],
        'MINIMUMAGE': 18,
        #'MAXIMUMAGE': 60,
    }
    search = advanced_search(args)
    print(search)

    fields = ct.get_study_fields(
        search_expr=search,
        fields=["EligibilityCriteria"],
        fmt="csv",
        max_studies=1000,
    )
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    temp = pd.DataFrame.from_records(fields[1:], columns=fields[0])

    for index, row in temp.iterrows():
        print(row['EligibilityCriteria'])




if __name__ == '__main__':
    main()
