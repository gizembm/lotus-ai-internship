# Derin Takviyeli Öğrenme – Snake AI (DQN)

Bu proje, **Lotus AI staj süreci** kapsamında Derin Takviyeli Öğrenme (Deep Reinforcement Learning – DRL)
alanında edinilen teorik bilgilerin **uygulamaya dökülmesi** amacıyla geliştirilmiştir.

Proje kapsamında, klasik **Snake oyunu** Python dili kullanılarak modellenmiş ve
oyunu oynayabilen bir **Deep Q-Network (DQN)** ajanı sıfırdan eğitilmiştir.

---

## 🎯 Projenin Amacı

- Takviyeli öğrenmenin temel prensiplerini uygulamalı olarak kavramak
- Ayrık eylem uzayına sahip bir oyun ortamında DQN algoritmasını uygulamak
- Bir ajanın **deneme–yanılma yoluyla davranış öğrenmesini** gözlemlemek
- Ödül fonksiyonu ve keşif–sömürü (exploration–exploitation) dengesinin etkisini analiz etmek

---

## 🧠 Kullanılan Yaklaşım: Deep Q-Network (DQN)

Snake oyunu için **DQN algoritması** tercih edilmiştir çünkü:

- Eylem uzayı **sınırlı ve ayrık** yapıdadır (ileri, sağa dön, sola dön)
- Durum uzayı tablo tabanlı yöntemler için **çok büyüktür**
- Ödül yapısı **seyrek ve gecikmeli** olduğundan Q-değer tabanlı yöntemler uygundur
- DQN, literatürde oyun tabanlı problemlerde başarısı kanıtlanmış bir yöntemdir

Bu proje, DQN’in temel bileşenlerini sade ve anlaşılır bir yapı ile içermektedir.

---

## 🧩 Kod Yapısı ve Mantığı

### `game.py` – Oyun Ortamı
- Snake oyununun tüm kuralları bu dosyada tanımlanmıştır
- Çevre (environment):
  - Yılanın hareketi
  - Yem yerleştirme
  - Çarpışma kontrolü
  - Ödül ve ceza mekanizması
- Ajan ile etkileşim `play_step()` fonksiyonu üzerinden sağlanır

---

### `agent.py` – DQN Ajanı
- Ajanın **durum temsili**, **eylem seçimi** ve **öğrenme** süreçlerini içerir
- Durum vektörü (11 boyut):
  - Çarpışma tehlikeleri
  - Mevcut yön bilgisi
  - Yemin konumu
- ε-greedy stratejisi ile:
  - Eğitim sırasında keşif (exploration)
  - Test sırasında tamamen greedy politika

Ajan:
- Kısa süreli hafıza (online öğrenme)
- Uzun süreli hafıza (experience replay)
kullanarak eğitilmektedir.

---

### `model.py` – Sinir Ağı (Q-Network)
- Basit ama etkili bir **2 katmanlı tam bağlantılı ağ**
- Girdi: Durum vektörü
- Çıktı: Her eylem için Q-değerleri
- Kayıp fonksiyonu: **Mean Squared Error (MSE)**

Model, en iyi performans elde edildiğinde otomatik olarak kaydedilir.

---

### `train.py` – Eğitim Süreci
- Ajan toplam **700 oyun (episode)** boyunca eğitilmiştir
- Eğitim sırasında:
  - Rastgele keşif → öğrenilen politika
  - Bellekten örnekleme ile stabil öğrenme
- En yüksek skor elde edildiğinde model ağırlıkları kaydedilir

Eğitim çıktıları:
- Ajanın zamanla rastgele hareketten bilinçli davranışlara geçtiği gözlemlenmiştir
- Maksimum skor: **~80**

---

### `play.py` – Test Modu
- Eğitimli model yüklenir
- Keşif kapatılır (`train_mode = False`)
- Ajan oyunu tamamen öğrendiği politikaya göre oynar
- Oyun görsel olarak izlenebilir

---

## 🛠️ Kullanılan Teknolojiler

- **Python**
- **PyTorch**
- **Pygame**
- **NumPy**

---
## 📊 Elde Edilen Sonuçlar

- Ajan, başlangıçta rastgele hareket ederken
- Eğitim ilerledikçe:
  - Yemlere daha bilinçli yönelme
  - Çarpışmalardan kaçınma
  davranışları geliştirmiştir

Elde edilen skorlar, modelin **anlamlı bir politika öğrendiğini** göstermektedir.

---

## 📚 Teorik Arka Plan

Bu uygulama, staj sürecinde hazırlanan
**“Derin Takviyeli Öğrenme Yöntemleri ve Oyun Uygulamaları”**
başlıklı literatür çalışması ile desteklenmiştir.

---

## 📝 Not

Bu proje **eğitim ve araştırma amacıyla** geliştirilmiştir ve  
**Lotus AI staj sürecinin** bir parçasıdır.

