import requests
from datetime import datetime
from bs4 import BeautifulSoup
import smtplib

fin = ''
fullname = 'LU VINH THINH'
passportNo = ''
applicationNo = ''

email = 'luvinhthinh.mono@gmail.com'
pw = ''

def sendEmail(src, des, msg):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(src, pw)
    body = '\r\n'.join(['To: %s' % des,
                    'From: %s' % src,
                    'Subject: MOM EP Status',
                    '', msg]);
    try :
        server.sendmail(src, des, body)
        print('email sent')
    except Exception as ex:
        print('error sending email')
        print(ex)
    server.quit()

def sendRequest():
    url = 'https://eponline.mom.gov.sg/epol/PEPOLENQM008SubmitAction.do'
    params = {'dispatch':'', 'requesterNRICFIN':fin, 'requesterName': fullname, 'fin':'', 'forOptionValidation':'', 'forGroupOptionValidation':'', 'finApplDt':'', 'travelDocNo': passportNo, 'applNo': applicationNo}
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    r = requests.post(url, data=params, headers=headers)
    return r.text

def parseData(htmlText):
    data = {}
    soup = BeautifulSoup(htmlText, 'html.parser')
    #/html/body/table[3]/tbody/tr[2]/td[3]/form/table[6]/tbody/tr/td/table/tr
    interested_rows = soup.form.find_all('table')[6].table.find_all('tr')
    for row in interested_rows:
        tds = row.find_all('td')
        data[cleanText(tds[1].get_text())] = cleanText(tds[2].get_text())

    data['datetime'] = datetime.now().strftime('%d/%m/%Y %H:%M')
    return data

def cleanText(text):
    return text.strip().replace(u'\xa0', u'')

raw_data = sendRequest()
data = str(parseData(raw_data))
#print(data)
sendEmail(email, email, data)
