# Comitfy-Kolaysis

# Kolaysis

Kolaysis, web tabanlı iş uygulamalarından oluşan bir pakettir.
Ana Kolaysis Uygulamaları arasında CRM, Proje Yönetimi, Faturalama ve Muhasebe, Satış Noktası, İnsan Kaynakları, Pazarlama, Üretim, Satın Alma Yönetimi... bulunmaktadır.
Kolaysis Uygulamaları bağımsız uygulamalar olarak kullanılabilir, ancak aynı zamanda sorunsuz bir şekilde entegre olurlar, böylece birkaç Uygulama yüklediğinizde tam özellikli bir Açık Kaynak ERP elde edebilirsiniz.

# Kolaysis ile çalışmaya başla

Standar bir ubuntu ile kurulum için.

Terminalize açın ve kuruluma başlayın

### Pyhton yükleyerek işe başlayalım:

`sudo apt install python3-pip`

Yüklemeyi doğrulamak için aşağıdaki komutu çalıştırın:

`pip3 --version`

### PostgreSQL yükleyelim:

Dosya deposu yapılandırmasını oluşturun:

`sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'`

Depo imzalama anahtarını içe aktarın:

`wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -`

Paket listelerini güncelleyin:

`sudo apt-get update`

 PostgreSQL'in en son sürümünü yükleyin.
 Belirli bir sürüm istiyorsanız, 'postgresql' yerine 'postgresql-12' veya benzerini kullanın:

 `sudo apt-get -y install postgresql`

 ### PgAdmin 4 yüklemeyle devam edelim:

Depo için ortak anahtarı yükleyin (daha önce yapılmadıysa):

`curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg`

Depo yapılandırma dosyasını oluşturun:

`sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'`

pgAdmini yükleyin:

`sudo apt install pgadmin4-web`

Eğer pgadmin4-web yüklediyseniz, web sunucusunu yapılandırın:

`sudo /usr/pgadmin4/bin/setup-web.sh`

Projeyi bilgisayarımıza klonlayalım:

`git clone https://github.com/furkanyalcindag/comitfy-kolaysis.git --depth 1 --branch main --single-branch Comitfy-Kolaysis`

Projeyi başarılı bir şekilde klonladıktan sonra projenin dizinine gidelim ve aşağıdaki komutu çalıştıralım:

`pip3 install -r requirements.txt`

### Projemizdeki gereksinimleri yükledikten sonra veritabanın da kullanıcı ve veritabanı oluşturalım:

`sudo su - postgres`

`create user --createdb --username postgres --no-createrole -no-superuser --pwprompt kolaysis_user`

`ALTER USER kolaysis_user WITH SUPERUSER`

`ALTER USER`


