import requests
import json
import smtplib
from email.mime.text import MIMEText


mail_host = 'smtp.qq.com'
mail_user = '1159753003@qq.com'
mail_pass = 'splzbbzzpmbtichf'
sender = '1159753003@qq.com'
receivers = ['1327344233@qq.com']
mail_msg = """
<p>野生鱼雷通知姬提醒您，您的沈工智校体温上报程序开始运行</p>
"""
message = MIMEText(mail_msg, 'html','utf-8')
message['Subject'] = '野生鱼雷通知姬'
message['From'] = '野生鱼雷通知姬'
message['To'] = receivers[0]

try:
    smtpObj = smtplib.SMTP_SSL(mail_host)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(
        sender,receivers,message.as_string())
    smtpObj.quit()
    print('success')
except smtplib.SMTPException as e:
    print('error',e) 



header1 = {
    'Charset': 'UTF-8',
    'Accept-Encoding':'gzip',
    'AppId': 'A6089765735696',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.4; 1107 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36',
    'AppKey': '3B1BEB93-ACE9-7A9C-6B28-49E8FA5C453C',
    'Connection': 'Keep-Alive',
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'sgzxapp.situ.edu.cn',
    'Content-Length': '111'

}

values1 ={
    'userid':'1911530019',
    'password':'',
    'systemtype':'android',
    'getuicid':'a5cb7f7524ceaf6258b9c9d01717015b'
}
requrl1 = "https://sgzxapp.situ.edu.cn/api/user/login"

response=requests.post(url=requrl1,data=values1,headers=header1)
print(response.text)
dict_str =json.loads(response.text)
TOKENID = (dict_str['data'][0]['accessTokenId'])
print (TOKENID)



mail_host = 'smtp.qq.com'
mail_user = '1159753003@qq.com'
mail_pass = 'splzbbzzpmbtichf'
sender = '1159753003@qq.com'
receivers = ['1327344233@qq.com']
mail_msg = """
<p>野生鱼雷通知姬提醒您，您的沈工智校登录成功</p>
"""
message = MIMEText(mail_msg, 'html','utf-8')
message['Subject'] = '野生鱼雷通知姬'
message['From'] = '野生鱼雷通知姬'
message['To'] = receivers[0]

try:
    smtpObj = smtplib.SMTP_SSL(mail_host)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(
        sender,receivers,message.as_string())
    smtpObj.quit()
    print('success')
except smtplib.SMTPException as e:
    print('error',e) 



header = {'AccessTokenId':TOKENID,'Accept':'*/*','AppId':'A6089765735696','AppKey':'3B1BEB93-ACE9-7A9C-6B28-49E8FA5C453C','User-Agent':'User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)','Charset':'UTF-8','Accept-Encoding':'gzip','Content-Type':'application/x-www-form-urlencoded','Host':'218.61.108.164:8111','Content-Length':'976'}
values ={
    "backschool_date":"2021-02-27",
    "dormitory":"暂无<&$*->暂无<&$*->暂无",
    "telephone":"13000000000",
    "home_address":"辽宁省<&$*->无<&$*->无<&$*->无<&$*->无<&$*->无<&$*->无",
    "radio_airway":"0",
    "radio_hospital":"0",
    "radio_liveortravelncp":"0",
    "radio_memberpatient":"0",
    "radio_stay":"0",
    "radio_touchncprole":"0",
    "radio_touchpatient":"0",
    "detail_hospital":"",
    "detail_liveortravelncp":"",
    "detail_memberpatient":"",
    "detail_touchncprole":"",
    "detail_touchpatient":"",
    "detailtraffic":"无",
    "duration_airway":"0",
    "fromaddr":" ",
    "remark":"无",
    "stayinfo":"",
    "backschooltraffic":"8",
    "predicArriveTime":"10",
    "lstHealth":"0",
    "temperature":"36.7",
    "healthstate":"0",
    "curaddress":"辽宁省<&$*->抚顺市",
    "outflag":"0",
    "out_reasion":"",
    "out_destination":"",
    "out_traffic":"",
    "out_traffic_detail":"",
    "fdy_record":"0"}
requrl = "http://218.61.108.164:8111/api/newStudent/reportNpcHealth"

response=requests.post(url=requrl,params=values,headers=header)

response.encoding ='utf-8'
print(response.text)
date_code = (dict_str['msg'])
print (date_code)

mail_host = 'smtp.qq.com'
mail_user = '1159753003@qq.com'
mail_pass = 'splzbbzzpmbtichf'
sender = '1159753003@qq.com'
receivers = ['2927330356@qq.com']
mail_msg = """
<p>这里是野生鱼雷通知姬，今天已经成功的为您打卡了一次沈工智校</p>
"""
message = MIMEText(mail_msg, 'html','utf-8')
message['Subject'] = '野生鱼雷通知姬'
message['From'] = '野生鱼雷通知姬'
message['To'] = receivers[0]

try:
    smtpObj = smtplib.SMTP_SSL(mail_host)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(
        sender,receivers,message.as_string())
    smtpObj.quit()
    print('success')
except smtplib.SMTPException as e:
    print('error',e) 



