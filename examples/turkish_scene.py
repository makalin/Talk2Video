"""
Sample Turkish usage example for Talk2Video
"""

import os
from dotenv import load_dotenv
from talk2video.logic import SceneManager
from talk2video.visuals import VisualGenerator
from talk2video.voice import VoiceGenerator

def main():
    # Load environment variables
    load_dotenv()
    
    # Initialize components
    scene_manager = SceneManager(default_lang="tr")
    visual_gen = VisualGenerator()
    voice_gen = VoiceGenerator()
    
    # Turkish prompt
    prompt = "Gün batımında sakin bir plaj, yumuşak dalgalar"
    
    # Generate scene
    scene = scene_manager.generate_scene(
        prompt=prompt,
        lang_code="tr",
        style="cinematic",
        duration=5
    )
    
    print("Sahne oluşturuldu:", scene["description"])
    
    # Generate visual
    image = visual_gen.generate_image(scene["visual_prompt"])
    image.save("output/turkish_scene.png")
    
    # Generate voice
    audio = voice_gen.generate_voice(
        text=scene["narration"],
        lang_code="tr",
        speed=1.0,
        pitch=0.0
    )
    
    with open("output/turkish_narration.mp3", "wb") as f:
        f.write(audio)
    
    print("Türkçe sahne bileşenleri başarıyla oluşturuldu!")

if __name__ == "__main__":
    main() 