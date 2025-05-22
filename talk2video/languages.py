"""
Language configuration module for Talk2Video
"""

from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass
class LanguageConfig:
    code: str
    name: str
    voice_ids: Dict[str, str]  # Provider -> voice_id mapping
    tts_provider: str
    default_voice: str

class LanguageManager:
    def __init__(self):
        self.languages: Dict[str, LanguageConfig] = {
            "en": LanguageConfig(
                code="en",
                name="English",
                voice_ids={
                    "elevenlabs": "EXAVITQu4vr4xnSDxMaL",
                    "google": "en-US-Neural2-F",
                },
                tts_provider="elevenlabs",
                default_voice="EXAVITQu4vr4xnSDxMaL"
            ),
            "es": LanguageConfig(
                code="es",
                name="Spanish",
                voice_ids={
                    "elevenlabs": "ErXwobaYiN019PkySvjV",
                    "google": "es-ES-Neural2-A",
                },
                tts_provider="elevenlabs",
                default_voice="ErXwobaYiN019PkySvjV"
            ),
            "fr": LanguageConfig(
                code="fr",
                name="French",
                voice_ids={
                    "elevenlabs": "MF3mGyEYCl7XYWbV9V6O",
                    "google": "fr-FR-Neural2-A",
                },
                tts_provider="elevenlabs",
                default_voice="MF3mGyEYCl7XYWbV9V6O"
            ),
            "de": LanguageConfig(
                code="de",
                name="German",
                voice_ids={
                    "elevenlabs": "AZnzlk1XvdvUeBnXmlld",
                    "google": "de-DE-Neural2-B",
                },
                tts_provider="elevenlabs",
                default_voice="AZnzlk1XvdvUeBnXmlld"
            ),
            "ja": LanguageConfig(
                code="ja",
                name="Japanese",
                voice_ids={
                    "elevenlabs": "TxGEqnHWrfWFTfGW9XjX",
                    "google": "ja-JP-Neural2-B",
                },
                tts_provider="elevenlabs",
                default_voice="TxGEqnHWrfWFTfGW9XjX"
            ),
            "tr": LanguageConfig(
                code="tr",
                name="Turkish",
                voice_ids={
                    "elevenlabs": "VR6AewLTigWG4xSOukaG",
                    "google": "tr-TR-Wavenet-A",
                },
                tts_provider="elevenlabs",
                default_voice="VR6AewLTigWG4xSOukaG"
            ),
        }
        
    def get_language(self, code: str) -> Optional[LanguageConfig]:
        """Get language configuration by code"""
        return self.languages.get(code.lower())
    
    def get_available_languages(self) -> List[str]:
        """Get list of available language codes"""
        return list(self.languages.keys())
    
    def get_voice_id(self, lang_code: str, provider: Optional[str] = None) -> Optional[str]:
        """Get voice ID for language and provider"""
        lang = self.get_language(lang_code)
        if not lang:
            return None
            
        if provider:
            return lang.voice_ids.get(provider)
        return lang.voice_ids.get(lang.tts_provider) 