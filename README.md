# gramedia-generate-link-search

Tools ini di gunakan untuk melakukan pencarian produk affiliate dan otomatis klik button generate link affiliate dari [affiliate gramedia](https://aff.gramedia.com/s/MrHMDcJDbt).

Tools ini sama dengan [gramedia-generate-link](https://github.com/1amkaizen/gramedia-generate-link/),tapi ini mengguakan pencarian untuk generate link produknya agar lebih spesifik.
### persiapan
Sebelum menjalankan kodenya harus export dulu email dan password untuk login ke [affiliate gramedia](https://aff.gramedia.com/s/MrHMDcJDbt) nya

```bash
export EMAIL="youremail@gmail.com"
export PASSWORD="yourpassword"
```

### cara menggunakan

```bash
python3 main.py -q "judul buku"
```
Contoh

```bash
python3 main.py -q "arduino"
```

flag `-q` ini untuk mengatur query dalam pencarian

jika seperti ini berarti berhasil login

```bash
Opened login page.
Entered email and password.
Clicked login button.
Login successful, current URL: https://affiliate.gramedia.com/dashboard
```

Tampilannya akan seperti ini

```bash
Opened login page.
Entered email and password.
Clicked login button.
Login successful, current URL: https://affiliate.gramedia.com/dashboard
Opened product URL: https://affiliate.gramedia.com/content/products/from-zero-to-a-pro-arduinocd-edisi-revisi
Clicked on 'Generate Link' button.
Generated affiliate link: https://aff.gramedia.com/s/QDWZxeHnxS
Opened product URL: https://affiliate.gramedia.com/content/products/19-jam-belajar-cepat-arduino-cd-edisi-revisi
Clicked on 'Generate Link' button.
Generated affiliate link: https://aff.gramedia.com/s/mNzMMGJCvy
Opened product URL: https://affiliate.gramedia.com/content/products/aplikasi-arduino-dan-sensor
Clicked on 'Generate Link' button.
Generated affiliate link: https://aff.gramedia.com/s/mpJfPDgRgH
Opened product URL: https://affiliate.gramedia.com/content/products/arduino-itu-mudah-cd
Clicked on 'Generate Link' button.
Generated affiliate link: https://aff.gramedia.com/s/QnSlQRPkfZ
Opened product URL: https://affiliate.gramedia.com/content/products/pengantar-mikrokontroler-aplikasi-pada-arduino
Generate button not found or already clicked.
Timeout waiting for element on https://affiliate.gramedia.com/content/products/pengantar-mikrokontroler-aplikasi-pada-arduino
Opened product URL: https://affiliate.gramedia.com/content/products/pengantar-elektronika-instrumentas-pendekatan-project-arduino-androidi
Clicked on 'Generate Link' button.

```
