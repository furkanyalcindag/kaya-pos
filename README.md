
![](https://github.com/furkanyalcindag/comitfy-kolaysis/blob/main/addons/web/static/img/kolaysisLogo.png)

Kolaysis, web tabanlı iş uygulamalarından oluşan bir pakettir. Ana Kolaysis Uygulamaları arasında CRM, Proje Yönetimi, Faturalama ve Muhasebe, Satış Noktası, İnsan Kaynakları, Pazarlama, Üretim, Satın Alma Yönetimi bulunmaktadır. Kolaysis Uygulamaları bağımsız uygulamalar olarak kullanılabilir, ancak aynı zamanda sorunsuz bir şekilde entegre olurlar, böylece birkaç uygulama yüklediğinizde tam özellikli bir Açık Kaynak ERP elde edebilirsiniz.

# Kolaysis ile Çalışmaya Başlama

Standart bir Ubuntu kurulumu için aşağıdaki adımları izleyebilirsiniz.

Terminal'i açın ve kurulumu başlatın.

### Python Yükleyerek İşe Başlayalım:

`sudo apt install python3-pip`

Yüklemeyi doğrulamak için aşağıdaki komutu çalıştırın:

`pip3 --version`

### PostgreSQL Yükleyelim:

Dosya deposu yapılandırmasını oluşturun:

`sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'`

Depo imzalama anahtarını içe aktarın:

`wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -`

Paket listelerini güncelleyin:

`sudo apt-get update`

 PostgreSQL'in en son sürümünü yükleyin. Belirli bir sürüm istiyorsanız, 'postgresql' yerine 'postgresql-12' veya benzerini kullanın:

 `sudo apt-get -y install postgresql`

 ### PgAdmin 4 Yüklemeyle Devam Edelim:

Depo için ortak anahtarı yükleyin (daha önce yapılmadıysa):

`curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg`

Depo yapılandırma dosyasını oluşturun:

`sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'`

pgAdmin'i yükleyin:

`sudo apt install pgadmin4-web`

Eğer pgadmin4-web yüklediyseniz, web sunucusunu yapılandırın:

`sudo /usr/pgadmin4/bin/setup-web.sh`

Projeyi bilgisayarımıza klonlayalım:

`git clone https://github.com/furkanyalcindag/comitfy-kolaysis.git --depth 1 --branch main --single-branch Comitfy-Kolaysis`

Projeyi başarılı bir şekilde klonladıktan sonra projenin dizinine gidip aşağıdaki komutu çalıştıralım:

`pip3 install -r requirements.txt`

### Projemizdeki Gereksinimleri Yükledikten Sonra Veritabanında Kullanıcı ve Veritabanı Oluşturalım:

`sudo su - postgres`

`create user --createdb --username postgres --no-createrole -no-superuser --pwprompt kolaysis_user`

`ALTER USER kolaysis_user WITH SUPERUSER`

`ALTER USER`

# Konfigürasyonları Ayarlayalım:

![image](https://github.com/furkanyalcindag/comitfy-kolaysis/assets/106275189/37aae1cf-db76-472e-8c3b-db4fd3b27101)

Projemizi localhost:8069 Adresinden Başlatarak Geliştirmeye Başlayalım.




