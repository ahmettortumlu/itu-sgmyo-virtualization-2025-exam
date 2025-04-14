# 2025 Yılı Sanallaştırma ve Bulut teknolojileri ara sınavı

Değerli İTÜ'lü, sınavda başarılar!

# Sınav Öncesi
Bu repo'yu nasıl localinize çekebilirsiniz?
Aşağıdaki komutu terminalinizden çalıştırarak gerçekleştirebilirsiniz.

Sizden beklediğim şey kendi dosya dizininize gidip oradaki dosyaları düzenleyip bu repository'e merge request açmanız. 

Öncelikle şimdi bu repo'yu clone'layın:
```bash
git clone https://github.com/ahmettortumlu/itu-sgmyo-virtualization-2025-exam.git
```

Sonra `kendinize özel isimle` bir branch açın:

```bash
git checkout -b ismini-yaz
```

Şimdi bilgisayarlarınızda bu repository'deki dosya  dizinine giderek sınava başlayabilirsiniz. Sınav sonuna kadar git ile alakalı bir işlem yapmanıza gerek yok. Çalışmalarınız bittiğinde aşağıdaki gibi komutlarla çalışmayı nihayete erdireceğiz:

```bash
git add .
git commit -m "senin-adin çözümü"
git push origin ismini-yaz
```

Sonra github sayfasından branch'e gidip merge request açacaksınız.

Şimdi asıl konumuz sınava gelelim. Sınav süremiz iki saattir. Yukarıdaki işlemlere de yarım saat kadar süre verdim. Toplamda sınav süreniz 2,5 saat olmasını bekliyorum.

# Sınav soruları
1. Sanallaştırma ve bulut teknolojilerinde kullanılan güvenlik iyi pratiklerini aşağıdaki adımları gerçekleştirirken uygulayınız ve not olarak yazınız. (20 puan)

2. Postgresql i docker container olarak kaldırmanızı istiyorum. (30 puan)

Bunu yaparken, 
* dockerhub'tan bulduğunuz bir docker imajını kullanın,
* imperatif şekilde yani docker cli kullanarak bunu gerçekleştirin,
* kullanıcı adı, şifre ve veritabanı isimlerini ortam değişkeni kullanarak siz belirleyin
* servisin bilgisayarınızın portundan erişebilir yapın (port-forwarding),
* Bu repo'da bir dizin oluşturun ve bu dizini postgres-data olarak isimlendirin. Bu dizinde postgresql datasını saklayın. Böylece container silinse de data dizininiz kaybolmasın.
* init-scripts ile database'i kaldırırken bir takım db initialize işlemlerini gerçekleştir. 
* Kaldırdığın container'ın düzgün çalıştığının kontrolünü loglarına bakarak yap,
* Aşağıdaki komutu container içinde çalıştırarak logların düzgün geldiğini gözlemle:
"SELECT * FROM security_logs WHERE severity = 'HIGH';"
Not: Burada postgresql komutunu çalıştırabilmen için bir takım komutlar çalıştırmanı bekliyorum.

3. Kaynak kodu verilen python scriptinden bir docker imajı oluştur. Bu docker imajı oluştururken;
İpucu:  Ana referans olarak python:3.9-slim imajını al, FLASK_APP=app.py ve FLASK_ENV=development olmak üzere iki adet ortam değişkeni tanımla. (20 puan) 
* Kaldırdığın imajı incele ve layerlarını gözlemle,
* Oluşturduğun imajı dockerhub hesabına gönder. 

4. İlk iki adımı docker-compose kullanarak gerçekleştir. (30 puan)
Docker compose dosyanızın içinde aşağodaki değişkenleri tanımla:
```yml
DB_HOST: postgres
DB_NAME: mydb
DB_USER: myuser
DB_PASSWORD: mypassword
```

Not: Çözüm'ü anlattığın bir dosya hazırla ve Çalıştırdığın tüm komutları çözüm dosyana ekle. Servislerin loglarına çalıştırdığın servislerin logları, imajların inspect edilmesi ve servislerin tüm işlem bittiğinde silinmesi imajların temizlenmesi adımları gibi adımlarda bu docker komutlarından inceleyeceğim.
