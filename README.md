# 🎬 Talk2Video

**Talk2Video** is an open-source AI agent that transforms spoken or written instructions into narrated videos.  
Say it — see it. Just like that.

Whether it's a story, presentation, tutorial, or visual script, Talk2Video listens, understands, and **directs your video with speech**.

---

## ✨ Features

- 🎙️ Convert **spoken or typed commands** into full video scenes
- 🧠 Use **LLM (OpenAI, Mistral, etc.)** to understand and script scenes
- 📸 Generate video scenes with **text-to-image/video models** (DALL·E, SD, Pika, RunwayML)
- 🗣️ Add natural voiceovers with **TTS APIs** (ElevenLabs, Bark, Coqui, Google TTS)
- 🎞️ Compose and render final video with **FFmpeg** or **moviepy**
- 🧾 Script memory: multi-step stories or presentations
- 🎛️ Optional GUI and CLI versions

---

## 🧠 Architecture & Tech Stack

| Layer | Tools |
|-------|-------|
| 🗣️ Input | Microphone (speech) or text prompt |
| 💬 NLP & Scene Logic | OpenAI GPT-4, Claude, or local LLM via Ollama |
| 🎨 Visual Generator | Stable Diffusion, DALL·E, Pika Labs, or Runway API |
| 🔊 Voice Generator | ElevenLabs, Bark, Coqui, or Google TTS |
| 🎬 Video Composer | FFmpeg, moviepy, or custom compositor |
| 🖥️ Interface | CLI + optional GUI (PyQt or Tauri) |
| 🧰 Backend | Python 3.11+ (main), Node.js (if using GUI), Shell |
| 🗃️ File Format | Outputs MP4 + JSON metadata per project |

---

## 🔧 Setup

```bash
git clone https://github.com/makalin/Talk2Video.git
cd Talk2Video
pip install -r requirements.txt
# Optional: setup API keys in .env
````

---

## 🗣️ Example Usage

### CLI

```bash
python talk2video.py --input "A calm beach at sunset, narrated in a soft female voice"
```

### Voice Mode

```bash
python talk2video.py --mic
# Speak: "Create a cyberpunk city intro with deep voice narration"
```

---

## 📦 API Keys Required

* `OPENAI_API_KEY` – for GPT logic
* `ELEVENLABS_API_KEY` (or `GOOGLE_TTS_API_KEY`) – for voice
* `RUNWAY_API_KEY` or `STABLE_DIFFUSION_HOST` – for visuals

---

## 🔌 Modular Design

Want to use your own models or APIs? Just replace:

* `voice.py`
* `visuals.py`
* `logic.py`

---

## 🧪 Roadmap

* [ ] Scene transitions & camera effects
* [ ] Avatar lip-sync support
* [ ] Multi-language narration
* [ ] Built-in storyboarding
* [ ] Mobile app (React Native or Flutter)

---

## 🤖 License

MIT License — free to use, modify, and contribute.

---

## 🙌 Contribute

Pull requests welcome!
Let’s make storytelling with voice easy for everyone.
