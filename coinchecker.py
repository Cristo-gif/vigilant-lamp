from pycoingecko import CoinGeckoAPI
import smtplib
from email.message import EmailMessage


prices=[]
totals=[]
names=['ethereum','polkadot','cardano','uniswap','theta-token','stellar']#insert names of coins you hold
def get_coins():
    cg=CoinGeckoAPI()
    eth=cg.get_price(ids='ethereum', vs_currencies='aud')#assign the prices to a dictionary
    dot=cg.get_price(ids='polkadot', vs_currencies='aud')
    ada=cg.get_price(ids='cardano', vs_currencies='aud')
    uni=cg.get_price(ids='uniswap', vs_currencies='aud')
    theta=cg.get_price(ids='theta-token', vs_currencies='aud')
    xlm=cg.get_price(ids='stellar', vs_currencies='aud')
    coins=[eth,dot,ada,uni,theta,xlm]
    
    amount=[0.35795154,7.44745502,478.70032347,3.81679389,38.77728894,105.5763936]#insert amount of each coin

    counter=0
    for coin in coins:#loop through the coins and add their prices to an array
        
        prices.append(coin[names[counter]])
        counter=counter+1

    for i in range(len(coins)):
        totals.append(float(prices[i]["aud"])*amount[i]) #loop through coins again and add your holdings of that coin to totals
        

def send_email():
    message=""
    for i in range(len(names)):
        message=message+names[i]+"current price is "+str(prices[i]["aud"])+"\n"#add each coin to the email
             
    total=0
    for pric in totals:
        total=total+pric

    msg = EmailMessage()
    msg.set_content(message+"Your current total is {}".format(total))

# me == the sender's email address
# you == the recipient's email address
    msg['Subject'] = 'The contents of '
    msg['From'] = 'Me'
    msg['To'] = 'You'

# Send the message via our own SMTP server.
    s = smtplib.SMTP('smtp.gmail.com')
    s.starttls()
    s.login('email address that is sending the email','password')
    s.send_message(msg)
    s.quit()
    
get_coins()
send_email()
