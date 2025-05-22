"""
Logic module for scene generation and management
"""

import os
from typing import List, Dict, Any, Optional
import openai
from dotenv import load_dotenv
from .languages import LanguageManager

load_dotenv()

class SceneManager:
    def __init__(self, model: str = "gpt-4", default_lang: str = "en"):
        self.model = model
        self.default_lang = default_lang
        self.language_manager = LanguageManager()
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        openai.api_key = api_key
        
    def generate_scene(self, prompt: str, lang_code: Optional[str] = None, 
                      style: str = "cinematic", duration: int = 5) -> Dict[str, Any]:
        """
        Generate scene details from prompt
        
        Args:
            prompt: User's scene description
            lang_code: Language code for narration
            style: Scene style (cinematic, documentary, etc.)
            duration: Scene duration in seconds
            
        Returns:
            Dict containing scene details
        """
        lang_code = lang_code or self.default_lang
        lang = self.language_manager.get_language(lang_code)
        if not lang:
            raise ValueError(f"Unsupported language: {lang_code}")
            
        system_prompt = f"""You are a professional video director creating a {style} scene.
        Generate a detailed scene description in {lang.name}.
        Include visual elements, camera movements, and narration text.
        Format the response as:
        VISUAL: [visual description]
        CAMERA: [camera movements]
        NARRATION: [narration text]"""
        
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        
        scene_text = response.choices[0].message.content
        
        # Parse scene details
        scene = {
            "description": scene_text,
            "visual_prompt": self._extract_visual_prompt(scene_text),
            "camera_movements": self._extract_camera_movements(scene_text),
            "narration": self._extract_narration(scene_text),
            "duration": duration,
            "language": lang_code,
            "style": style
        }
        
        return scene
    
    def _extract_visual_prompt(self, scene_text: str) -> str:
        """Extract visual description from scene text"""
        if "VISUAL:" in scene_text:
            return scene_text.split("VISUAL:")[1].split("CAMERA:")[0].strip()
        return scene_text
    
    def _extract_camera_movements(self, scene_text: str) -> str:
        """Extract camera movements from scene text"""
        if "CAMERA:" in scene_text:
            return scene_text.split("CAMERA:")[1].split("NARRATION:")[0].strip()
        return ""
    
    def _extract_narration(self, scene_text: str) -> str:
        """Extract narration text from scene text"""
        if "NARRATION:" in scene_text:
            return scene_text.split("NARRATION:")[1].strip()
        return scene_text
        
    def get_available_styles(self) -> List[str]:
        """Get list of available scene styles"""
        return ["cinematic", "documentary", "commercial", "educational", "dramatic"] 