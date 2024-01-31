
![](https://github.com/furkanyalcindag/comitfy-kolaysis/blob/main/addons/web/static/img/kolaysisLogo.png)

Kolaysis, web tabanlı iş uygulamalarından oluşan bir pakettir. Ana Kolaysis Uygulamaları arasında CRM, Proje Yönetimi, Faturalama ve Muhasebe, Satış Noktası, İnsan Kaynakları, Pazarlama, Üretim, Satın Alma Yönetimi bulunmaktadır. Kolaysis Uygulamaları bağımsız uygulamalar olarak kullanılabilir, ancak aynı zamanda sorunsuz bir şekilde entegre olurlar, böylece birkaç uygulama yüklediğinizde tam özellikli bir Açık Kaynak ERP elde edebilirsiniz.

# Kolaysis ile Ubuntu'da Çalışmaya Başlama

Standart bir Ubuntu kurulumu için aşağıdaki adımları izleyebilirsiniz.

Terminal'i açın ve kurulumu başlatın.

### Python Yükleyerek İşe Başlayalım:

```
sudo apt install python3-pip
```

Yüklemeyi doğrulamak için aşağıdaki komutu çalıştırın:

```
pip3 --version
```

### PostgreSQL Yükleyelim:

Dosya Repository yapılandırmasını oluşturun:

```
sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
```

Repository imzalama anahtarını içe aktarın:

```
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```

Paket listelerini güncelleyin:

```
sudo apt-get update
```

 PostgreSQL'in en son sürümünü yükleyin. Belirli bir sürüm istiyorsanız, 'postgresql' yerine 'postgresql-12' veya benzerini kullanın:

 ```
 sudo apt-get -y install postgresql
```

 ### PgAdmin 4 Yüklemeyle Devam Edelim:

Repository için ortak anahtarı yükleyin (daha önce yapılmadıysa):

```
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg
```

Repository yapılandırma dosyasını oluşturun:

```
sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
```

pgAdmin'i yükleyin:

```
sudo apt install pgadmin4-web
```

Eğer pgadmin4-web yüklediyseniz, web sunucusunu yapılandırın:

```
sudo /usr/pgadmin4/bin/setup-web.sh
```

Projeyi bilgisayarımıza klonlayalım:

```
git clone https://github.com/furkanyalcindag/comitfy-kolaysis.git --depth 1 --branch main --single-branch Comitfy-Kolaysis
```

Projeyi başarılı bir şekilde klonladıktan sonra projenin dizinine gidip aşağıdaki komutu çalıştıralım:

```
pip3 install -r requirements.txt
```

### Projemizdeki Gereksinimleri Yükledikten Sonra Veritabanında Kullanıcı ve Veritabanı Oluşturalım:

```
sudo su - postgres
```

```
create user --createdb --username postgres --no-createrole -no-superuser --pwprompt odoo17_user
```

```
ALTER USER odoo17_user WITH SUPERUSER
```

```
ALTER USER
```

### Konfigürasyonları Ayarlayalım:

![image](https://github.com/furkanyalcindag/comitfy-kolaysis/assets/106275189/37aae1cf-db76-472e-8c3b-db4fd3b27101)

Projemizi localhost:8069 Adresinden Başlatarak Geliştirmeye Başlayalım.


# Kolaysis ile Windows'da Çalışmaya Başlama

Standart bir Windows kurulumu için aşağıdaki adımları izleyebilirsiniz.

### Python'u bilgisayarınıza kurun.

<a href="https://www.python.org/downloads/release/python-3100/">Buradan</a> Python'un 3.10 versiyonunu indirip installer ile kuruluma başlayın.

![image](https://github.com/furkanyalcindag/comitfy-kolaysis/assets/20794065/293a9e6e-8156-4eb5-b503-20e8ff661872)


Burada bütün seçenekleri seçin, ardından kuruluma devam edin.Kurulum tamamlandıktan sonra ```python --version``` ve ```pip --version``` yazarak kurulumun tamamlandığından emin olun.

### PostgreSQL'i bilgisayarınıza kurun.

<a href="https://www.enterprisedb.com/downloads/postgres-postgresql-downloads">Buradan</a> PostgreSQL'in 12 veya daha üstü bir sürümü indirip installer ile kuruluma başlayın. Kurulum tamamlandıktan sonra denetim masasından Gelişmiş sistem ayarlarını açın ve ortam değişkenlerinden, sistem değişkenlerinde bulunan `PATH`'i seçip düzenle diyin. Düzenleme ekranı açıldığında yeni diyip PostgreSQL klasörünün içindeki bin'in yolunu path'e ekleyin.(Varsayılan olarak bu yol şu şekildedir:`C:\Program Files\PostgreSQL\<PostgreSQL versiyonu>\bin`)

Varsayılan olarak PostgreSQL'de gelen kullanıcı postgres'dir. Yeni bir kullanıcı ekleyin, bunun için şu adımları takip edin;
-1- pgAdmin'i açın ve Servers'a çift tıklayın.
- PostgreSQL<versiyonunuz> 'a tıklayın ve yukarıda bulunan araç çubuğundan Object sekmesine gelin.
- Burada Create'e basıp Login/Group Role'e tıklayın.
- Açılan General sekmesinde bulunan name kısmına yeni kullanıcı adınızı girin. (örnek;`kolaysis`)
- Definition sekmesini açın ve kullanmak istediğiniz şifrenizi girin. (örnek;`kolaysis`)
- Privileges sekmesini açın, Can Login? ve Superuser? bunlarnı aktifleştirin. Ardından sağ alttan kaydedin.

### Dependency'leri yükleme
Dependencies yani projenin bağımlılıklarını yüklemeden önce <a href="https://visualstudio.microsoft.com/visual-cpp-build-tools/">buradan</a> C++ build tools'u indirin ve kurun.

C++ build tools kurulduktan sonra yönetici olarak çalıştırılan konsoldan projenin dizinine gidin ve `pip install setuptools wheel` ile `pip install -r requirements.txt` komutlarını sırasıyla çalıştırın.

### wkhtmltopdf
> [!IMPORTANT]
>`wkhtmltopdf` pip ile yüklenmiyor, bundan dolayı <a href="https://wkhtmltopdf.org/downloads.html">buradan</a> wkhtmltopdf'i indirin urulum tamamlandıktan sonra denetim masasından Gelişmiş sistem ayarlarını açın ve ortam değişkenlerinden, sistem değişkenlerinde bulunan `PATH`'i seçip düzenle diyin. Düzenleme ekranı açıldığında yeni diyip wkhtmltopdf klasörünün içindeki bin'in yolunu path'e ekleyin.(Varsayılan olarak bu yol şu şekildedir:`C:\Program Files\wkhtmltopdf\bin`) 

### Config dosyasını hazırlama
Projenin klasörünün içinde yer alan `odoo.conf` dosyasını açın, içerisinde yer alan `addons_path`'i projenin mevcut yoluna göre düzenleyin örneğin;
```
[options]
addons_path = C:\Users\osman\Desktop\comitfy-workspace\comitfy-kolaysis\addons,
              C:\Users\osman\Desktop\comitfy-workspace\comitfy-kolaysis\odoo\addons,
              C:\Users\osman\Desktop\comitfy-workspace\comitfy-kolaysis\odoo\custom_addons,
db_user = kolaysis
db_password = kolaysis
```
### Konfigürasyonları Ayarlayalım:

![image](https://github.com/furkanyalcindag/comitfy-kolaysis/assets/20794065/c22211f1-0309-45f0-88b7-fdb5aa3b79e9)

Projemizi localhost:8069 Adresinden Başlatarak Geliştirmeye Başlayalım.
