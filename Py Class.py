# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:41:07 2024

@author: lenovo
"""

class Araba():
    marka = "Mercedes"
    model = "GLA"
    motorHacmi= 2.0
    yili = 2024
    renk = "Kırmızı"
    
araba1= Araba()


type(araba1)

print(araba1.marka and araba1.model)

dir(araba1)


###

class Personel():
    def __init__(self,isim,soyisim,sicil,no,maas,yetenekler):
        self.isim = isim
        self.soyisim= soyisim
        self.sicil=sicil
        self.no =no
        self.maas= maas
        self.yetenekler=yetenekler
        
    def BilgileriGetir(self):
        print("""   
              Çalışan Bilgileri : 
              İsim : {}
             Soyisim : {}
             Sicil  : {}
             No : {}
             Maas : {}
             Yetenekler : {}
             
              
              
              
              
              """.format(self.isim,self.soyisim,self.sicil,self.no,self.maas,self.yetenekler))

    def yetenekEkle(self,yeniYetenek):
          self.yetenekler.append(yeniYetenek)
          print("Yeni yetenek eklendi ")
          
    def zamYap(self, zamMiktarı):
        self.maas += zamMiktarı
        print("Zam Yapıldı")
        
personel1 = Personel("Önder", "Ünlü", 101, 52, 50000, ["Excel", "Python", "Java"])
personel1.yetenekEkle("C#")

personel1.BilgileriGetir()
personel1.yetenekler


#Inheritance

class Yonetici(Personel):
    
    def __init__(self,isim,soyisim,sicil,no,maas,yetenekler,kisiSayisi):
  #1.Yöntem   
        self.isim= isim
        self.soyisim=soyisim
        self.sicil=sicil
        self.no=no
        self.maas=maas
        self.yetenekler=yetenekler
        self.kisiSayisi=kisiSayisi
        
    def BilgileriGetir(self):
       print("""   
             Çalışan Bilgileri : 
             İsim : {}
            Soyisim : {}
            Sicil  : {}
            No : {}
            Maas : {}
            Yetenekler : {}
            Sorumlu olduğu kişi sayısı : {}
             
             
             
             
             """.format(self.isim,self.soyisim,self.sicil,self.no,self.maas,self.yetenekler,self.kisiSayisi))
        
y1 = Yonetici ("Önder", "Ünlü", 101, 52, 50000, ["Excel", "Python", "Java"],15)
        
y1.BilgileriGetir()


#kumanda

class kumanda():
    def __init__(self,tvDurumu="Kapat",tvSes=0,kanalListesi = ["TRT"],kanal="TRT"):
      self.tvDurumu= tvDurumu
      self.tvSes=tvSes
      self.kanalListesi=kanalListesi
      self.kanal=kanal
      
    def tvAc(self):
        if(self.tvDurumu=="Açık"):
            print("Tv  zaten Açık")
        else:
            print("Tv açıldı")
            self.tvDurumu="Açık"
            
    def tvKapat(self):
          if(self.tvDurumu=="Kapalı"):
              print("Tv  zaten Kapalı")
          else:
              print("Tv açıldı")
              self.tvDurumu="Kapalı"      
        
    def sesAyari(self):
        
        cevap=input("Sesi azalt '<' Sesi arttır '>' ")
        if(cevap == "<" ):
            if(self.tvSes != 0):
                self.tvSes -=1
                print("Ses : ",self.tvSes)
            else:
                print("Sessiz")
                
        elif(cevap == ">" ):
               if(self.tvSes != 30):
                   self.tvSes +=1
                   print("Ses : ",self.tvSes)
        else:
            print("Yükses ses sağlığa zararlıdır")
           
    def kanalEkle(self,yeniKanal):
        self.kanalListesi.append(yeniKanal)
        
    def __len__(self):
       return len(self.kanalListesi)
   
    def __str__(self):
         return "Tv Durumu : {}\n Tv Ses:{}\n Kanal Listesi : {}\n Kanal : {} ".format(self.tvDurumu,self.tvSes,self.kanalListesi,self.kanal)
     
        
kumanda = kumanda()

kumanda.kanalListesi
kumanda.kanal
kumanda.tvSes

print(""" 
      
1. Tv Aç
2. Tv Kapat
3. Ses Ayarları
4. Kanal Ekle
5. Kanal Sayısı Öğren
6. Tv Bilgileri
Çıkış:q
    
      
      
      
      """)
       
while(True):
    islem=input("İşlem Seçiniz : ")
    if(islem=="q"):
        print("Program Kapatılıyor")
        break
    elif (islem=="1"):
        kumanda.tvAc()
    elif (islem=="2"):
        kumanda.tvKapat()
    elif(islem=="3"):
        kumanda.sesAyari()
    elif(islem=="4"):
        yeniKanal=input("Yeni kanal :")
        kumanda.kanalEkle(yeniKanal)
    elif(islem=="5"):
        print("Kanal Sayısı : ",len(kumanda))
    elif(islem=="6"):
        print(kumanda)
    else:
        print("Geçersiz İşlem")
    
        
   
   


