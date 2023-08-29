Proje Açıklaması:

Bu proje, Flask framework'ü kullanılarak geliştirilen bir Araba Fiyatı Tahmin API'sini temsil eder.
Amacı, kullanıcılara veri tabanlı tahmini araba fiyatlarını sunmaktır.
Veri kümesi olarak Kaggle'dan alınan bir araba fiyatı veri kümesi kullanılmaktadır.

Bağımlılıkların Yüklenmesi:

Projenin başlaması için öncelikle gerekli Python bağımlılıklarını yüklemek gerekmektedir.
Bu bağımlılıklar requirements.txt dosyasında listelenir.
Bağımlılıkları yüklemek için terminalde projenin kök dizinine giderek aşağıdaki komut çalıştırılabilir:
pip install -r requirements.txt

Flask Uygulamasının Başlatılması:

Bağımlılıklar yüklendikten sonra, Flask uygulamasını başlatmak gerekmektedir.
Terminalde aşağıdaki komut çalıştırılarak uygulama başlatılabilir:
flask run
Uygulama başarıyla başladığında, http://localhost:5000 adresinden API'ye erişilebilir olacaktır.

API Kullanımı:

API'yi kullanmak için /predict endpoint'ine POST isteği yapmanız gerekmektedir.
İstek gövdesinde arabaların tahmin edilmesi için gereken parametreler bulunmalıdır (örneğin, marka, model, yıl, kilometre, vb.).
Bu parametreler JSON formatında istek gövdesine eklenmelidir.

Tahmin ve Sonuç:

API aldığı verilere dayanarak tahmini bir fiyat üretecektir.
Sonuç JSON formatında dönüş yapılacaktır, bu sonuç tahmini araba fiyatını içerecektir.

Veri Seti:

Proje için Kaggle'dan temin edilen bir araba fiyatı veri kümesi kullanılmaktadır.
