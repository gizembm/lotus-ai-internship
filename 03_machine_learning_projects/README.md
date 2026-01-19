# Makine Öğrenmesi Projeleri

Bu klasör, **Lotus AI staj süreci** kapsamında gerçekleştirilen ve farklı veri setleri üzerinde
**makine öğrenmesi problemlerini uçtan uca ele alan** çalışmaları içermektedir.

Çalışmalar; veri ön işleme, özellik mühendisliği, modelleme, performans değerlendirme ve
sonuçların yorumlanması adımlarını kapsamaktadır. Analizler ağırlıklı olarak
**KNIME Analytics Platform** üzerinde gerçekleştirilmiş, bazı problemler **Python (Jupyter Notebook)** ortamında tekrar edilerek karşılaştırmalı analiz yapılmıştır.

---

## 📌 Proje Kapsamı

Bu klasör altında **5 farklı makine öğrenmesi problemi** yer almaktadır:

1. **Food Delivery – Regresyon**
2. **Health Insurance – Regresyon**
3. **Uber Trips – Zaman Serisi Tabanlı Regresyon**
4. **Credit Card Clustering – Gözetimsiz Öğrenme**
5. **YouTube Spam Yorum Tespiti – Metin Sınıflandırma**

Her problem gerçek hayata yakın veri setleri kullanılarak çözülmüş ve sonuçlar ayrıntılı şekilde raporlanmıştır.

---

## 1️⃣ Food Delivery – Teslimat Süresi Tahmini (Regresyon)

**Amaç:**  
Sipariş ve teslimat sürecine ait özellikler kullanılarak **teslimat süresinin tahmin edilmesi**.

**Kullanılan Yaklaşım:**
- Veri ön işleme (eksik değer giderme, kategorik değişken dönüşümü)
- KNIME AutoML (Regression)
- RMSE metriği ile model karşılaştırması

**Sonuç:**
- En başarılı model: **H2O Generalized Linear Model**
- Veri setindeki ilişkilerin büyük ölçüde **doğrusal** olduğu gözlemlenmiştir.
- Python ortamında elde edilen **Linear Regression** sonuçları ile KNIME çıktıları tutarlıdır.

---

## 2️⃣ Health Insurance – Sigorta Maliyeti Tahmini (Regresyon)

**Amaç:**  
Bireylerin demografik ve sağlık bilgilerine göre **yıllık sigorta maliyetinin (charges)** tahmin edilmesi.

**Öne Çıkan Adımlar:**
- Feature Engineering (BMI kategorisi, yaş grupları)
- KNIME AutoML ile model karşılaştırması
- Python (scikit-learn) ile yeniden modelleme

**Sonuç:**
- En başarılı model: **Gradient Boosted Trees**
- Veri yapısının **doğrusal olmayan ve karmaşık** olduğu belirlenmiştir.
- Boosting tabanlı modeller doğrusal modellere göre daha başarılıdır.

---

## 3️⃣ Uber Trips – Saatlik Yolculuk Talebi Tahmini

**Amaç:**  
Uber yolculuk verileri kullanılarak **saatlik yolculuk sayısının tahmin edilmesi**.

**Öne Çıkan İşlemler:**
- Tarih-saat dönüşümleri
- Zaman tabanlı özellik çıkarımı (gün, saat, hafta günü)
- Saatlik talep değişkeninin oluşturulması

**Sonuç:**
- KNIME: **XGBoost Tree Ensemble**
- Python: **Random Forest**
- Talep yapısının **zamana bağlı ve doğrusal olmayan** bir karaktere sahip olduğu gözlemlenmiştir.

---

## 4️⃣ Credit Card Clustering – Müşteri Segmentasyonu

**Amaç:**  
Kredi kartı kullanıcılarını harcama ve kullanım davranışlarına göre **segmentlere ayırmak**.

**Yöntem:**
- Z-score normalizasyon
- **K-Means kümeleme (k = 4)**
- Box plot ve PCA ile görsel analiz

**Sonuç:**
- Matematiksel ayrışma sınırlı olsa da
- Elde edilen kümeler **davranışsal olarak anlamlı müşteri segmentleri** sunmaktadır.
- Python ve KNIME sonuçları tutarlıdır.

---

## 5️⃣ YouTube Spam Yorum Tespiti – Metin Sınıflandırma

**Amaç:**  
YouTube yorumlarının **spam / spam değil** olarak sınıflandırılması.

**Uygulanan Adımlar:**
- Metin ön işleme
- TF-IDF tabanlı özellik çıkarımı
- Naive Bayes ve Logistic Regression modelleri

**Sonuç:**
- KNIME ortamında sınırlı performans
- Python ortamında Logistic Regression ile daha yüksek doğruluk
- Metin sınıflandırmada model ve özellik seçiminin kritik olduğu görülmüştür

---

## 🧰 Kullanılan Teknolojiler

- **KNIME Analytics Platform**
- **Python**
  - pandas
  - scikit-learn
  - matplotlib / seaborn
- **AutoML**
- **TF-IDF, One-Hot Encoding**
- **RMSE, Confusion Matrix, Silhouette Score**

---

## 🎯 Kazanımlar

Bu çalışmalar sayesinde:

- Regresyon, sınıflandırma ve kümeleme problemlerini uçtan uca ele aldım
- AutoML ve manuel modelleme yaklaşımlarını karşılaştırdım
- Gerçek veri setleri üzerinde analitik yorumlama becerisi kazandım
- KNIME ve Python ortamlarını birlikte kullanma deneyimi edindim

---

## 📝 Not

Bu projeler **Lotus AI staj sürecinin** bir parçası olarak,
eğitim ve yetkinlik geliştirme amacıyla hazırlanmıştır.


