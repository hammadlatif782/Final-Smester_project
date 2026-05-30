OOP Analysis Report — Pillow Library
Object-Oriented Programming Analysis: Pillow Library
Object-Oriented Programming Analysis: Pillow Library Course: Object-Oriented Programming (OOP) Final Term Project

Program: BS Data Science — Semester 2 
Group Member     ROLL NUMBER 
Hammad Latif    F25BDATS1M02049
Mudassir Jabbar F25BDATS1M02052 
Javeria Ahmad   F25BDATS1M02074 
Date: 7May 2026

Table of Contents
Library Overview
Class Hierarchy Diagram
OOP Principles Analysis
Design Decision Critique
Comparison with Alternatives
Custom Extension
References
Library Overview
What is Pillow?
Pillow (Python Imaging Library - PIL) is a powerful and widely-used Python imaging library that provides comprehensive tools for creating, opening, manipulating, and saving images in various formats. It is the de facto standard for image processing in Python.

Purpose
Pillow serves as a bridge between high-level Python code and low-level C/C++ imaging operations. It provides: Image file format support (JPEG, PNG, GIF, TIFF, BMP, WebP, etc.) Image manipulation operations (resize, rotate, crop, blur, etc.) Drawing capabilities (shapes, text, colors) Advanced operations (color management, statistical analysis)

Real-World Use Cases
Web Development: Django/Flask applications for image processing, thumbnail generation
Data Science: Image preprocessing in computer vision pipelines (PyTorch, TensorFlow)
Scientific Research: Medical imaging, satellite image analysis
Graphics Applications: Photo editing, batch image processing, watermarking
Game Development: Asset processing, sprite manipulation
Automation: Automated testing, screenshot analysis
Installation
pip install Pillow
Key Statistics
First Release: 1995
Current Version: 10.x (as of 2026)
GitHub Stars: 10,000+
Active Maintainers: Global open-source community
Lines of Python Code: ~10,000 lines (excluding C extensions)
Class Hierarchy Diagram
UML Class Hierarchy
                                ┌─────────────────┐
                                │  <<abstract>>   │
                                │     Filter      │
                                └────────┬────────┘
                                         │
                    ┌────────────────────┼────────────────────┐
                    │                    │                    │
           ┌────────▼────────┐  ┌────────▼────────┐  ┌────────▼────────┐
           │MultibandFilter  │  │ BuiltinFilter   │  │  RankFilter     │
           └────────────────┘  └────────┬────────┘  └─────────────────┘
                                        │
                    ┌───────────────────┼───────────────────┐
                    │                   │                   │
           ┌────────▼────────┐ ┌────────▼────────┐ ┌───────▼──────────┐
           │    Kernel       │ │   MedianFilter  │ │  GaussianBlur    │
           └─────────────────┘ └─────────────────┘ └──────────────────┘


                        ┌──────────────────┐
                        │   Image          │
                        │   (Main Class)   │
                        ├──────────────────┤
                        │- mode: str       │
                        │- size: tuple     │
                        │- palette: Palette│
                        │- info: dict      │
                        ├──────────────────┤
                        │+ open()          │
                        │+ save()          │
                        │+ paste()         │
                        │+ crop()          │
                        │+ resize()        │
                        │+ rotate()        │
                        │+ filter()        │
                        │+ getdata()       │
                        └────────┬─────────┘
                                 │ inherits
                                 │
                        ┌────────▼──────────┐
                        │  ImageFile        │
                        │  (Abstract Base)  │
                        ├───────────────────┤
                        │- fp: IO           │
                        │- format: str      │
                        │- tile: list       │
                        ├───────────────────┤
                        │+ _open()          │
                        │+ _load()          │
                        │+ _save()          │
                        │+ load()           │
                        │+ seek()           │
                        └────────┬──────────┘
                                 │ inherited by
         ┌───────────────────────┼───────────────────────┬───────────────┐
         │                       │                       │               │
    ┌────▼────────┐    ┌────────▼────────┐    ┌────────▼──────┐  ┌─────▼────────┐
    │GifImageFile │    │PngImagePlugin   │    │JpegImageFile  │  │BmpImageFile  │
    │(GIF Format) │    │(PNG Format)     │    │(JPEG Format)  │  │(BMP Format)  │
    └─────────────┘    └─────────────────┘    └───────────────┘  └──────────────┘


                        ┌──────────────────┐
                        │   ImageDraw      │
                        │  (Drawing Ops)   │
                        ├──────────────────┤
                        │- _image: Image   │
                        │- draw: core obj  │
                        │- mode: str       │
                        │- font: Font      │
                        ├──────────────────┤
                        │+ line()          │
                        │+ ellipse()       │
                        │+ rectangle()     │
                        │+ polygon()       │
                        │+ text()          │
                        │+ point()         │
                        └──────────────────┘


                        ┌──────────────────┐
                        │   ImageFont      │
                        │  (Font Handler)  │
                        ├──────────────────┤
                        │- font: obj       │
                        ├──────────────────┤
                        │+ getsize()       │
                        │+ getmask()       │
                        │+ getbbox()       │
                        └──────────────────┘


                    ┌──────────────────┐
                    │  ImagePalette    │
                    │  (Color Palette) │
                    ├──────────────────┤
                    │- palette: bytes  │
                    │- mode: str       │
                    ├──────────────────┤
                    │+ getcolor()      │
                    │+ tobytes()       │
                    │+ save()          │
                    └──────────────────┘
