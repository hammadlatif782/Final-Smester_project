"""
Custom Image Filters - OOP Implementation with Pillow
======================================================

This module demonstrates Object-Oriented Programming principles using Pillow's
image processing capabilities. Three custom filter implementations showcase
inheritance, encapsulation, and polymorphism.

Classes:
    VignetteFilter: Creates a vignette effect by darkening image edges
    SepiaToneFilter: Applies a sepia tone color effect
    InvertFilter: Inverts the colors in an image
"""

from PIL import Image, ImageFilter
import numpy as np


class BaseFilter(ImageFilter.Filter):
    """
    Base class for custom filters demonstrating inheritance principle.
    
    This class defines the interface that all filter subclasses must implement.
    It inherits from PIL's ImageFilter.Filter to be compatible with Image.filter()
    """
    
    size = 1
    
    def filter(self, image):
        """
        Apply the filter to an image.  
        Handles both full images and individual bands from PIL's Image.filter()
        
        Args:
            image: PIL Image object or PIL internal ImagingCore object
            
        Returns:
            Filtered image
        """
        # Check if this is a PIL internal object (band from Image.filter())
        if hasattr(image, 'tobytes') and hasattr(image, 'size'):
            # This is a band - convert to PIL Image
            band_bytes = image.tobytes()
            img = Image.frombytes('L', image.size, band_bytes)
            # Apply filter to the band
            return self._filter_band(img).im
        elif isinstance(image, Image.Image):
            # Full image
            return self._filter_image(image)
        else:
            return image
    
    def _filter_band(self, image):
        """Apply filter to a single grayscale band. Override in subclasses."""
        return image
    
    def _filter_image(self, image):
        """Apply filter to a full RGB image. Override in subclasses."""
        return image


class VignetteFilter(BaseFilter):
    """
    Vignette Filter - Darkens the edges of an image.
    
    This filter demonstrates inheritance from PIL's ImageFilter.Filter class
    and encapsulation through parameter validation.
    
    Attributes:
        strength (float): Controls vignette darkness (0.0 to 1.0)
        radius (float): Controls vignette spread radius (0.5 to 2.0)
    """
    
    name = "Vignette"
    
    def __init__(self, strength=0.5, radius=1.0):
        """
        Initialize the VignetteFilter.
        
        Args:
            strength (float): Darkness intensity, must be between 0.0 and 1.0
            radius (float): Spread radius, must be between 0.5 and 2.0
            
        Raises:
            ValueError: If parameters are outside valid ranges
        """
        # Encapsulation: Validate parameters
        if not 0.0 <= strength <= 1.0:
            raise ValueError(f"strength must be between 0.0 and 1.0, got {strength}")
        if not 0.5 <= radius <= 2.0:
            raise ValueError(f"radius must be between 0.5 and 2.0, got {radius}")
        
        self.strength = strength
        self.radius = radius
    
    def _filter_band(self, image):
        """
        Apply vignette effect to a single grayscale band.
        
        Args:
            image (PIL.Image): Grayscale image band
            
        Returns:
            PIL.Image: Filtered band
        """
        # Convert to numpy array
        img_array = np.array(image, dtype=np.float32)
        height, width = img_array.shape[:2]
        
        # Create vignette mask
        center_x, center_y = width / 2.0, height / 2.0
        max_dist = np.sqrt(center_x**2 + center_y**2)
        
        # Generate distance grid from center
        y, x = np.ogrid[:height, :width]
        dist_from_center = np.sqrt((x - center_x)**2 + (y - center_y)**2)
        
        # Create vignette mask based on distance and radius
        vignette_mask = 1 - (dist_from_center / (max_dist + 1e-6)) ** (1.0 / self.radius)
        vignette_mask = np.clip(vignette_mask, 0, 1)
        
        # Apply strength to the vignette effect
        darkening = 1 - (self.strength * (1 - vignette_mask))
        
        # Apply vignette
        img_array *= darkening
        
        # Convert back to PIL Image
        result = Image.fromarray(np.uint8(np.clip(img_array, 0, 255)), mode='L')
        return result
    
    def _filter_image(self, image):
        """
        Apply vignette effect to a full RGB image.
        
        Args:
            image (PIL.Image): Input image
            
        Returns:
            PIL.Image: Image with vignette effect
        """
        # Ensure image is in RGB mode
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Convert to numpy array for processing
        img_array = np.array(image, dtype=np.float32)
        height, width = img_array.shape[:2]
        
        # Create vignette mask
        center_x, center_y = width / 2.0, height / 2.0
        max_dist = np.sqrt(center_x**2 + center_y**2)
        
        # Generate distance grid from center
        y, x = np.ogrid[:height, :width]
        dist_from_center = np.sqrt((x - center_x)**2 + (y - center_y)**2)
        
        # Create vignette mask based on distance and radius
        vignette_mask = 1 - (dist_from_center / (max_dist + 1e-6)) ** (1.0 / self.radius)
        vignette_mask = np.clip(vignette_mask, 0, 1)
        
        # Apply strength to the vignette effect
        darkening = 1 - (self.strength * (1 - vignette_mask))
        
        # Apply vignette to each color channel
        for i in range(3):
            img_array[:, :, i] *= darkening
        
        # Convert back to PIL Image
        result = Image.fromarray(np.uint8(np.clip(img_array, 0, 255)))
        return result


