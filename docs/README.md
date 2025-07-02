# Teknoloji Sınavı Rehberi PDF Oluşturucu

Bu proje, Markdown formatındaki teknoloji sınavı rehberini professional PDF formatına dönüştüren kapsamlı bir sistemdir.

## 📋 Özellikler

- ✅ **Türkçe Karakter Desteği**: Tam UTF-8 destekli, Türkçe karakterler sorunsuz işlenir
- ✅ **Professional Layout**: A4 format, uygun margin değerleri, okunabilir font boyutu
- ✅ **İçindekiler Tablosu**: Otomatik oluşturulan, clickable navigation
- ✅ **Sayfa Numaraları**: Alt merkezde otomatik sayfa numarası
- ✅ **Başlık Hiyerarşisi**: 4 seviye başlık desteği, renkli ve organize
- ✅ **Sınav Soruları Bölümü**: 6 detaylı sınav sorusu, cevap anahtarları, puanlama sistemi
- ✅ **Konu Kapsamı**: 12 ana teknoloji konusu detaylı olarak işlenmiş

## 📁 Dosya Yapısı

```
/docs/
├── teknoloji_sinav_rehberi.md    # Ana içerik (Markdown format)
├── generate_pdf.py               # PDF oluşturucu script
├── requirements.txt              # Python bağımlılıkları
├── test_pdf_system.py           # Test ve doğrulama scripti
├── README.md                    # Bu dosya
└── output/
    └── Teknoloji_Sinav_Rehberi.pdf  # Oluşturulan PDF
```

## 🚀 Kurulum ve Kullanım

### 1. Bağımlılıkları Yükle

```bash
pip install -r requirements.txt
```

### 2. PDF Oluştur

```bash
python generate_pdf.py
```

### 3. Sistemi Test Et

```bash
python test_pdf_system.py
```

## 📖 İçerik Kapsamı

### Ana Konular

1. **IoT ve Siber Güvenlik**
   - DoS/DDoS saldırıları
   - Güvenlik zayıflıkları
   - Kimlik doğrulama

2. **Bilişim Paradigmaları**
   - Cloud Computing
   - Fog Computing
   - Edge Computing

3. **Edge Intelligence ve Endüstri 4.0**
   - Cyber-Physical Systems
   - Smart Manufacturing
   - Predictive Maintenance

4. **CEI Sürekliliği ve 5G**
   - Computing-Edge-Intelligence Continuum
   - Network Slicing
   - Ultra-Reliable Low-Latency Communication

5. **Akıllı Tarım Uygulamaları**
   - Precision Agriculture
   - IoT Sensor Networks
   - AI/ML in Agriculture

6. **Siber Güvenlik ve Bilgi Güvenliği**
   - CIA Triad
   - Modern Güvenlik Tehditleri
   - Güvenlik Çerçeveleri

7. **Makine Öğrenmesi ve Siber Güvenlik**
   - AI/ML in Cybersecurity
   - Adversarial Machine Learning
   - Threat Detection

8. **Yüksek Performanslı Hesaplama**
   - HPC Architecture
   - Parallel Computing
   - Scientific Computing

9. **Dijital İkiz Teknolojisi**
   - Digital Twin Fundamentals
   - Implementation Challenges
   - Industry Applications

10. **Blockchain ve Yeşil Enerji**
    - Green Blockchain Initiatives
    - Renewable Energy Trading
    - Carbon Credits

11. **Yeşil İletişim ve Bilişim**
    - Green Computing Principles
    - Energy-Efficient Networks
    - Sustainable IT

12. **Yüksek İrtifa Platform Veri Merkezleri**
    - High Altitude Platform Systems
    - Distributed Computing
    - Rural Connectivity

### Sınav Bölümü

- **6 Detaylı Soru**: Her biri farklı konuları kapsayan kapsamlı problemler
- **Cevap Anahtarları**: Detaylı değerlendirme kriterleri
- **Puanlama Sistemi**: 100 puan üzerinden değerlendirme
- **Sınav İpuçları**: Başarılı sınav stratejileri

## 🔧 Teknik Özellikler

### PDF Özellikleri

- **Format**: A4 (210 x 297 mm)
- **Margin**: 2.5cm üst/alt, 2cm sağ/sol
- **Font**: Segoe UI (Türkçe karakter desteği)
- **Font Boyutu**: 11pt ana metin, çeşitli başlık boyutları
- **Satır Aralığı**: 1.6 (okunabilirlik için optimize)

### Renkler

- **Ana Başlık**: #1f4e79 (Koyu mavi)
- **Alt Başlık**: #4472c4 (Orta mavi)
- **Vurgu**: #5b9bd5 (Açık mavi)
- **Accent**: #70ad47 (Yeşil)

### Yazılım Bağımlılıkları

- `weasyprint==62.3`: PDF rendering engine
- `markdown==3.6`: Markdown processing
- `python-markdown-math==0.8`: Mathematical expressions
- `pymdown-extensions==10.7.1`: Advanced Markdown features

## 🧪 Test Sistemi

`test_pdf_system.py` scripti aşağıdaki testleri çalıştırır:

1. **Bağımlılık Kontrolü**: Gerekli Python paketlerinin varlığı
2. **Dosya Varlığı**: Kaynak dosyaların kontrolü
3. **PDF Oluşturma**: Başarılı PDF generation
4. **İçerik Doğrulama**: PDF kalite kontrolü

## 📊 Performans

- **İşlem Süresi**: ~2-3 saniye
- **PDF Boyutu**: ~170-180 KB
- **Sayfa Sayısı**: ~40-50 sayfa
- **Bellek Kullanımı**: <100 MB

## 🔍 Sorun Giderme

### Yaygın Hatalar

1. **Font Hataları**: 
   - Sistem fontlarının eksikliği
   - Çözüm: Segoe UI fontunun sistem üzerinde bulunması

2. **Encoding Hataları**:
   - UTF-8 encoding sorunları
   - Çözüm: Dosyaların UTF-8 encoding ile kaydedilmesi

3. **Memory Hataları**:
   - Büyük dosyalar için bellek yetersizliği
   - Çözüm: İçerik bölümlerini küçültmek

### Log Kontrolü

Script çalışırken detaylı log mesajları üretir:

```bash
python generate_pdf.py 2>&1 | grep -E "(INFO|ERROR|WARNING)"
```

## 🚀 Geliştirme

### Yeni İçerik Ekleme

1. `teknoloji_sinav_rehberi.md` dosyasını düzenle
2. Markdown syntax kullan
3. PDF'i yeniden oluştur

### CSS Stillerini Değiştirme

`generate_pdf.py` içindeki `get_css_styles()` metodunu düzenle:

```python
def get_css_styles(self):
    css = """
    /* Kendi CSS stillerinizi buraya ekleyin */
    """
    return css
```

## 📝 Lisans

Bu proje eğitim amaçlı hazırlanmıştır. İçerik güncel teknoloji trendleri ve endüstri standartları dikkate alınarak oluşturulmuştur.

## 🤝 Katkıda Bulunma

1. Yeni teknoloji konuları eklemek
2. Sınav sorularını güncellemek
3. PDF formatını iyileştirmek
4. Test kapsamını genişletmek

## 📞 Destek

Herhangi bir sorun yaşarsanız:

1. `test_pdf_system.py` ile sistem durumunu kontrol edin
2. Log mesajlarını inceleyin
3. Hata raporunu paylaşın

---

*Son güncelleme: Temmuz 2025*
*Versiyon: 1.0.0*