Plugin Architecture
┌─────────────────────────────────────┐ │ PluginRegistry │ │ (_plugins module) │ ├─────────────────────────────────────┤ │ - Format Plugins (dynamic loading) │ │ - Codec Registration │ │ - Lazy Loading Support │ └──────────────┬──────────────────────┘ │ ┌──────────┴──────────┬──────────────┐ │ │ │ ▼ ▼ ▼ ┌─────────┐ ┌────────┐ ┌──────────┐ │ Decoder │ │Encoder │ │ Identify │ │ (Read) │ │(Write) │ │ (Detect) │ └─────────┘ └────────┘ └──────────┘

OOP Principles Analysis
1. Encapsulation
Encapsulation is demonstrated through private attributes and controlled access in Pillow classes.

Code Example from Image.py:
class Image:
    """Represents an image object"""
    
    def __init__(self, ...):
        # Private attributes - protected with underscore convention
        self._mode = mode
        self._size = size
        self._palette = palette
        self._exif = exif
        self._im = im  # Core C object for performance
        self._readonly = False
    
    @property
    def mode(self) -> str:
        """
        The image mode ('RGB', 'L', 'RGBA', etc.)
        Read-only property - controlled access
        """
        return self._mode
    
    @property
    def size(self) -> tuple[int, int]:
        """
        The image size as (width, height)
        Immutable - users cannot directly set
        """
        return self._size
    
    def _ensure_mutable(self) -> None:
        """
        Private method - only called internally
        Prevents modification of read-only images
        """
        if self._readonly:
            msg = "cannot modify read-only image"
            raise OSError(msg)
    
    def paste(self, im: Image | int, box: tuple = None) -> None:
        """
        Public method with internal safeguards
        Encapsulation ensures data integrity
        """
        self._ensure_mutable()  # Internal validation
        # ... implementation ...
Benefits of Encapsulation in Pillow:

Data Protection: Internal image buffer (_im) cannot be corrupted
Consistency: Mode and size cannot be changed independently
Abstraction: Users don't need to know about C extension details
Version Compatibility: Internal implementation can change without breaking user code
2. Inheritance
Inheritance enables code reuse and establishes hierarchical relationships between image formats.

Code Example from ImageFile.py and GifImagePlugin.py:
# Base class - from ImageFile.py
class ImageFile(Image):
    """Base class for image file handlers"""
    
    # Shared attributes for all file-based image formats
    format = None  # Overridden by subclasses
    format_description = None
    
    def __init__(self, fp=None, filename=None):
        """Initialize file-based image"""
        super().__init__()  # Call parent constructor
        self.fp = fp
        self.filename = filename
    
    def _open(self) -> None:
        """
        Abstract method - must be implemented by subclasses
        Each format implements its own parsing logic
        """
        raise NotImplementedError("_open() not implemented")
    
    def load(self) -> None:
        """Template method - uses _open() implementation"""
        if self.fp:
            self._open()  # Calls subclass implementation
            self._load()  # Loads image data
    
    def _load(self) -> None:
        """Common loading logic for all formats"""
        # Generic frame/tile loading implementation
        pass


