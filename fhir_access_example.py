import requests

headers = {'Accept': 'application/fhir+json'}
print('enter')
r = requests.get('http://hapi.fhir.org/baseR4/metadata', headers=headers)
print('exit')
#print(r.status_code)
print(r.text)
