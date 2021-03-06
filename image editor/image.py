from PIL import Image, ImageEnhance, ImageOps,ImageDraw,ImageFilter, ImageFont
import glob
from instapy import InstaPy
from instabot import Bot
import time
from random import randint
import os,sys
path="path to where the scraped memes are"
path2="path to where the results will go"

def deepfry(image, phrases,counter):

    imagee=Image.open(path+'/'+image)#create image object resize and set as thumbnail so all images work
    img=imagee.copy()
    img = img.convert('RGB')
    size=(226,223)
    img.thumbnail(size,Image.ANTIALIAS)
    
    width, height = img.width, img.height
    img = img.resize((int(width ** .75), int(height ** .75)), resample=Image.LANCZOS)#scuff the quality of the image
    img = img.resize((int(width ** .88), int(height ** .88)), resample=Image.BILINEAR)
    img = img.resize((int(width ** .9), int(height ** .9)), resample=Image.BICUBIC)
    img = img.resize((width, height), resample=Image.BICUBIC)
    img = ImageOps.posterize(img, 4)
 
    img = ImageEnhance.Brightness(img).enhance(1.1)#make it brighter
    img = ImageEnhance.Color(img).enhance(1.5)#make it more saturated

    
    img = ImageEnhance.Sharpness(img).enhance(12.0)#sharpen it
    temp=ImageEnhance.Color(img)
    img2=temp.enhance(3)
    
    draw=ImageDraw.Draw(img2)
    value=randint(-1,len(phrases)-1)#get a random number within the length of the array of phrases
    
    
    print(value)
   
    if(len(phrases[value])>11):#change font size depending on how big the phrase is then draw it on
        font=ImageFont.truetype("impact.ttf",25)
        draw.text((0,0),phrases[value],(255,255,255),font=font)
    else:
         font=ImageFont.truetype("impact.ttf",40)
         if(' ' in phrases[value]):
            draw.text((20,0),phrases[value],(255,255,255),font=font)
         else:
            draw.text((70,0),phrases[value],(255,255,255),font=font)
             
         

    img2.save(path2+'/'+str(counter)+'.png','PNG')#save it to the results folder

#list of different meme phrases to put on the image
phrase=["me when the","top text","bottom text","finally","do be kinda vibin doe","homies coming through","yankee wiv no brim","baked beans brekky","rise and grind","lets get bread","funny text","gamers are opressed","so truuuuue","yes"]

i=0

#set up instagram bot
arrr=os.listdir(path2)
bot = Bot()
bot.login(username="instagramusername", password="password")
time.sleep(15)

#file = open(path2+'/'+'0.png', 'r')
for item in arrr: #post every photo in the result folder sleep 20 secs between so instagram doesnt block requests
    value=randint(-1,len(phrases)-1)
    bot.upload_photo(path2+'/'+item, caption=phrase[value])
    time.sleep(20)
#deepfry('memes25.jpg', phrase,1)
