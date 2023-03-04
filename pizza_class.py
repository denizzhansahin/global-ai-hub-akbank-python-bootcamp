#Kütüphane tanımlama
import csv
import datetime

from fpdf import FPDF
import pandas as pd

#SUPER CLASSES

#Dekarasyon superclass
class Dekorasyon():
  def __init__(self,fiyat,aciklama):
    self.fiyat = fiyat
    self.aciklama = aciklama

  def bilgi_fiyat(self):
    return "Fiyat :" + " " + str(self.fiyat)
  
  def bilgi_aciklama(self):
    return "Açıklama :" + " " + str(self.aciklama)


#pizza superclass
class pizza(Dekorasyon):
  def __init__(self,isim,fiyat,aciklama,sos_tur):
    super().__init__(fiyat,aciklama)
    self.isim = isim
    self.sos_tur = sos_tur
    
    if self.sos_tur == "Zeytin":
      self.fiyat += Zeytin_sos.fiyat
    elif self.sos_tur ==  "Mantar":
      self.fiyat += Mantar_sos.fiyat
    elif self.sos_tur ==  "Keçi Peyniri":
      self.fiyat += Keci_Peynir_sos.fiyat
    elif self.sos_tur ==  "Et":
      self.fiyat += Et_sos.fiyat
    elif self.sos_tur ==  "Soğan":
      self.fiyat += Sogan_sos.fiyat
    elif self.sos_tur ==  "Mısır":
      self.fiyat += Misir_sos.fiyat

#sos superclass
class sos(Dekorasyon):
  def __init__(self,isim,fiyat,aciklama):
    super().__init__(fiyat,aciklama)
    self.isim = isim


#Pizza Alt Classları
class Turk_pizza(pizza):
  def __init__(self,isim,fiyat,aciklama,sos_tur,malzeme):
    super().__init__(isim,fiyat,aciklama,sos_tur)
    self.malzeme = malzeme

class Klasik_pizza(pizza):
  def __init__(self,isim,fiyat,aciklama,sos_tur,malzeme):
    super().__init__(isim,fiyat,aciklama,sos_tur)
    self.malzeme = malzeme

class Margherita_pizza(pizza):
  def __init__(self,isim,fiyat,aciklama,sos_tur,malzeme):
    super().__init__(isim,fiyat,aciklama,sos_tur)
    self.malzeme = malzeme

class Dominos_pizza(pizza):
  def __init__(self,isim,fiyat,aciklama,sos_tur,malzeme):
    super().__init__(isim,fiyat,aciklama,sos_tur)
    self.malzeme = malzeme

#Sos Subclasses
class Zeytin_sos(sos):
  def __init__(self,isim,fiyat,aciklama):
    super().__init__(isim,fiyat,aciklama)

class Mantar_sos(sos):
  def __init__(self,isim,fiyat,aciklama):
    super().__init__(isim,fiyat,aciklama)

class Keci_Peynir_sos(sos):
  def __init__(self,isim,fiyat,aciklama):
    super().__init__(isim,fiyat,aciklama)

class Et_sos(sos):
  def __init__(self,isim,fiyat,aciklama):
    super().__init__(isim,fiyat,aciklama)

class Sogan_sos(sos):
  def __init__(self,isim,fiyat,aciklama):
    super().__init__(isim,fiyat,aciklama)

class Misir_sos(sos):
  def __init__(self,isim,fiyat,aciklama):
    super().__init__(isim,fiyat,aciklama)

#Sos Data Adding
Zeytin_sos = Zeytin_sos("Zeytin Sos",10,"Bol Acı Sos")
Mantar_sos = Mantar_sos("Mantar Sos",20,"Bol Acı Sos")
Keci_Peynir_sos = Keci_Peynir_sos("Keçi Peynir Sos",30,"Bol Acı Sos")
Et_sos = Et_sos("Et Sos",40,"Bol Acı Sos")
Sogan_sos = Sogan_sos("Soğan Sos",50,"Bol Acı Sos")
Misir_sos = Misir_sos("Mısır Sos",60,"Bol Acı Sos")

#User Class
class kredi_karti:
    def __init__(self,kredi_karti_no,kredi_karti_sifre,en_son_kullanim):
        self.kredi_karti_no = kredi_karti_no
        self.kredi_karti_sifre = kredi_karti_sifre
        self.en_son_kullanim = en_son_kullanim

class kullanici(kredi_karti):
    def __init__(self,isim,soyisim,TC_No,kredi_karti_no,kredi_karti_sifre,en_son_kullanim):
        self.isim = isim
        self.soyisim = soyisim
        self.TC_No = TC_No
        super().__init__(kredi_karti_no,kredi_karti_sifre,en_son_kullanim)