# Subclass 1 - GIF Format Handler
class GifImageFile(ImageFile):
    """Image plugin for GIF files"""
    
    format = "GIF"
    format_description = "Compuserve GIF"
    
    def _open(self) -> None:
        """GIF-specific parsing logic"""
        # Read GIF header
        s = self.fp.read(13)
        if not s.startswith((b"GIF87a", b"GIF89a")):
            raise SyntaxError("not a GIF file")
        
        # Parse logical screen descriptor
        self._size = (i16(s, 6), i16(s, 8))
        flags = s[10]
        bits = (flags & 7) + 1
        
        # Read global color table if present
        if flags & 128:
            p = self.fp.read(3 << bits)
            self.palette = ImagePalette.raw("RGB", p)
    
    @property
    def n_frames(self) -> int:
        """GIF-specific property for animation support"""
        # Count frames in animated GIF
        pass


# Subclass 2 - PNG Format Handler
class PngImageFile(ImageFile):
    """Image plugin for PNG files"""
    
    format = "PNG"
    format_description = "Portable Network Graphics"
    
    def _open(self) -> None:
        """PNG-specific parsing logic"""
        # Read PNG signature
        signature = self.fp.read(8)
        if signature != _MAGIC:
            raise SyntaxError("not a PNG file")
        
        # Parse PNG chunks
        self._read_chunks()
    
    def _read_chunks(self) -> None:
        """PNG-specific chunk parsing"""
        # Process IHDR, PLTE, IDAT, IEND chunks
        pass
Inheritance Benefits:

Code Reuse: Common file I/O logic in ImageFile base class
Polymorphism: Different formats implement _open() differently
Extensibility: New formats can be added as subclasses
Consistency: All file-based formats follow same interface
3. Polymorphism
Polymorphism allows different image format plugins to be treated uniformly through a common interface.

Code Example - Method Overriding:
# Base class defines interface
class ImageFile(Image):
    def _open(self):
        raise NotImplementedError()
    
    def load(self):
        """Template method that uses _open()"""
        if self.fp and not self.fp.closed:
            self._open()
            # Load image data


# Different plugins implement same interface differently
class JpegImageFile(ImageFile):
    def _open(self):
        # JPEG-specific parsing using JFIF/Exif format
        buffer = self.fp.read(16)
        # Parse SOI marker (0xFFD8) and App0 marker


class BmpImageFile(ImageFile):
    def _open(self):
        # BMP-specific parsing using DIB header
        self._size = (i32(bmpfileheader, 18), i32(bmpfileheader, 22))


class TiffImageFile(ImageFile):
    def _open(self):
        # TIFF-specific parsing using IFD (Image File Directory)
        tag_data = self.fp.read(8)
        # Parse byte order and TIFF magic number


# Polymorphic usage - same code works for all formats
def save_image_thumbnail(image_path, output_path):
    # Open returns appropriate subclass based on file format
    img = Image.open(image_path)  # Returns GifImageFile, PngImageFile, etc.
    
    # Same method call works for all formats (polymorphism!)
    img.thumbnail((150, 150))
    img.save(output_path, quality=85)
Code Example - Abstract Base Class (Filter):
# Abstract base class
class Filter(abc.ABC):
    """Base class for all image filters"""
    
    @abc.abstractmethod
    def filter(self, image):
        """Must be implemented by all subclasses"""
        pass


# Concrete implementations
class Kernel(Filter):
    """Convolution kernel filter"""
    def filter(self, image):
        return image.filter(KERNEL, self.size, self.kernel)


class MedianFilter(Filter):
    """Median filter for noise reduction"""
    def filter(self, image):
        return image.filter(MEDIAN, self.size)


