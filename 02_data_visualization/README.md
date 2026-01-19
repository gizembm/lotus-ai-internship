# Veri Görselleştirme Çalışmaları

Bu çalışma, **Lotus AI staj süreci** kapsamında veri görselleştirme tekniklerini hem **Python** hem de **KNIME Analytics Platform** kullanarak uygulamak amacıyla hazırlanmıştır.

Çalışmanın temel hedefi; **veri yapısına uygun grafik türlerini bilinçli bir şekilde seçmek**, bu grafiklerin **avantaj ve dezavantajlarını analiz etmek** ve elde edilen sonuçları yorumlamaktır.

---

## 📌 Çalışmanın Amacı

- Veri görselleştirme kütüphanelerini tanımak ve karşılaştırmak  
- Grafik türlerinin hangi veri yapıları için uygun olduğunu öğrenmek  
- Aynı analizleri **kod tabanlı (Python)** ve **görsel tabanlı (KNIME)** araçlarla gerçekleştirmek  
- Görselleştirme üzerinden **analitik çıkarımlar yapabilmek**

---

## 🧰 Kullanılan Kütüphaneler ve Araçlar

### Python Kütüphaneleri
- **Matplotlib** – Detaylı ve özelleştirilebilir grafikler
- **Seaborn** – İstatistiksel ve estetik görselleştirmeler
- **Plotly** – Etkileşimli (interactive) grafikler

### Görsel Analiz Aracı
- **KNIME Analytics Platform**

---

## 📊 İncelenen Grafik Türleri

Bu çalışma kapsamında aşağıdaki grafik türleri veri yapısına göre seçilerek kullanılmıştır:

- **Box Plot** – Dağılım, medyan ve aykırı değer analizi
- **Violin Plot** – Dağılım ve yoğunluk yapısının birlikte incelenmesi
- **Bar Chart** – Kategorik verilerin karşılaştırılması
- **Pie Chart** – Parça–bütün ilişkilerinin gösterilmesi
- **Histogram** – Sayısal verilerin frekans dağılımı
- **Line Chart** – Zaman serisi verilerinde trend analizi

> Not: Zaman serisi içermeyen veri setlerinde **Line Chart bilinçli olarak kullanılmamıştır.**

---

## 🗂️ Kullanılan Veri Setleri

### 1️⃣ Students Performance in Exams
- Öğrencilerin sınav notları ve demografik bilgilerini içeren **kesitsel (cross-sectional)** veri seti
- Kullanım amacı:
  - Not dağılımlarını incelemek
  - Cinsiyet ve ebeveyn eğitim durumu gibi kategorik değişkenlerle karşılaştırmalar yapmak

Bu veri setinde:
- Box Plot
- Violin Plot
- Bar Chart
- Pie Chart
- Histogram  
grafikleri kullanılmıştır.

---

### 2️⃣ Monthly CSV (Zaman Serisi Veri Seti)
- Aylık ortalama sıcaklık anomalilerini içeren **zaman serisi** veri seti
- Kullanım amacı:
  - Zaman içerisindeki değişimleri ve trendleri analiz etmek
  - Farklı veri kaynaklarını karşılaştırmak

Bu veri setinde:
- Line Chart
- Bar Chart
- Box Plot
- Violin Plot
- Pie Chart  
grafikleri uygulanmıştır.

---

## 🔄 Python ve KNIME Karşılaştırması

Aynı veri setleri ve benzer grafik türleri:

- **Python (Jupyter Notebook)** ortamında kod yazarak
- **KNIME Analytics Platform** üzerinde node tabanlı olarak

oluşturulmuş ve sonuçlar karşılaştırılmıştır.

Bu sayede:
- Kod tabanlı ve görsel tabanlı analiz yaklaşımları arasındaki farklar
- Her iki aracın güçlü ve sınırlı yönleri
net bir şekilde gözlemlenmiştir.

---
## 🎯 Kazanımlar

Bu çalışma sayesinde:

- Veri yapısına uygun görselleştirme seçimi yapabilme becerisi kazandım
- Grafiklerin sadece görsel değil, **analitik bir araç** olduğunu öğrendim
- Python ve KNIME ile veri görselleştirme süreçlerini karşılaştırmalı olarak deneyimledim
- Görselleştirme üzerinden anlamlı yorumlar ve çıkarımlar yapma yetkinliğimi geliştirdim

---

## 📝 Not

Bu çalışma **Lotus AI staj sürecinin** bir parçası olarak hazırlanmıştır ve  
eğitim & yetkinlik geliştirme amacı taşımaktadır.