class satis_islem(kullanici):
    def __init__(self,isim,soyisim,TC_No,kredi_karti_no,kredi_karti_sifre,en_son_kullanim,satin_alinan_pizza_isim,satin_alinan_pizza_fiyat):
        super().__init__(isim,soyisim,TC_No,kredi_karti_no,kredi_karti_sifre,en_son_kullanim)
        self.satin_alinan_pizza_isim = satin_alinan_pizza_isim
        self.satin_alinan_pizza_fiyat = satin_alinan_pizza_fiyat

#Selecet pizza function for user

def musteri_pizza_secme(pizza_deger,sos_deger, k_isim, k_soyisim, k_tc, k_kredi_no, k_sifre):
  print("-------------------------------------------------------------")
  print("PİZZA TÜRLERİ")
  print("Türk Pizza - Klasik Pizza - Margherita Pizza - Dominos Pizza")
  print("-------------------------------------------------------------")
  print("SOS TÜRLERİ")
  print("Zeytin - Mantar - Keçi Peyniri - Et - Soğan - Mısır")
  print("-------------------------------------------------------------")
  print("Pizza türünü seçiniz ve eğer sos istemiyorsanız 'no' yazınız.")
  print("-------------------------------------------------------------")
  pizza_select = pizza_deger
  sos_select = sos_deger

  if pizza_select == "Türk Pizza":
    Turk_Pizza1 = Turk_pizza("Türk Pizza",200,"Yozgat Yapımı", sos_select,["yumurta","un"])
    secilen_urun_yazdir(Turk_Pizza1.isim,Turk_Pizza1.sos_tur,Turk_Pizza1.bilgi_fiyat())
    kullanici_islem(Turk_Pizza1.isim,Turk_Pizza1.fiyat,k_isim, k_soyisim, k_tc, k_kredi_no, k_sifre)
  elif pizza_select == "Klasik Pizza":
    Klasik_Pizza1 = Klasik_pizza("Klasik Pizza",220,"Kayseri Yapımı",sos_select,["yumurta","un"])
    secilen_urun_yazdir(Klasik_Pizza1.isim,Klasik_Pizza1.sos_tur,Klasik_Pizza1.bilgi_fiyat())
    kullanici_islem(Klasik_Pizza1.isim,Klasik_Pizza1.fiyat,k_isim, k_soyisim, k_tc, k_kredi_no, k_sifre)
  elif pizza_select == "Margherita Pizza":
    Margherita_pizza1 = Margherita_pizza("Margherita Pizza",240,"Kırşehir Yapımı",sos_select,["yumurta","un"])
    secilen_urun_yazdir(Margherita_pizza1.isim,Margherita_pizza1.sos_tur,Margherita_pizza1.bilgi_fiyat())
    kullanici_islem(Margherita_pizza1.isim,Margherita_pizza1.fiyat,k_isim, k_soyisim, k_tc, k_kredi_no, k_sifre)
  elif pizza_select == "Dominos Pizza":
    Dominos_pizza1 = Dominos_pizza("Dominos Pizza",260,"Nevşehir Yapımı",sos_select,["yumurta","un"])
    secilen_urun_yazdir(Dominos_pizza1.isim,Dominos_pizza1.sos_tur,Dominos_pizza1.bilgi_fiyat())
    kullanici_islem(Dominos_pizza1.isim,Dominos_pizza1.fiyat,k_isim, k_soyisim, k_tc, k_kredi_no, k_sifre)
  else:
    print("Hatalı işlem yaptınız! Lütfen pizza seçiniz!")

def kullanici_islem(urun_isim,urun_fiyat, k_isim, k_soyisim,k_tc, k_kredi_no, k_sifre):
  zaman = datetime.datetime.now()
  zaman = datetime.datetime.strftime(zaman, '%d.%m.%Y. %X')
  global satis1
  satis1 = satis_islem(k_isim,k_soyisim,k_tc,k_kredi_no,k_sifre,zaman,str(urun_isim),str(urun_fiyat))
  deger_pizza_musteri = [satis1.isim,satis1.soyisim,satis1.TC_No,satis1.kredi_karti_no,satis1.kredi_karti_sifre,satis1.en_son_kullanim,satis1.satin_alinan_pizza_isim,satis1.satin_alinan_pizza_fiyat]
  with open('pizza_musteri.csv','a') as pizza_musteri:
    yazdirma_islem = csv.writer(pizza_musteri)
    yazdirma_islem.writerow(deger_pizza_musteri)
  
  print("-------------------------------------------------------------")
  print("MÜŞTERİ BİLGİLERİ")
  print("Müşteri İsmi ve Soyadı: {} {}\nMüşteri TC No: {}".format(satis1.isim,satis1.soyisim,satis1.TC_No))
  print("-------------------------------------------------------------")
  print("ÖDEME BİLGİLERİ")
  print("Kredi Kartı Numarası: {}\nKredi Kartı Şifresi: {}\nÖdeme Tarihi: {}".format(satis1.kredi_karti_no,satis1.kredi_karti_sifre,satis1.en_son_kullanim))
  print("-------------------------------------------------------------")
  
