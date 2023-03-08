# global-ai-hub-akbank-python-bootcamp
Grafik Arayüz ile Pizzacı Dükkanı Projesi!

<p align="center">
  <img width="500" height="200" src="https://user-images.githubusercontent.com/95483485/222830777-cf2ec043-ea21-452e-b81b-384625170379.png">
</p>



PyQt5 kurmak için:

            pip install PyQt5

FPDF kurmak için:

            pip install fpdf

Python dosyası (Pizza.py) çalıştırmak için:
          
          python3 Pizza.py

Python grafik arayüz kütüphanesi PyQt5 ile bir pizzacı işletmesinin şipariş alma ve CSV destekli bir veritabanına eklenmesi sağlanmaktadır.
Müşteri için Türk Pizza, Klasik Pizza, Margherita Pizza ve Dominos Pizza çeşitleri ve mantar sosu, mısır sosu, keçi peyniri sosu, et sosu, soğan sosu,zeytin sosu oluşturulmuştur. Bu sosların ve pizzaların her biri için class oluşturulmuştur. Bu classlara isim, değer, açıklama gibi özellikler eklenmiş ve bu classlar ile pizzalar ve soslar için nesneler oluşturulmuştur.

Müşteriden ise isim, soyisim, kimlik numarası, kredi kartı kimlik numarası ve kredi kartı şifresi istenmektedir. Müşteriden istenen bilgilerin nesne olarak depolanması ise müşteri ile ilgili classlar arası miras alma yoluyla yapılmıştır. 

Ödeme işlemi yapıldıktan sonra CSV dosyasına Python'da yer alan datetime kütüphanesinden alınan zaman bilgisli ile diğer gerekli bilgiler kayıt edilmektedir. Kullanıcı isterse fatura alma özelliği ile şiparişi ile ilgili PDF dosyasını da alabilir.

Aşağıda ise pizza ve soslar ile ilgili classların yapısı ile ilgili kodlar paylaşılmıştır.
Fonksşyonlar ile ilgili kodlar:

                      class Dekorasyon():
                        def __init__(self,fiyat,aciklama):
                          self.fiyat = fiyat
                          self.aciklama = aciklama

                        def bilgi_fiyat(self):
                          return "Fiyat :" + " " + str(self.fiyat)

                        def bilgi_aciklama(self):
                          return "Açıklama :" + " " + str(self.aciklama)
Pizza ile ilgili kodlar:

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

Sos ile ilgili kodlar:
        
                       class sos(Dekorasyon):
                            def __init__(self,isim,fiyat,aciklama):
                              super().__init__(fiyat,aciklama)
                              self.isim = isim
 

Örnek pizza ve sos kodlar:
                    
                    #pizza kodu
                    class Turk_pizza(pizza):
                      def __init__(self,isim,fiyat,aciklama,sos_tur,malzeme):
                        super().__init__(isim,fiyat,aciklama,sos_tur)
                        self.malzeme = malzeme
                    
                    #sos kodu
                    class Zeytin_sos(sos):
                      def __init__(self,isim,fiyat,aciklama):
                        super().__init__(isim,fiyat,aciklama)

Örnek pizza ve sos için nesnelerin oluşturulması:
                     
                     #sos nesnesi
                     Zeytin_sos = Zeytin_sos("Zeytin Sos",10,"Bol Acı Sos")
                     
                     #pizza nesnesi
                     Turk_Pizza1 = Turk_pizza("Türk Pizza",200,"Yozgat Yapımı", sos_select,["yumurta","un"])


Kullanıcı ve kredi kartı ile ödeme işlemi için classların oluşturulması ile ilgili kodlar:
                    
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

Müşterinin seçtiği pizza ile ilgili nesne oluşturma kodu ise aşağıda paylaşılmıştır. Ayrıca musteri_pizza_secme, kullanici_secim fonksiyonları birbirleri ile bağlantılıdır ve aşağıda paylaşılmıştır. Ayrıca secilen_urun_yazdir fonksiyonu ise müşterinin seçtiği pizza ile ilgili ekrana çıktı yazdırır.

Müşterinin pizza seçimi ile kodların bir kısmı:

                    def musteri_pizza_secme(pizza_deger,sos_deger, k_isim, k_soyisim, k_tc, k_kredi_no, k_sifre):
                        pizza_select = pizza_deger
                        sos_select = sos_deger

                        if pizza_select == "Türk Pizza":
                          Turk_Pizza1 = Turk_pizza("Türk Pizza",200,"Yozgat Yapımı", sos_select,["yumurta","un"])
                          secilen_urun_yazdir(Turk_Pizza1.isim,Turk_Pizza1.sos_tur,Turk_Pizza1.bilgi_fiyat())
                          kullanici_islem(Turk_Pizza1.isim,Turk_Pizza1.fiyat,k_isim, k_soyisim, k_tc, k_kredi_no, k_sifre)

Kullanıcının bilgileri ile şipariş bilgilerinin CSV ile kayıt edilmesi ile ilgili kodlar:
                    
                    def kullanici_islem(urun_isim,urun_fiyat, k_isim, k_soyisim,k_tc, k_kredi_no, k_sifre):
                      zaman = datetime.datetime.now()
                      zaman = datetime.datetime.strftime(zaman, '%d.%m.%Y. %X')
                      satis1 = satis_islem(k_isim,k_soyisim,k_tc,k_kredi_no,k_sifre,zaman,str(urun_isim),str(urun_fiyat))
                      deger_pizza_musteri = [satis1.isim,satis1.soyisim,satis1.TC_No,satis1.kredi_karti_no,satis1.kredi_karti_sifre,satis1.en_son_kullanim,satis1.satin_alinan_pizza_isim,satis1.satin_alinan_pizza_fiyat]
                      with open('pizza_musteri.csv','a') as pizza_musteri:
                        yazdirma_islem = csv.writer(pizza_musteri)
                        yazdirma_islem.writerow(deger_pizza_musteri)

