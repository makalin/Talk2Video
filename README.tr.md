# 🎬 Talk2Video

**Talk2Video**, konuşulan veya yazılan talimatları anlatımlı videolara dönüştüren açık kaynaklı bir yapay zeka aracıdır.  
Söyle — gör. Bu kadar basit.

Bir hikaye, sunum, eğitim veya görsel senaryo olsun, Talk2Video dinler, anlar ve **videonuzu sesle yönetir**.

---

## ✨ Özellikler

- 🎙️ **Konuşulan veya yazılan komutları** tam video sahnelerine dönüştürür
- 🧠 **LLM (OpenAI, Mistral, vb.)** ile sahneleri anlar ve senaryolaştırır
- 📸 **Metinden görsele/video** modelleriyle sahne üretir (DALL·E, SD, Pika, RunwayML)
- 🗣️ **Doğal seslendirme** ekler (ElevenLabs, Bark, Coqui, Google TTS)
- 🎞️ **FFmpeg** veya **moviepy** ile videoyu birleştirir ve renderlar
- 🧾 Senaryo hafızası: Çok adımlı hikaye veya sunumlar
- 🎛️ İsteğe bağlı GUI ve CLI sürümleri

---

## 🧠 Mimari & Teknoloji Yığını

| Katman | Araçlar |
|-------|-------|
| 🗣️ Girdi | Mikrofon (konuşma) veya metin komutu |
| 💬 NLP & Sahneler | OpenAI GPT-4, Claude veya yerel LLM (Ollama) |
| 🎨 Görsel Üretici | Stable Diffusion, DALL·E, Pika Labs, Runway API |
| 🔊 Ses Üretici | ElevenLabs, Bark, Coqui, Google TTS |
| 🎬 Video Birleştirici | FFmpeg, moviepy veya özel birleştirici |
| 🖥️ Arayüz | CLI + isteğe bağlı GUI (PyQt veya Tauri) |
| 🧰 Backend | Python 3.11+ (ana), Node.js (GUI için), Shell |
| 🗃️ Dosya Formatı | MP4 + JSON çıktı |

---

## 🔧 Kurulum

```bash
git clone https://github.com/makalin/Talk2Video.git
cd Talk2Video
pip install -r requirements.txt
# İsteğe bağlı: API anahtarlarını .env dosyasına ekleyin
```

---

## 🗣️ Örnek Kullanım

### CLI

```bash
python talk2video.py --input "Gün batımında sakin bir plaj, yumuşak kadın sesiyle anlatım"
```

### Sesli Mod

```bash
python talk2video.py --mic
# Konuşun: "Derin sesli anlatımla siberpunk şehir girişi oluştur"
```

---

## 📦 Gerekli API Anahtarları

* `OPENAI_API_KEY` – GPT mantığı için
* `ELEVENLABS_API_KEY` (veya `GOOGLE_TTS_API_KEY`) – ses için
* `RUNWAY_API_KEY` veya `STABLE_DIFFUSION_HOST` – görseller için

---

## 🔌 Modüler Tasarım

Kendi model veya API'nizi mi kullanmak istiyorsunuz? Sadece şunları değiştirin:

* `voice.py`
* `visuals.py`
* `logic.py`

---

## 🧪 Yol Haritası

* [ ] Sahne geçişleri & kamera efektleri
* [ ] Avatar dudak senkronizasyonu
* [ ] Çok dilli anlatım (Türkçe dahil!)
* [ ] Dahili storyboard
* [ ] Mobil uygulama (React Native veya Flutter)

---

## 🤖 Lisans

MIT Lisansı — kullanmakta, değiştirmekte ve katkıda bulunmakta özgürsünüz.

---

## 🙌 Katkı

Pull request'ler memnuniyetle karşılanır!
Herkes için sesli hikaye anlatımını kolaylaştıralım. 