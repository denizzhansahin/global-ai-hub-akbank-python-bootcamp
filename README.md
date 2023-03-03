# global-ai-hub-akbank-python-bootcamp
Grafik Arayüz ile Pizzacı Dükkanı Projesi!

<p align="center">
  <img width="500" height="200" src="https://user-images.githubusercontent.com/95483485/222830777-cf2ec043-ea21-452e-b81b-384625170379.png">
</p>



PyQt5 kurmak için:

            pip install PyQt5

FPDF kurmak için:

            pip install fpdf

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

Uygulama Jupiter Notenook dosyası ve Python dosyaları olmak üzere iki farklı kullanım ile hazırlanmıştır. Jupiter Notebook dosyası ve Python dosyası Google Colab veya herhangi bir IDE ile kullanılabilir.

Grafik arayüz ile uyumlu Python dosyasını çalıştırmak için:

          python3 Pizza.py

Pizza.py dosyası ise ilgili tüm class ve diğer özellikleri ise pizza_class.py isimli Python dosyasından almaktadır.

Grafik arayüzü görüntüsü:

<p align="center">
<img width="988" height="999" src="https://user-images.githubusercontent.com/95483485/222834053-143140e4-8e84-4990-9a9b-6498028587fa.png">
</p>

Konsol ekranı görüntüsü:

<p align="center">
<img width="988" height="999" src="https://user-images.githubusercontent.com/95483485/222834672-6cfa1b95-987e-49aa-8ac3-c2d92fa1bd0f.png">
</p>