Şipariş ile bilgilerin ekrana yazdırılması ile kodların bir kısmı:

                    def secilen_urun_yazdir(isim,sos,fiyat):
                      print("Seçilen Pizza: {}\nSos : {}\nToplam Tutar: {}".format(isim,sos,fiyat))

Grafik arayüz ile ilgili dosya ile elde edilen verinin aktarılması ile ilgili kodların bir kısmı aşağıda paylaşılmıştır.
                  
                    self.turk_pizza_sec.stateChanged.connect(turk_pizza_secim)
                    
                    self.zeytin_sos_sec.stateChanged.connect(zeytin_sos_secim)
                    
                    self.odeme_yap.clicked.connect(self.odeme_yapmak)
                    
                  def odeme_yapmak(self):
                    try:
                        pizza_class.musteri_pizza_secme(pizza_secim,sos_secim,self.isim_line.text(),self.soyisim_line.text(),self.tc_no_line.text(),self.kart_no_line.text(),self.kart_sifre_line.text())
                    except:
                        print("HATA İŞLEM YAPILAMADI!")
            
             def turk_pizza_secim():
                global pizza_secim
                pizza_secim = "Türk Pizza"

             def zeytin_sos_secim():
                global sos_secim
                sos_secim = "Zeytin"

Örnek CSV dosyası bilgileri ise aşağıdaki gibidir. Sırası ile isim, soyisim,kimlik numarası, kredi kartı numarası, kredi kartı şifresi, ödeme tarihi, şipariş edilen ürünün adı ve şipariş tutarı yazılmıştır.

            Denizhan,Sahin,123456789000000,222222222222222,143242,05.03.2023. 01:29:02,Dominos Pizza,290

Uygulama Jupiter Notenook dosyası ve Python dosyaları olmak üzere iki farklı kullanım ile hazırlanmıştır. Jupiter Notebook dosyası ve Python dosyası Google Colab veya herhangi bir IDE ile kullanılabilir. Ayrıca Jupiter Notebook dosyası içinde PDF ile fatura alma özelliği mevcut değildir.

PDF ile fatura alma özelliği pizza_class.py dosyası içinde yer alan PDF isimli class ile yapılmaktadır. Pizza.py ile aşağıdaki komut ile ilgili class çalıştırılır.

            self.fatura_goster.clicked.connect(self.fatura)

        def fatura(self):
            try:
                pizza_class.fatura.islem()
            except:
                print("HATA FATURA OLUŞTURULAMADI!")
                
pizza_class.fatura.islem() ile aşağıdaki kod çalıştırılır ve bu kod pizza_class.py içinde yer alır.

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


          def footer(self):
              # Position at 1.5 cm from bottom
              self.set_y(-15)
              # Arial italic 8
              self.set_font('Arial', 'I', 8)
              # Page number
              self.cell(0, 10, 'Fatura Belgesi' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

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


          pdf.cell(0,5," ",0,1)
          pdf.cell(0,5,"SIPARIS EDILEN URUN BILGILERI",0,1)
          pdf.line(0,85,100,85)

          pdf.cell(0,5,"Urun Tipi             :"+str(" ")+str("Pizza"),0,1)
          pdf.cell(0,5,"Urun Turu           :"+str(" ")+str(satis1.satin_alinan_pizza_isim),0,1)
          pdf.cell(0,5,"Urun Fiyat           :"+str(" ")+str(satis1.satin_alinan_pizza_fiyat),0,1)



          pdf.line(0,160,210,160)
          pdf.image('icon/PizzaDeniz.png')


          bilgi_deger_yazi = "MusteriFatura"+str("_")+str(satis1.en_son_kullanim)
          print(bilgi_deger_yazi)

          try:
            pdf.output((bilgi_deger_yazi)+'.pdf', 'F')
          except:
            pdf.output((bilgi_deger_yazi)+'.pdf', 'F')


Grafik arayüz dosyasını (form.ui), Python dosyasına (Pizza.py) dönüştürmek için:

          pyuic5 -x form.ui -o Pizza.py
      
Python dosyası (Pizza.py) çalıştırmak için:
          
          python3 Pizza.py

Pizza.py dosyası ise ilgili tüm class ve diğer özellikleri ise pizza_class.py isimli Python dosyasından almaktadır.

Grafik arayüzü görüntüsü:

<p align="center">
<img width="988" height="999" src="https://user-images.githubusercontent.com/95483485/222959124-e0afd6c0-0ba8-4d65-ae6e-8c46f732e9a8.png">
</p>

Konsol ekranı görüntüsü:

<p align="center">
<img width="988" height="999" src="https://user-images.githubusercontent.com/95483485/222959147-776cac72-a01f-4e4c-8834-cb0766ad59d2.png">
</p>

Fatura görseli PDF olarak :

<p align="center">
<img width="988" height="999" src="https://user-images.githubusercontent.com/95483485/222959217-9633b656-0ecc-419a-bf54-08b0a875e01c.png">
</p>