def secilen_urun_yazdir(isim,sos,fiyat):
  print("-------------------------------------------------------------")
  print("-------------------------------------------------------------")
  print("-------------------------------------------------------------")
  print("PİZZA BİLGİLERİ")
  print("Seçilen Pizza: {}\nSos : {}\nToplam Tutar: {}".format(isim,sos,fiyat))
  print("-------------------------------------------------------------")
  print("-------------------------------------------------------------")
  print("-------------------------------------------------------------")

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('icon/PizzaDeniz.png', 10, 10, 30)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(50)
        # Title
        self.cell(10, 10, 'Pizza Deniz - Online Odeme')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Fatura Belgesi' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# Instantiation of inherited class
class fatura():
  def islem():
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)

    pdf.cell(0,5,"Bu fatura belgesi online ortam uzerinde olusturulmustur.",0,1)
    pdf.cell(0,5,"Bu fatura belgesi musterinin istegi uzerine olusturulmustur.",0,1)
    pdf.cell(0,5,"Bu belgeyi saklayiniz.",0,1)
    pdf.cell(0,5," ",0,1)
    pdf.line(0,45,210,45)

    pdf.cell(0,5,"FATURA DUZENLEYICI SIRKET BILGILERI",0,1)
    pdf.line(0,55,100,55)
    pdf.cell(0,5,"Sirket Adi                 :"+str(" ")+str("Pizza Deniz"),0,1)
    pdf.cell(0,5,"Fatura Duzenleme Ortami:"+str(" ")+str("Online"),0,1)
    pdf.cell(0,5,"Sirket Adresi            :"+str(" ")+str("Turkiye"),0,1)
    pdf.cell(0,5,"Sirket Vergi No        :"+str(" ")+str("123456789"),0,1)

    pdf.cell(0,5," ",0,1)
    pdf.cell(0,5,"SIPARIS EDILEN URUN BILGILERI",0,1)
    pdf.line(0,85,100,85)

    pdf.cell(0,5,"Urun Tipi             :"+str(" ")+str("Pizza"),0,1)
    pdf.cell(0,5,"Urun Turu           :"+str(" ")+str(satis1.satin_alinan_pizza_isim),0,1)
    pdf.cell(0,5,"Urun Fiyat           :"+str(" ")+str(satis1.satin_alinan_pizza_fiyat),0,1)

    pdf.cell(0,5," ",0,1)
    pdf.cell(0,5,"MUSTERI BILGILERI:",0,1)
    pdf.line(0,110,100,110)
    pdf.cell(0,5,"Musteri Isim            :"+str(" ")+str(satis1.isim),0,1)
    pdf.cell(0,5,"Musteri Soyisim      :"+str(" ")+str(satis1.soyisim),0,1)
    pdf.cell(0,5,"Musteri TC No        :"+str(" ")+str(satis1.TC_No),0,1)

    pdf.cell(0,5," ",0,1)
    pdf.cell(0,5,"ODEME BILGILERI:",0,1)
    pdf.line(0,135,100,135)
    pdf.cell(0,5,"Odeme Tipi                    :"+str(" ")+str("Online Banka Odemesi"),0,1)
    pdf.cell(0,5,"Odeme Tarihi                 :"+str(" ")+str(satis1.en_son_kullanim),0,1)
    pdf.cell(0,5,"Kredi/Banka Karti No     :"+str(" ")+str(satis1.kredi_karti_no),0,1)
    pdf.cell(0,5,"Kredi/Banka Karti Sifre  :"+str(" ")+str(satis1.kredi_karti_sifre),0,1)

    pdf.line(0,160,210,160)
    pdf.image('icon/PizzaDeniz.png')


    bilgi_deger_yazi = "MusteriFatura"+str("_")+str(satis1.en_son_kullanim)
    print(bilgi_deger_yazi)

    try:
      pdf.output((bilgi_deger_yazi)+'.pdf', 'F')
    except:
      pdf.output((bilgi_deger_yazi)+'.pdf', 'F')