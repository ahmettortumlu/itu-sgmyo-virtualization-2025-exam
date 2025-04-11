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

1. Postgresql i docker container olarak kaldırmanızı istiyorum. (30 puan)

Bunu yaparken, 
* dockerhub'tan bulduğunuz bir docker imajını kullanın,
* imperatif şekilde yani docker cli kullanarak bunu gerçekleştirin,
* kullanıcı adı, şifre ve veritabanı isimlerini ortam değişkeni siz belirleyin
* bilgisayarınızın portundan erişebilir yapın,
* Bu repo'da bir dizin oluşturun ve bu dizini postgres-data olarak isimlendirin. Bu dizinde postgresql datasını saklayın. Böylece container silinse de data dizininiz kaybolmasın.
* init-scripts ile database'i kaldırırken bir takım db initialize işlemlerini gerçekleştir. ????
```
-- init-scripts/01-init.sql
CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Örnek veriler
INSERT INTO items (name, description) VALUES
    ('Item 1', 'First sample item'),
    ('Item 2', 'Second sample item'),
    ('Item 3', 'Third sample item');
```

2. Kaynak kodu verilen python scriptinden bir docker imajı oluştur. Bu docker imajı oluştururken;
İpucu:  Ana referans olarak python:3.9-slim imajını al, FLASK_APP=app.py ve FLASK_ENV=development olmak üzere iki adet ortam değişkeni tanımla. (20 puan)

3. İlk iki adımı docker-compose kullanarak gerçekleştir. (30 puan)

4. Sanallaştırma ve bulut teknolojilerinde kullanılan güvenlik iyi pratiklerini aşağıdaki adımları gerçekleştirirken uygulayınız ve not olarak yazınız. (20 puan)