class GaussianBlur(Filter):
    """Gaussian blur filter"""
    def filter(self, image):
        return image.filter(BLUR, self.radius)


# Polymorphic usage
def apply_filters(img, filters):
    """Works with any Filter subclass"""
    for filter_obj in filters:
        # Each filter implements differently internally
        img = img.filter(filter_obj)
    return img

# Usage:
filters = [
    GaussianBlur(radius=2),
    MedianFilter(size=3),
    Kernel(...)
]
result = apply_filters(img, filters)  # Polymorphism in action
Polymorphism Benefits:

Extensibility: New filters/formats can be added without changing client code
Flexibility: Users can write custom filters by inheriting from Filter
Maintainability: Plugin architecture separates concerns
Testability: Each implementation can be tested independently
4. Abstraction
Abstraction hides complex implementation details and exposes only essential functionality.

Code Example:
# Low-level C extension (implementation hidden)
from . import _imaging as core
# Users don't see: C-level memory management, buffer operations

class Image:
    def __init__(self, ...):
        # Complex C object creation hidden
        self._im = core.new(mode, size)  # C-level call
    
    def resize(self, size, resample=LANCZOS):
        """
        Simple, high-level interface
        Hides: interpolation algorithms, memory allocation, 
               coordinate transformation, buffer manipulation
        """
        im = self._im.resize(size, resample)
        return self._new(im)
    
    def filter(self, filter_obj):
        """
        High-level abstraction
        Hides: complex signal processing, kernel convolution,
               color space conversions, optimization logic
        """
        if isinstance(filter_obj, Filter):
            return filter_obj.filter(self._im)
        # ...


# Simple API abstraction
class ImageDraw:
    """Drawing operations abstraction"""
    
    def __init__(self, im):
        self._image = im
        # Hide core.draw() complexity
        self.draw = core.draw(self._image.im, blend=0)
        self.mode = im.mode
    
    def rectangle(self, xy, fill=None, outline=None, width=1):
        """
        Simple rectangle drawing
        Hides: coordinate normalization, color conversion,
               anti-aliasing, scanline algorithms
        """
        self.draw.rectangle(xy, self._getfill(fill), outline, width)
    
    def _getfill(self, fill):
        """Internal helper - encapsulates color processing"""
        if isinstance(fill, str):
            fill = ImageColor.getrgb(fill)
        return self.draw.draw_ink(fill)


# Real-world usage - very simple!
img = Image.new('RGB', (100, 100), 'white')
draw = ImageDraw.Draw(img)
draw.rectangle([10, 10, 90, 90], fill='red', outline='black', width=2)
img.save('output.png')
Abstraction Benefits:

Simplicity: Complex operations exposed as simple methods
Usability: No need to understand C extensions or low-level graphics
Maintainability: Implementation can be optimized without API changes
Learning Curve: Easy for beginners, depth available for advanced users
Design Decision Critique
1. Selected Design Decision: Plugin Architecture for Image Format Support
The Decision
Pillow uses a plugin/registry pattern for supporting multiple image formats, where:

Each image format (PNG, JPEG, GIF, etc.) is handled as a separate plugin
Plugins are lazily loaded when needed
A central registry (_plugins) manages format detection and handler instantiation
Users use the same Image.open() API regardless of format
Code Implementation:
# Central Image.open() method (simplified)
class Image:
    @staticmethod
    def open(fp, mode='r', formats=None):
        """Open and identify image file"""
        
        # Lazy detection - try each plugin's _accept() function
        for plugin_module in get_plugins():
            if plugin_module._accept(header):
                # Dynamically load appropriate handler
                handler = plugin_module.ImageFile()
                handler.load()
                return handler
        
        raise UnidentifiedImageError(f"Cannot identify image file")


# Plugin structure example (GifImagePlugin)
def _accept(prefix):
    """Plugin-specific format detection"""
    return prefix.startswith((b"GIF87a", b"GIF89a"))

class GifImageFile(ImageFile):
    format = "GIF"
    # GIF-specific implementation...
