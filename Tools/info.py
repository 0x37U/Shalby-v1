import requests
import os

os.system("cls" or "clear")

print("""

██╗███╗░░██╗███████╗░█████╗░  ░░░░░░  ░██████╗░███████╗███╗░░██╗
██║████╗░██║██╔════╝██╔══██╗  ░░░░░░  ██╔════╝░██╔════╝████╗░██║
██║██╔██╗██║█████╗░░██║░░██║  █████╗  ██║░░██╗░█████╗░░██╔██╗██║
██║██║╚████║██╔══╝░░██║░░██║  ╚════╝  ██║░░╚██╗██╔══╝░░██║╚████║
██║██║░╚███║██║░░░░░╚█████╔╝  ░░░░░░  ╚██████╔╝███████╗██║░╚███║
╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░  ░░░░░░  ░╚═════╝░╚══════╝╚═╝░░╚══╝

""")
Url = "https://randomuser.me/api?results=1&gender=male&password=upper,lower,12&exc=register,picture,id&nat=US"

i = int(input("How Many Data You Want ? ").strip())
def Getinfo():

    global Url
    global i

    count = 0

    while 1:
        if i == 0:
            break
        count +=1
        with open(".\data.txt","a") as f:

            req = requests.get(Url).json()
            gender = req["results"][0]["gender"]
            frist = req["results"][0]["name"]['first']
            last = req["results"][0]["name"]['last']
            country = req["results"][0]["location"]["country"]
            city = req["results"][0]["location"]["city"]
            number = req["results"][0]["location"]["street"]["number"]
            street = req["results"][0]["location"]["street"]["name"]
            postcode = req["results"][0]["location"]["postcode"]

            print("Gender : "+gender.capitalize())
            print("Name : "+frist,last)
            print(f"Email : {frist+last}@yahoo.com".lower())
            print(f"Country : {country}\nCity : {city}\nStreet : {number} {street}\nPostalcode : {postcode}")
            print("="*25)

            f.write(f"Gender : {gender.capitalize()}\nName : {frist} {last}\nEmail : {frist.lower()}{last.lower()}@yahoo.com\nCountry : {country}\nCity : {city}\nStreet : {number} {street}\nPostalcode : {postcode}\n================\n")
    
        if count == i:
            print("<======= Check \"Data.txt\" File =======>")
            break
Getinfo()