"""
Example of generating a video scene in multiple languages
"""

import os
from dotenv import load_dotenv
from talk2video.logic import SceneManager
from talk2video.visuals import VisualGenerator
from talk2video.voice import VoiceGenerator
from talk2video.languages import LanguageManager

def main():
    # Load environment variables
    load_dotenv()
    
    # Initialize components
    scene_manager = SceneManager()
    visual_gen = VisualGenerator()
    voice_gen = VoiceGenerator()
    lang_manager = LanguageManager()
    
    # Example scene in multiple languages
    prompt = "A peaceful beach at sunset with gentle waves"
    languages = ["en", "es", "fr", "de", "ja"]
    
    for lang_code in languages:
        print(f"\nGenerating scene in {lang_manager.get_language(lang_code).name}...")
        
        # Generate scene
        scene = scene_manager.generate_scene(
            prompt=prompt,
            lang_code=lang_code,
            style="cinematic",
            duration=5
        )
        
        print(f"Scene generated: {scene['description']}")
        
        # Generate visual
        image = visual_gen.generate_image(scene["visual_prompt"])
        image.save(f"output/scene_{lang_code}.png")
        
        # Generate voice
        audio = voice_gen.generate_voice(
            text=scene["narration"],
            lang_code=lang_code,
            speed=1.0,
            pitch=0.0
        )
        
        with open(f"output/narration_{lang_code}.mp3", "wb") as f:
            f.write(audio)
            
        print(f"Scene components generated for {lang_code}!")

if __name__ == "__main__":
    main() 