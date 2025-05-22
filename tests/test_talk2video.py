"""
Test cases for Talk2Video
"""

import pytest
from talk2video.voice import VoiceGenerator
from talk2video.visuals import VisualGenerator
from talk2video.logic import SceneManager

def test_voice_generator_initialization():
    """Test voice generator initialization"""
    with pytest.raises(ValueError):
        VoiceGenerator()  # Should raise error without API key

def test_visual_generator_initialization():
    """Test visual generator initialization"""
    with pytest.raises(ValueError):
        VisualGenerator()  # Should raise error without API key

def test_scene_manager_initialization():
    """Test scene manager initialization"""
    with pytest.raises(ValueError):
        SceneManager()  # Should raise error without API key

def test_scene_generation():
    """Test scene generation"""
    # This test requires API keys to be set
    pytest.skip("Requires API keys")
    
    manager = SceneManager()
    scene = manager.generate_scene("A peaceful beach at sunset")
    
    assert isinstance(scene, dict)
    assert "description" in scene
    assert "visual_prompt" in scene
    assert "narration" in scene
    assert "duration" in scene 