Why This Decision Was Made
Reason	Explanation
Extensibility	New image formats can be added without modifying core code
Lazy Loading	Only load plugins for formats actually used
Maintainability	Each format isolated in separate module
Community	Easy for external developers to contribute format handlers
Trade-offs
Advantage	Disadvantage
✓ Modular design	✗ Slight performance overhead in format detection
✓ Easy to extend	✗ More complex than monolithic approach
✓ Reduces memory footprint	✗ Requires plugin discovery mechanism
✓ Encapsulates format logic	✗ Harder to debug cross-format issues
Alternative Approaches
Option 1: Monolithic Design (NOT used)

# Everything in one Image class
class Image:
    def open(self, fp):
        header = fp.read(16)
        
        # Long if-elif chain
        if header.startswith(b'\x89PNG'):
            self._open_png(fp)
        elif header.startswith(b'GIF'):
            self._open_gif(fp)
        elif header.startswith(b'\xFF\xD8'):
            self._open_jpeg(fp)
        # ... 50+ more formats ...
Cons:

Single 5000+ line file
Tightly coupled code
Hard to extend without modifying core
High memory usage (all format logic always loaded)
Option 2: Separate Command-Line Tools (NOT used)

pil-png input.png output.jpg
pil-gif input.gif output.png
Cons:

Not a library, separate tools
No programmatic API
Poor for automation
Format conversion requires spawning processes
Why Plugin Architecture is Better
The plugin architecture balances:

Separation of Concerns: Each format has its own module
Performance: Formats loaded only when needed
Maintainability: Format-specific bugs isolated
Extensibility: Third-party formats can be registered
2. Secondary Design Decision: Template Method Pattern in ImageFile
The Pattern
# Template Method - base class defines algorithm structure
class ImageFile(Image):
    def load(self):
        """Template method - defines algorithm structure"""
        if self.fp and not self.fp.closed:
            self._open()  # Step 1: Subclass implements
            self._load()  # Step 2: Common logic
            self.fp.close()  # Step 3: Cleanup
    
    def _open(self):
        """Step 1: Subclasses override"""
        raise NotImplementedError()
    
    def _load(self):
        """Step 2: Common tile/frame loading"""
        # Shared logic for all formats
        pass

# Subclasses override specific step
class JpegImageFile(ImageFile):
    def _open(self):
        # JPEG-specific parsing only
        pass  # _load() inherited from parent
Benefits of This Pattern:

Reduces code duplication
Enforces consistent file handling
Easy to add new formats (implement only _open())
Comparison with Alternatives
Pillow vs. OpenCV
Feature	Pillow	OpenCV
Purpose	Image processing library	Computer vision library
Size	Lightweight (~2MB)	Heavy (~100MB+)
API Complexity	Simple, beginner-friendly	Complex, research-oriented
Image Formats	30+ formats	15+ formats
Image Manipulation	Basic (resize, crop, filter)	Advanced (morphing, tracking)
Performance	Good for most tasks	Optimized for CV algorithms
Learning Curve	1-2 hours	1-2 weeks
Machine Learning	Limited	Extensive (computer vision)
Documentation	Clear, practical	Academic, detailed
Best Use Case	Web apps, automation	Medical imaging, autonomous vehicles
OOP Design Comparison
Pillow's Approach:

# Minimal OOP overhead - focuses on usability
img = Image.open('photo.jpg')
img.thumbnail((150, 150))
img.save('thumb.jpg')
OpenCV's Approach:

# More OOP structure - extensible but complex
import cv2
img = cv2.imread('photo.jpg')
height, width = img.shape[:2]
scale = min(150/height, 150/width)
resized = cv2.resize(img, (int(width*scale), int(height*scale)))
cv2.imwrite('thumb.jpg', resized)
Pillow vs. scikit-image
Aspect	Pillow	scikit-image
Architecture	Plugin-based	Functional/NumPy-based
Data Structure	PIL Image objects	NumPy arrays
Target Audience	General Python developers	Data scientists
Algorithms	Basic filtering	Advanced scientific algorithms
Integration	Simple	Seamless with NumPy/SciPy
Custom Extension
Extending ImageFilter for Advanced Effects
We'll create a custom VignetteFilter that adds a vignette effect to images:

