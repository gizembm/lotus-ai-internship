# Pandas & SQL Uygulamaları (100 Soru)

Bu çalışma, **Lotus AI staj sürecinde** verilen bir görev kapsamında hazırlanmıştır.  
Amaç; **SQL ile yazılmış sorguların, Python Pandas kütüphanesi kullanılarak birebir karşılıklarının üretilmesi** ve iki yaklaşımın sonuçlarının karşılaştırılmasıdır.

---

## 📌 Görev Tanımı

Elimizde **film kiralama sistemine ait bir SQLite veritabanı** bulunmaktadır.  
Bu veritabanı üzerinde hazırlanmış **100 adet SQL sorusu**, aşağıdaki kurallar çerçevesinde Pandas kullanılarak çözülmüştür:

- Her soru için önce **SQL sorgusu analiz edilmiştir**
- Aynı mantık **Pandas DataFrame işlemleriyle** yeniden uygulanmıştır
- **SQL çıktısı ile Pandas çıktısı birebir karşılaştırılmıştır**
- Analiz sürecinde **yalnızca gerekli tablolar veritabanından çekilmiştir**

---

## ⚙️ Kullanılan Kurallar ve Kısıtlar

Bu çalışma sırasında aşağıdaki kurallara **özellikle dikkat edilmiştir**:

- `read_sql_query` **sadece tabloyu çekmek için** kullanılmıştır  
- Sorgular **doğrudan SQL çalıştırılarak çözülmemiştir**
- Join, groupby, aggregation gibi işlemler **tamamen Pandas ile yapılmıştır**
- Her sorunun çözümünde:
  - SQL sorgusu
  - Pandas karşılığı
  - Çıktı karşılaştırması
  birlikte sunulmuştur

---

## 🗂️ Veri Seti Hakkında

Kullanılan veritabanı, aşağıdaki tabloları içeren bir **SQLite Film Kiralama Veritabanıdır**:

- Film
- Actor
- Customer
- Rental
- Inventory
- Payment
- Category
- Store
- Staff
- Address / City / Country

Bu yapı sayesinde:
- Çok tablolu ilişkiler
- Join işlemleri
- Zaman, gelir ve müşteri bazlı analizler
gerçekçi bir senaryo üzerinden uygulanmıştır.

---

## 🧠 Çözülen Problem Türleri

Bu çalışma kapsamında toplam **100 farklı analitik soru** çözülmüştür.  
Sorular aşağıdaki başlıklarda yoğunlaşmaktadır:

- Film ve kategori bazlı analizler
- Müşteri davranışları (kiralama sayısı, harcama miktarı)
- Gelir ve performans analizleri
- Zaman bazlı kiralama ve iade analizleri
- Çalışan ve mağaza performans karşılaştırmaları
- En çok / en az kiralanan içerikler

---

## 🛠️ Kullanılan Teknolojiler

- **Python**
- **Pandas**
- **SQLite**
- **Jupyter Notebook**



