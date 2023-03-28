# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 14:36:23 2022

@author: eftal
"""

import time
import random
import string



cumleler10p = [
"Bir insan sevip de bir şey yapmadan duramaz.",
"Bana bir önyargı verin, dünyayı yerinden oynatayım.",
"İnsan kendini kime şikayet eder?",
"Kafan saman dolu olunca asla büyümezsin.",
"İnsan eninde sonunda her şeye alışacaktır."     
]


zn = random.choice(cumleler10p)
z = ""


for i in zn:
    if i not in string.punctuation:
        z += i
        
z = z.lower()


cumleler20p = [
"Suç, toplumsal düzenin bozukluklarına karşı bir protestodur.",
"Her erkek onlarla mutlu olur çünkü acı çekmek için yetiştirilmişler.",
"Gerçeklerden çok dosyayı kolayca kapatmakla ilgileniyor olsa gerekti.",
"Savaşçı balıkçılla düşüp kalkmaya cesaret eden şahini, tehlike bekler.",
"Yaşamak acı çekmektir ve hayatta kalmak acıda bir anlam bulmak demektir.",
]


an = random.choice(cumleler20p)
a = ""


for i in an:
    if i not in string.punctuation:
        a += i
        
a = a.lower()
        
    
cumleler40p = [
"Annem öldü, ben kaybolmuş bir çocuğum, mağazanın kasa bölümüne beni almak için artık kimse gelmeyecek.Terk edilmiş her çocuk mahvolacaktır.",
"Bir kez kendini bulmuş birinin bu dünyada kaybedecek hiçbir şeyi yoktur. Ve kendi içindeki insanı anlamış olan biri, bütün insanları anlar.",
"Herkes hukukçu olacak diye bir kaide yoktur. Bizim muslukçu da yetiştirmemiz gerekir. Bir muslukçu bazen bir hukukçudan fazla işe yarar.",
"Hiçbirşeyi protesto etmiyorduk, karşı çıkmıyorduk. 'Bana dokunmayan yılan bin yıl yaşasın!' diyor ama yılanın bize de dokunacağını hesap etmiyorduk.",
"İnsanoğlunun en büyük icadı dildir diyeceğim ama belki de dil insanoğlunun icadı değil, biz onun yönlendirdiği bir organizmayız."
]


bn = random.choice(cumleler40p)
b = ""


for j in bn:
    if j not in string.punctuation:
        b += j
        
b = b.lower()
        
puan = 0


print(f'Ekrana şu cümleyi 15 saniye içinde yazınız.\n {zn}')

baslandi0 = time.time()

print("Başla")
k = input(" ").lower() 


bitti0 = time.time()

gecen_sure0 =  bitti0 - baslandi0

if gecen_sure0 < 15 and z == k:
    puan = puan + 10
    print("Bu bölümü geçtiniz. 10 puan kazandınız. Devam etmek ister misiniz.")
    
    k = input()
    
    if k == "evet":
        print(f'Ekrana şu cümleyi 30 saniye içinde yazınız.\n {an}')
        
        baslandi1 = time.time()
    
        print("Başla")
        m = input(" ").lower() 
    
        bitti1 = time.time()
        gecen_sure1 =  bitti1 - baslandi1
    
        if gecen_sure1 < 30 and a == m:
            puan = puan + 20
            print("Bu bölümü geçtiniz. 20 puan kazandınız. Devam etmek ister misiniz.")
        
            k = input()
        
            if k == "evet":
                print(f'Ekrana şu cümleyi 50 saniye içinde yazınız. \n {bn}') 
            
                baslandi2 = time.time()
                print("Başla")
                n = input(" ").lower()
            
                bitti2 = time.time()
                gecen_sure2 =  bitti2 - baslandi2 
            
                if gecen_sure2 < 50 and b == n:
                    puan = puan + 40
                    print(f'Bu bölümü geçtiniz. 40 puan kazandınız. Puanınız {puan}')
                
            
                else:
                    print(f'Oyunu kaybettiniz.Puanınız  {puan}')
        
            else:
                print(f'Oyun bitti. {puan}')
    
        else:
            print(f'Bu bölümü kaybettiniz.Tekrar deneyiniz. Puanınız {puan}')         
    
    else:
        print(f'Oyun bitti. {puan}')    
    
else:
    print('Oyunu kaybettiniz.')
    
    
    
    

    
    
    

    


    

    
   
    

