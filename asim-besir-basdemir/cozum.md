## 1. PostgreSQL Konteyneri Kurulumu ve Güvenlik Önlemleri

### İmaj Çekme

```bash
docker pull docker.io/library/postgres:latest
```
> Burada resmi bir sağlayıcı kullanarak güvenliği artırıyoruz.


### Kullanıcı Adı ve Parola Belirleme (Imperative)

```bash
docker run --name postgres-container -e POSTGRES_USER=kullanici -e POSTGRES_PASSWORD=parola -d postgres
```

> `-d`: detach mode  
> Burada güçlü bir parola seçmeye dikkat etmeliyiz.


### Port Forwarding

```bash
docker run --name postgres-container -d -p 226:5432 postgres
```

> Container'daki 5432 port'unu ana makinedeki 226 portuna bağladık. Bunun sebebi 5432'nin çokça biliniyor olması ve bir saldırgan tarafından hedef haline gelme ihtimalinin yüksek olması.  
> Öte yandan 226 portu *nmap* kaynak koduna göre en az sıklıkta kullanılan portlardan biri ve *nmap* gibi uygulamalar da bu portu en son seçenek olarak görüyor ve taramıyor genelde.  
> Benzer portlar: 228, 229, 234, 238, 270...


### Volume Bağlama

```bash
mkdir postgres-data
docker run --name postgres-container -d -v /home/slime/docker/itu-sgmyo-virtualization-2025-exam/postgres-data:/var/lib/postgresql/data postgres
```


### Init Scripts

```bash
docker run --name postgres-container -d -v /home/slime/docker/itu-sgmyo-virtualization-2025-exam/init-scripts:/docker-entrypoint-initdb.d/ postgres
```


### Log Takibi

```bash
docker logs --details --timestamps postgres-container
```

> Hem daha detaylı hem de zaman verisiyle birlikte log'u daha iyi anlamak için bu 2 parametreyi kullandım.


### Nihai Konteyner Oluşturma Komutu

```bash
docker run --name postgres-container \
--security-opt=no-new-privileges \
--restart=on-failure:10 \
--memory=1024m \
--cpus=2 \
-d \
-e POSTGRES_USER=kullanici \
-e POSTGRES_PASSWORD=parola \
-e POSTGRES_DB=logs \
-p 226:5432 \
-v /home/slime/docker/itu-sgmyo-virtualization-2025-exam/init-scripts:/docker-entrypoint-initdb.d/ \
-v /home/slime/docker/itu-sgmyo-virtualization-2025-exam/postgres-data:/var/lib/postgresql/data \
postgres
```

> `--security-opt=no-new-privileges` kullanarak privilege escalation saldırılarının önüne geçmeye çalışıyorum.  
> Ayrıca `--restart=on-failure:10` ile birlikte DoS gibi saldırılarda konteynerin sürekli olarak yeniden başlayıp sisteme yük bindirmemesi için en fazla 10 kere yeniden başlayacağını belirtiyorum.  
> Benzer bir sebeple `--memory=1024m --cpus=2` parametrelerini kullanıp konteynerin kaynak kullanımını sınırlandırıyorum.


### Konteynıra Girmek

```bash
docker exec -it postgres-container bash
```


### Veritabanına Bağlanmak

```bash
psql -d postgres -U kullanici
```

> Daha sonra şifre için sorar.


### SQL Sorgusu

```sql
SELECT * FROM security_logs WHERE severity = 'HIGH';
```

#### Çıktı:

```sql
logs=# SELECT * FROM security_logs WHERE severity = 'HIGH';
 id |         timestamp          |   source_ip   | destination_ip | protocol | port |   event_type    | severity |            description
----+----------------------------+---------------+----------------+----------+------+-----------------+----------+------------------------------------
  1 | 2025-04-14 16:17:45.068707 | 192.168.1.100 | 10.0.0.1       | TCP      |   22 | SSH Brute Force | HIGH     | Multiple failed SSH login attempts
(1 row)
```


## 2. Dockerfile ile Uygulama İmajı Oluşturma ve Yükleme

### Build Etmek

```bash
docker build --tag my-python-app .
```


### Test Etmek

```bash
docker run -d -p 5001:5000 my-python-app
```


### Layerlara Bakmak

İmaj ID'sini bulmak için:

```bash
docker images -a
```

Layer’ları incelemek için:

```bash
docker history 2e5d08f79862
```


### DockerHub’a Yüklemek

Giriş yapmak:

```bash
docker login -u misile00
```

İmajı etiketlemek ve yüklemek:

```bash
docker tag my-python-app:latest misile00/itu-sgmyo-files:latest
docker push misile00/itu-sgmyo-files:latest
```

**Adres:** [https://hub.docker.com/r/misile00/itu-sgmyo-files](https://hub.docker.com/r/misile00/itu-sgmyo-files)

### Docker Compose
docker-compose.yml dosyasını yazdım. Daha sonraysa aşağıdaki komutla çalıştırdım:
```bash
docker-compose up --build
```