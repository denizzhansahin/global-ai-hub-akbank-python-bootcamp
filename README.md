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
