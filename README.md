# scraping-extractor

Alat praktis untuk ekstraksi data dari website menggunakan CSS selector. Tinggal input URL dan selector yang mau di-scrape, langsung jadi!

## Fitur

- 🚀 Input interaktif via terminal
- 🎯 Support semua HTML tag (div, article, section, span, dll)
- 🔍 Ekstraksi berdasarkan class name
- 💾 Opsi simpan hasil ke file .txt
- 📊 Penomoran otomatis per data
- ⚡ Error handling lengkap

## Requirement

```bash
pip install requests beautifulsoup4
```

## Cara Pakai

1. **Jalankan program:**
```bash
python extractor.py
```

2. **Input data yang diminta:**
```
Masukkan URL website: https://quotes.toscrape.com/
Masukkan tag HTML: div
Masukkan nama class dari <div>: quote
Simpan hasil ke file? (y/n): y
Nama file: hasil.txt
```

3. **Selesai!** Data akan ditampilkan di terminal dan/atau disimpan ke file.

## Contoh Penggunaan

### 1. Ekstrak Quotes dari quotes.toscrape.com
```
URL: https://quotes.toscrape.com/
Tag: div
Class: quote
```

### 2. Ekstrak Artikel dari Blog
```
URL: https://example-blog.com
Tag: article
Class: post
```

### 3. Ekstrak Product Card dari E-commerce
```
URL: https://example-shop.com
Tag: div
Class: product-card
```

### 4. Ekstrak Semua Div (tanpa class spesifik)
```
URL: https://example.com
Tag: div
Class: (kosongkan)
```

## Cara Cari CSS Selector

### Method 1: Inspect Element (Chrome/Firefox)
1. Klik kanan pada elemen yang mau di-scrape
2. Pilih **Inspect** atau **Inspect Element**
3. Lihat tag HTML dan class name-nya
   ```html
   <div class="quote">...</div>
   ```
   - Tag: `div`
   - Class: `quote`

### Method 2: Developer Tools
1. Tekan `F12` atau `Ctrl+Shift+I`
2. Klik icon **Select Element** (panah/pointer)
3. Hover ke elemen yang mau di-scrape
4. Lihat highlight di DevTools untuk tahu tag dan class-nya

### Method 3: View Source
1. Klik kanan > **View Page Source**
2. Tekan `Ctrl+F` untuk search
3. Cari pola yang berulang (biasanya punya class yang sama)

## Tips & Trik

### ✅ DO's
- Pastikan URL lengkap dengan `https://`
- Gunakan class yang spesifik dan unik
- Test dulu dengan website yang simple
- Perhatikan struktur HTML yang berulang

### ❌ DON'Ts
- Jangan scrape website yang melarang scraping (cek robots.txt)
- Jangan spam request terlalu cepat (bisa kena ban)
- Jangan scrape data pribadi/sensitif

## Troubleshooting

### Error: "URL tidak boleh kosong!"
- Pastikan input URL lengkap, contoh: `https://example.com`

### Error: "Ditemukan: 0 data"
- Cek kembali tag dan class name-nya
- Buka DevTools dan pastikan selector benar
- Mungkin website pakai JavaScript rendering (butuh Selenium)

### Error: "Connection Error"
- Cek koneksi internet
- Pastikan URL bisa diakses di browser
- Website mungkin blok bot/scraper

## Format Output

### Di Terminal:
```
[1]
<div class="quote">
    <span class="text">"The world as we have created it..."</span>
    <span>by <small>Albert Einstein</small></span>
</div>
--------------------------------------------------------------------------------

[2]
<div class="quote">
    ...
</div>
--------------------------------------------------------------------------------
```

### Di File (hasil.txt):
```
URL: https://quotes.toscrape.com/
Tag: <div> Class: quote
Total: 10 data
================================================================================

[1]
<div class="quote">...</div>
--------------------------------------------------------------------------------

[2]
<div class="quote">...</div>
--------------------------------------------------------------------------------
```

## Advanced: Pakai Langsung di Code

```python
from extractor import extract_data

# Ekstrak data
results = extract_data(
    url="https://quotes.toscrape.com/",
    tag="div",
    class_name="quote",
    show_content=True,
    save_to_file=True,
    filename="output.txt"
)

# Proses hasil
for data in results:
    print(data.get_text())
```

## Struktur Project

```
scraping/
├── extractor.py          # Main program
├── README.md            # Dokumentasi ini
├── latihan5.py          # File latihan original
└── hasil_ekstraksi.txt  # Output file (jika disimpan)
```

## Lisensi

Free to use. Happy scraping! 🚀

## Author

Dibuat untuk memudahkan ekstraksi data dari website dengan cara yang simple dan praktis.

---

**Note:** Selalu respect robots.txt dan terms of service dari website yang di-scrape!
