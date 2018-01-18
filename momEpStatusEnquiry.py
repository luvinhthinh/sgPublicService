import requests

fin = ''
fullname = 'LU VINH THINH'
passportNo = ''
applicationNo = ''

url = 'https://eponline.mom.gov.sg/epol/PEPOLENQM008SubmitAction.do'
params = {'dispatch':'', 'requesterNRICFIN':fin, 'requesterName': fullname,
'fin':'', 'forOptionValidation':'', 'forGroupOptionValidation':'', 'finApplDt':'',
'travelDocNo': passportNo, 'applNo': applicationNo}
headers = {'content-type': 'application/x-www-form-urlencoded'}

r = requests.post(url, data=params, headers=headers)

print(r.text)