# custom_filters.py
from PIL import Image, ImageDraw, ImageFilter
import math

class VignetteFilter(ImageFilter.Filter):
    """
    Custom filter that applies a vignette effect (darkening edges)
    
    Demonstrates:
    - Inheritance from Filter abstract base class
    - Overriding abstract method filter()
    - Method composition (using existing Pillow classes)
    - Encapsulation of algorithm parameters
    """
    
    def __init__(self, strength=0.5, radius=1.5):
        """
        Initialize vignette filter
        
        Args:
            strength: How dark the vignette becomes (0.0 to 1.0)
            radius: How far from center the vignette extends (1.0 to 3.0)
        """
        self.strength = max(0, min(1, strength))  # Clamp 0-1
        self.radius = max(1, min(3, radius))      # Clamp 1-3
    
    def filter(self, image):
        """
        Apply vignette effect
        
        Overrides abstract method from Filter base class
        """
        width, height = image.size
        
        # Create gradient overlay (the vignette mask)
        vignette = Image.new('L', (width, height), 255)
        vignette_draw = ImageDraw.Draw(vignette)
        
        # Calculate center point
        center_x, center_y = width / 2, height / 2
        
        # Calculate maximum distance from center
        max_dist = math.sqrt(center_x**2 + center_y**2) / self.radius
        
        # Draw darkening from edges inward
        for y in range(height):
            for x in range(width):
                # Calculate distance from center
                dx = x - center_x
                dy = y - center_y
                dist = math.sqrt(dx**2 + dy**2)
                
                # Calculate vignette intensity
                intensity = 255 * (1 - self.strength * (dist / max_dist)**2)
                intensity = max(0, min(255, int(intensity)))
                
                vignette.putpixel((x, y), intensity)
        
        # Apply Gaussian blur for smooth transition
        vignette = vignette.filter(ImageFilter.GaussianBlur(radius=15))
        
        # Convert image to RGBA to support transparency
        if image.mode != 'RGBA':
            image = image.convert('RGBA')
        
        # Create darkening overlay
        overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        
        # Apply vignette mask to overlay
        for y in range(height):
            for x in range(width):
                vignette_val = vignette.getpixel((x, y))
                alpha = int(255 * (1 - vignette_val / 255) * self.strength)
                overlay.putpixel((x, y), (0, 0, 0, alpha))
        
        # Composite overlay onto original image
        return Image.alpha_composite(image, overlay)


class SepiaToneFilter(ImageFilter.Filter):
    """
    Custom filter for sepia tone effect
    
    Demonstrates:
    - Color transformation
    - Matrix operations
    - Extending Pillow functionality
    """
    
    def __init__(self, intensity=1.0):
        """
        Initialize sepia filter
        
        Args:
            intensity: Strength of sepia effect (0.0 to 1.0)
        """
        self.intensity = max(0, min(1, intensity))
    
    def filter(self, image):
        """Apply sepia tone transformation"""
        # Convert to RGB if necessary
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Convert to grayscale
        gray = image.convert('L')
        
        # Create sepia toned image
        width, height = image.size
        sepia = Image.new('RGB', (width, height))
        
        for y in range(height):
            for x in range(width):
                # Get grayscale value
                gray_val = gray.getpixel((x, y))
                
                # Apply sepia formula
                r = int(gray_val * 1.2)
                g = int(gray_val * 1.0)
                b = int(gray_val * 0.8)
                
                # Clamp values to 0-255
                r = min(255, r)
                g = min(255, g)
                b = min(255, b)
                
                sepia.putpixel((x, y), (r, g, b))
        
        # Blend with original based on intensity
        original = image.convert('RGB')
        result = Image.new('RGB', (width, height))
        
        for y in range(height):
            for x in range(width):
                orig_pixel = original.getpixel((x, y))
                sepia_pixel = sepia.getpixel((x, y))
                
                # Blend pixels
                blended = (
                    int(orig_pixel[0] * (1 - self.intensity) + sepia_pixel[0] * self.intensity),
                    int(orig_pixel[1] * (1 - self.intensity) + sepia_pixel[1] * self.intensity),
                    int(orig_pixel[2] * (1 - self.intensity) + sepia_pixel[2] * self.intensity),
                )
                result.putpixel((x, y), blended)
        
        return result


