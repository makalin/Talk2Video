"""
Visual generation module for Talk2Video
"""

import os
import requests
from typing import Optional
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

class VisualGenerator:
    def __init__(self, provider: str = "stable-diffusion"):
        self.provider = provider
        self.api_key = os.getenv("RUNWAY_API_KEY")
        self.sd_host = os.getenv("STABLE_DIFFUSION_HOST")
        
    def generate_image(self, prompt: str, size: tuple = (512, 512)) -> Image.Image:
        """
        Generate image from text prompt
        
        Args:
            prompt: Text description of the image
            size: Tuple of (width, height)
            
        Returns:
            PIL.Image: Generated image
        """
        if self.provider == "stable-diffusion":
            if not self.sd_host:
                raise ValueError("STABLE_DIFFUSION_HOST not found in environment variables")
                
            response = requests.post(
                f"{self.sd_host}/sdapi/v1/txt2img",
                json={
                    "prompt": prompt,
                    "width": size[0],
                    "height": size[1],
                    "steps": 20,
                }
            )
            
            if response.status_code != 200:
                raise Exception(f"Failed to generate image: {response.text}")
                
            r = response.json()
            image = Image.open(BytesIO(bytes(r['images'][0], 'utf-8')))
            return image
            
        elif self.provider == "runway":
            if not self.api_key:
                raise ValueError("RUNWAY_API_KEY not found in environment variables")
            raise NotImplementedError("Runway API not implemented yet")
            
        else:
            raise NotImplementedError(f"Provider {self.provider} not implemented") 