class SepiaToneFilter(BaseFilter):
    """
    Sepia Tone Filter - Applies warm, brownish tones to an image.
    
    This filter demonstrates polymorphism by implementing the same interface
    as other filters while using different internal algorithms.
    
    Attributes:
        intensity (float): Controls sepia effect strength (0.0 to 1.0)
    """
    
    name = "SepiaTone"
    
    def __init__(self, intensity=0.5):
        """
        Initialize the SepiaToneFilter.
        
        Args:
            intensity (float): Effect strength, must be between 0.0 and 1.0
            
        Raises:
            ValueError: If intensity is outside valid range
        """
        # Encapsulation: Validate parameters
        if not 0.0 <= intensity <= 1.0:
            raise ValueError(f"intensity must be between 0.0 and 1.0, got {intensity}")
        
        self.intensity = intensity
    
    def _filter_band(self, image):
        """
        Apply sepia tone effect to a single grayscale band.
        
        Args:
            image (PIL.Image): Grayscale image band
            
        Returns:
            PIL.Image: Filtered band
        """
        # For a single band, apply a brightening based on intensity
        img_array = np.array(image, dtype=np.float32)
        
        # Apply sepia tone by adjusting brightness
        adjusted = img_array * (1 + self.intensity * 0.2)
        
        result = Image.fromarray(np.uint8(np.clip(adjusted, 0, 255)), mode='L')
        return result
    
    def _filter_image(self, image):
        """
        Apply sepia tone effect to a full RGB image.
        
        Args:
            image (PIL.Image): Input image
            
        Returns:
            PIL.Image: Image with sepia tone applied
        """
        # Ensure image is in RGB mode
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Convert to numpy array
        img_array = np.array(image, dtype=np.float32)
        
        # Sepia transformation matrix
        sepia_matrix = np.array([
            [0.393, 0.769, 0.189],  # Red channel
            [0.349, 0.686, 0.168],  # Green channel
            [0.272, 0.534, 0.131]   # Blue channel
        ])
        
        # Apply sepia transformation
        sepia = np.zeros_like(img_array)
        for i in range(3):
            sepia[:, :, i] = (
                img_array[:, :, 0] * sepia_matrix[i, 0] +
                img_array[:, :, 1] * sepia_matrix[i, 1] +
                img_array[:, :, 2] * sepia_matrix[i, 2]
            )
        
        # Blend with original based on intensity
        result_array = (
            img_array * (1 - self.intensity) +
            sepia * self.intensity
        )
        
        # Convert back to PIL Image
        result = Image.fromarray(np.uint8(np.clip(result_array, 0, 255)))
        return result


class InvertFilter(BaseFilter):
    """
    Invert Filter - Inverts all colors in an image.
    
    This is a simple filter that demonstrates the basic structure while
    providing useful functionality.
    """
    
    name = "Invert"
    
    def __init__(self):
        """Initialize the InvertFilter."""
        pass
    
    def _filter_band(self, image):
        """
        Invert a single grayscale band.
        
        Args:
            image (PIL.Image): Grayscale image band
            
        Returns:
            PIL.Image: Inverted band
        """
        # Convert to numpy array
        img_array = np.array(image, dtype=np.uint8)
        
        # Invert
        inverted_array = 255 - img_array
        
        # Convert back to PIL Image
        result = Image.fromarray(inverted_array, mode='L')
        return result
    
    def _filter_image(self, image):
        """
        Invert the colors of the image.
        
        Args:
            image (PIL.Image): Input image
            
        Returns:
            PIL.Image: Image with colors inverted
        """
        # Ensure image is in RGB mode
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Convert to numpy array
        img_array = np.array(image, dtype=np.uint8)
        
        # Invert the color channels
        inverted_array = 255 - img_array
        
        # Convert back to PIL Image
        result = Image.fromarray(inverted_array)
        return result