# ============================================================================
# DEMONSTRATION / MAIN BLOCK
# ============================================================================

def demonstrate_custom_filters():
    """
    Demo script showing custom filter usage
    
    Demonstrates how custom classes properly extend Pillow's architecture
    """
    
    # Create a sample image
    print("Creating sample image...")
    sample_img = Image.new('RGB', (400, 300), color='white')
    draw = ImageDraw.Draw(sample_img)
    
    # Draw some content
    draw.rectangle([50, 50, 350, 250], outline='blue', width=2)
    draw.text((100, 100), "Sample Image", fill='black')
    draw.ellipse([200, 100, 300, 200], fill='yellow', outline='red', width=3)
    
    # Apply vignette filter
    print("Applying vignette filter...")
    vignette = VignetteFilter(strength=0.6, radius=1.5)
    vignetted = sample_img.filter(vignette)
    vignetted.save('output_vignette.png')
    print("✓ Saved: output_vignette.png")
    
    # Apply sepia filter
    print("Applying sepia tone filter...")
    sepia = SepiaToneFilter(intensity=0.8)
    sepia_img = sample_img.filter(sepia)
    sepia_img.save('output_sepia.png')
    print("✓ Saved: output_sepia.png")
    
    # Apply both filters in sequence
    print("Applying vignette + sepia...")
    combined = sample_img.filter(vignette).filter(sepia)
    combined.save('output_combined.png')
    print("✓ Saved: output_combined.png")
    
    print("\nDemo complete! Check output images.")


if __name__ == "__main__":
    demonstrate_custom_filters()
How the Custom Extension Demonstrates OOP Principles
Inheritance: VignetteFilter and SepiaToneFilter inherit from ImageFilter.Filter

class VignetteFilter(ImageFilter.Filter):
    # Inherits from abstract base class
Method Overriding: Subclasses override the abstract filter() method

def filter(self, image):
    # Implementation specific to this filter type
Encapsulation: Private parameters with controlled initialization

def __init__(self, strength=0.5):
    self.strength = max(0, min(1, strength))  # Validated
Polymorphism: Custom filters work with existing Pillow image processing pipeline

result = image.filter(VignetteFilter())  # Works like built-in filters
result = result.filter(SepiaToneFilter())  # Can chain filters
Abstraction: Users interact with simple filter() interface, not low-level details

# Simple API hides complex processing
filtered = img.filter(CustomFilter())
References
Official Documentation
Pillow Official Documentation
Pillow GitHub Repository
PIL (Original) Documentation Archive
Source Code Resources
Image.py - Main Image class implementation
ImageFile.py - Base class for file-based image formats
ImageDraw.py - Drawing operations
ImageFilter.py - Filter abstract base class and implementations
GifImagePlugin.py, PngImagePlugin.py - Format-specific implementations
Related Libraries
OpenCV-Python
scikit-image
ImageMagick - Command-line image processing tool
OOP Concepts References
Design Patterns:

Plugin Architecture Pattern
Template Method Pattern
Abstract Factory Pattern
Python OOP:

Python Abstract Base Classes (abc)
Python Properties and Descriptors
Academic References
Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). Design Patterns: Elements of Reusable Object-Oriented Software.
Freeman, E., Freeman, E., Sierra, K., & Bates, B. (2004). Head First Design Patterns.
Conclusion
Pillow is an excellent case study for professional-grade OOP design in Python. Its use of plugin architecture, abstract base classes, and template method patterns demonstrates how to build extensible, maintainable libraries. The careful encapsulation of C-level operations behind high-level Python interfaces shows how to balance performance with usability.

The library proves that good OOP design is not about complexity, but about clarity, extensibility, and maintainability. By studying Pillow's architecture, developers can learn valuable lessons about designing robust, professional-grade libraries
