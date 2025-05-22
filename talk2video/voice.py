"""
Voice generation module for Talk2Video
"""

import os
from typing import Optional, Dict, Any
from elevenlabs import generate, set_api_key
from google.cloud import texttospeech
from dotenv import load_dotenv
from .languages import LanguageManager

load_dotenv()

class VoiceGenerator:
    def __init__(self, provider: str = "elevenlabs"):
        self.provider = provider
        self.language_manager = LanguageManager()
        
        if provider == "elevenlabs":
            api_key = os.getenv("ELEVENLABS_API_KEY")
            if not api_key:
                raise ValueError("ELEVENLABS_API_KEY not found in environment variables")
            set_api_key(api_key)
        elif provider == "google":
            credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
            if not credentials_path:
                raise ValueError("GOOGLE_APPLICATION_CREDENTIALS not found in environment variables")
            self.google_client = texttospeech.TextToSpeechClient()
    
    def generate_voice(self, text: str, lang_code: str = "en", voice_id: Optional[str] = None, 
                      speed: float = 1.0, pitch: float = 0.0) -> bytes:
        """
        Generate voice audio from text
        
        Args:
            text: Text to convert to speech
            lang_code: Language code (e.g., 'en', 'es', 'fr')
            voice_id: Optional voice ID override
            speed: Speech rate (0.5 to 2.0)
            pitch: Voice pitch (-20.0 to 20.0)
            
        Returns:
            bytes: Audio data
        """
        if self.provider == "elevenlabs":
            voice = voice_id or self.language_manager.get_voice_id(lang_code, "elevenlabs")
            if not voice:
                raise ValueError(f"No voice found for language {lang_code}")
                
            audio = generate(
                text=text,
                voice=voice,
                model="eleven_multilingual_v2" if lang_code != "en" else "eleven_monolingual_v1"
            )
            return audio
            
        elif self.provider == "google":
            voice = voice_id or self.language_manager.get_voice_id(lang_code, "google")
            if not voice:
                raise ValueError(f"No voice found for language {lang_code}")
                
            synthesis_input = texttospeech.SynthesisInput(text=text)
            voice_config = texttospeech.VoiceSelectionParams(
                language_code=lang_code,
                name=voice,
                ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
            )
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3,
                speaking_rate=speed,
                pitch=pitch
            )
            
            response = self.google_client.synthesize_speech(
                input=synthesis_input,
                voice=voice_config,
                audio_config=audio_config
            )
            return response.audio_content
            
        else:
            raise NotImplementedError(f"Provider {self.provider} not implemented")
            
    def get_available_voices(self, lang_code: str) -> Dict[str, Any]:
        """Get available voices for a language"""
        lang = self.language_manager.get_language(lang_code)
        if not lang:
            return {}
            
        return {
            "provider": lang.tts_provider,
            "voices": lang.voice_ids
        } 