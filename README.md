# global-ai-hub-akbank-python-bootcamp
Grafik Arayüz ile Pizzacı Dükkanı Projesi

PyQt5 kurmak için:

pip install PyQt5

Python grafik arayüz kütüphanesi PyQt5 ile bir pizzacı işletmesinin şipariş alma ve CSV destekli bir veritabanına eklenmesi sağlanmaktadır.
Müşteri için Türk Pizza, Klasik Pizza, Margherita Pizza ve Dominos Pizza çeşitleri ve mantar sosu, mısır sosu, keçi peyniri sosu, et sosu, soğan sosu,zeytin sosu oluşturulmuştur. Bu sosların ve pizzaların her biri için class oluşturulmuştur. Bu classlara isim, değer, açıklama gibi özellikler eklenmiş ve bu classlar ile pizzalar ve soslar için nesneler oluşturulmuştur.
Müşteriden ise isim, soyisim, kimlik numarası, kredi kartı kimlik numarası ve kredi kartı şifresi istenmektedir. Ödeme işlemi yapıldıktan sonra CSV dosyasına Python'da yer alan datetime kütüphanesinden alınan zaman bilgisli ile diğer gerekli bilgiler kayıt edilmektedir. Kullanıcı isterse fatura alma özelliği ile şiparişi ile ilgili PDF dosyasını da alabilir.
