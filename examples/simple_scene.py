"""
Simple example of generating a video scene
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
    scene_manager = SceneManager()
    visual_gen = VisualGenerator()
    voice_gen = VoiceGenerator()
    
    # Generate scene
    prompt = "A peaceful beach at sunset with gentle waves"
    scene = scene_manager.generate_scene(prompt)
    
    print("Scene generated:", scene["description"])
    
    # Generate visual
    image = visual_gen.generate_image(scene["visual_prompt"])
    image.save("output/scene.png")
    
    # Generate voice
    audio = voice_gen.generate_voice(scene["narration"])
    with open("output/narration.mp3", "wb") as f:
        f.write(audio)
    
    print("Scene components generated successfully!")

if __name__ == "__main__":
    main() 