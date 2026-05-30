# Pillow OOP Analysis - Quick Reference Guide

**For Group Presentation & Viva**

---

##The 4 OOP Principles in Pillow

### ENCAPSULATION - "Data Protection"

**Definition:** Bundling data and methods together, hiding internal details.

**Where in Pillow:**
```python
class Image:
    def __init__(self):
        self._mode = mode        # Private (underscore = hidden)
        self._size = size        # Private
        self._im = core_object   # Hidden C extension!
    
    @property
    def mode(self):              # Read-only access
        return self._mode        # Can't be directly modified
    
    def _ensure_mutable(self):   # Private method
        if self._readonly:
            raise OSError("Cannot modify read-only image")
```

Why it matters:
Prevents accidental modification of image buffer
Keeps internal C extension hidden
Allows implementation changes without breaking code
Forces validation before changes

**Real-world example:**
```python
img = Image.open('photo.jpg')
img.mode = 'RGBA'  # WRONG! Won't work - property is read-only
# Instead:
img_rgba = img.convert('RGBA')  # Controlled conversion
```

---

### 2 INHERITANCE - "Code Reuse"

**Definition:** Child classes inherit properties and methods from parent classes.

**Where in Pillow:**
```
Image (Parent - Core functionality)
    ↓
ImageFile (Parent - File handling)
    ↓
├── GifImageFile
├── PngImageFile  
├── JpegImageFile
├── BmpImageFile
└── [30+ other format handlers]
```

**Code Example:**
```python
class ImageFile(Image):              # Inherits from Image
    def load(self):                  # Common template
        self._open()                 # Subclass implements
        self._load()                 # Shared logic

class GifImageFile(ImageFile):       # Inherits from ImageFile
    def _open(self):
        # GIF-specific parsing only
        # Don't repeat the load() template!

class PngImageFile(ImageFile):       # Inherits from ImageFile
    def _open(self):
        # PNG-specific parsing only
        # Reuses same load() template
```

**Why it matters:**
 Eliminates code duplication (DRY principle)
 Common logic in one place (easier to fix bugs)
 New formats only need format-specific code
Consistent behavior across all formats

**Real-world example:**
```python
# All formats use same interface!
img_gif = Image.open('image.gif')
img_png = Image.open('image.png')
img_jpg = Image.open('image.jpg')

# But internally, different _open() implementations
```

---

### 3️POLYMORPHISM - "Same Interface, Different Implementation"

**Definition:** Different objects respond to the same method call in their own way.

**Where in Pillow - Method Overriding:**
```python
class ImageFile(Image):
    def _open(self):
        raise NotImplementedError()  # Template method

class GifImageFile(ImageFile):
    def _open(self):
        # Read GIF87a or GIF89a header
        s = self.fp.read(13)
        if not s.startswith((b"GIF87a", b"GIF89a")):
            raise SyntaxError("not a GIF file")

class PngImageFile(ImageFile):
    def _open(self):
        # Read PNG magic bytes
        signature = self.fp.read(8)
        if signature != b'\x89PNG\r\n\x1a\n':
            raise SyntaxError("not a PNG file")
```

**Where in Pillow - Filter Classes:**
```python
# Abstract base class
class Filter(ABC):
    @abstractmethod
    def filter(self, image):
        pass  # Each subclass implements differently

# Different implementations
class GaussianBlur(Filter):
    def filter(self, image):
        # Gaussian blur algorithm
        pass

class MedianFilter(Filter):
    def filter(self, image):
        # Median filter algorithm
        pass

class Kernel(Filter):
    def filter(self, image):
        # Convolution kernel algorithm
        pass
```

**Using polymorphism:**
```python
# Same code works for ANY filter!
def apply_filter(image, filter_obj):
    return image.filter(filter_obj)

# Works with built-in filters
apply_filter(img, GaussianBlur(2))
apply_filter(img, MedianFilter(3))

# Works with custom filters!
apply_filter(img, VignetteFilter(strength=0.5))
apply_filter(img, SepiaToneFilter(intensity=0.8))
```

**Why it matters:**
  Write code once, works for many types
  Easy to add new types (new filters)
  No code changes needed for new implementations
  Plugin architecture possible

---

### 4️ ABSTRACTION - "Hide Complexity"

**Definition:** Show only essential features, hide implementation details.

**Where in Pillow:**
```python
# Simple high-level API
img = Image.open('photo.jpg')        # Hidden: format detection
img.thumbnail((150, 150))            # Hidden: resize algorithm
img.save('thumb.jpg')                # Hidden: compression

# Actual complexity hidden inside:
# - File format parsing
# - Color space conversion
# - Memory buffer management
# - C extension calls
# - Platform-specific code
```

**Example - Abstraction Layers:**
```
User Code: img.resize((100, 100))
    ↓
Abstract Method: Image.resize()
    ↓
Core Function: core.resize()
    ↓
C Extension (_imaging.c)
    ↓
Low-level operations (memory, algorithms)
```

**Abstraction in practice:**
```python
# User doesn't need to know:
# - How resampling algorithms work
# - How pixels are stored in memory
# - Platform differences (Windows/Linux/Mac)

# Just use the simple interface:
img_small = img.resize((200, 200), Image.LANCZOS)
```

**Why it matters:**
Simple API for complex operations
 Easy for beginners to use
 Advanced users don't see unnecessary details
 Implementation can be optimized without API changes

---

##  Design Patterns in Pillow

### Plugin Architecture Pattern

**Problem:** How to support 30+ image formats?

**Bad approach:**
```python
if header.startswith(b'PNG'):
    # Handle PNG
elif header.startswith(b'JPEG'):
    # Handle JPEG
elif header.startswith(b'GIF'):
    # Handle GIF
# ... 50+ more conditions ... 😫
```

**Pillow's approach:**
```python
# Each format is a plugin
class GifImagePlugin:
    def _accept(header):
        return header.startswith(b'GIF')
    class GifImageFile(ImageFile):
        pass

class PngImagePlugin:
    def _accept(header):
        return header.startswith(b'PNG')
    class PngImageFile(ImageFile):
        pass

# Plugins registered dynamically
# New formats added without changing core code!
```

**Benefits:**
-Modular design
-Easy to extend
 Only loads formats used
 Community can contribute formats

---

### Template Method Pattern

**Problem:** All file formats need similar loading:
1. Open file
2. Parse header
3. Load image data
4. Close file

**Pillow's solution:**
```python
class ImageFile(Image):
    def load(self):
        # Step 1: Open - standard
        # Step 2: Parse header - format-specific!
        self._open()
        # Step 3: Load data - standard
        self._load()
        # Step 4: Close - standard
        self.fp.close()
    
    def _open(self):
        raise NotImplementedError()  # Subclass must implement

class GifImageFile(ImageFile):
    def _open(self):  # Only implement this!
        # GIF-specific parsing
        pass  # Everything else inherited
```

**Benefits:**
- ✓ Reduces code duplication
- ✓ Enforces process consistency
- ✓ Easy to add new formats

---

##  Class Hierarchy (Simplified)

```
                    Image
                  (Core API)
                      ↑
                      │ inherits
                      │
                  ImageFile
                 (File Base)
                      ↑
        ┌─────────────┼─────────────┐
        │             │             │
    GifImageFile  PngImageFile  JpegImageFile
    (GIF Parsing) (PNG Parsing) (JPEG Parsing)


                   Filter (ABC)
              (Abstract Base)
                      ↑
        ┌─────────────┼─────────────┐
        │             │             │
  GaussianBlur   MedianFilter   Kernel
  (Blur Effect)  (Noise Removal) (Convolution)
        
+ Your custom filters inherit here! →
  VignetteFilter, SepiaToneFilter
```

---

## 💡 Interview Questions & Answers

### Q1: "What OOP principle does GifImageFile demonstrate?"
**A:** **Inheritance** - GifImageFile inherits from ImageFile, reusing the file loading template and only implementing GIF-specific parsing in `_open()`.

### Q2: "Why can we treat PNG and JPEG files the same way in code?"
**A:** **Polymorphism** - Both PngImageFile and JpegImageFile inherit from ImageFile and implement `_open()`. Users call `Image.open()` which returns the correct subclass, and both work via the same interface.

### Q3: "What does `_ensure_mutable()` demonstrate?"
**A:** **Encapsulation** - It's a private method that validates internal state before allowing modifications, protecting the image data from corruption.

### Q4: "Why does Pillow use so many different plugins?"
**A:** **Extensibility via Plugin Architecture** - Each format is isolated, making it easy to add new formats without modifying core code. It also reduces memory usage by lazy-loading.

### Q5: "What is abstraction in the context of Image.resize()?"
**A:** **Abstraction** - Users see a simple method, but it hides complex resampling algorithms, color space conversions, and C extension calls.

### Q6: "How does the Template Method pattern help here?"
**A:** It defines the file loading algorithm in ImageFile.load(), and subclasses only implement `_open()`. This prevents code duplication and ensures consistency.

### Q7: "Can you extend Pillow to add your own filter?"
**A:** **Yes!** By inheriting from `ImageFilter.Filter` and implementing `filter()` method, as demonstrated in `custom_filters.py` with VignetteFilter.

### Q8: "What's the advantage of read-only properties in Image class?"
**A:** **Encapsulation** - Image dimensions and mode can't be accidentally changed, maintaining data integrity. Format conversions must go through controlled methods like `convert()`.

---

## 🎯 Key Talking Points for Presentation

### Opening (2 min)
"Pillow is a 30-year-old image library with 10,000+ GitHub stars. It's a perfect case study of professional OOP design because it balances simplicity with extensibility."

### Middle (6 min)
1. **Show class hierarchy** - Explain inheritance tree
2. **Code example** - GifImageFile vs PngImageFile comparison
3. **Custom filter demo** - Run VignetteFilter live
4. **Design decision** - Why plugins are better than monolithic code

### Ending (2 min)
"Pillow teaches us that good OOP isn't about complexity—it's about clarity, extensibility, and maintainability. By studying this library, we see how professional developers apply OOP principles in production code."

---

## Quick Facts to Memorize

- **Lines of Python Code:** ~10,000 (excluding C)
- **Supported Formats:** 30+
- **First Release:** 1995
- **Current Version:** 10.x (2026)
- **Main OOP Features:** Plugin architecture, template method, abstract base classes
- **Key Classes:** Image, ImageFile, Filter, ImageDraw
- **Design Patterns:** Plugin, Template Method, Abstract Factory

---

##  Code Demo Script

```python
# ===== LIVE DEMO =====
from PIL import Image
from custom_filters import VignetteFilter, SepiaToneFilter

# 1. Create image
print("Creating sample image...")
img = Image.new('RGB', (200, 200), 'white')

# 2. Apply custom filter (shows inheritance + polymorphism)
print("Applying VignetteFilter...")
vignette = VignetteFilter(strength=0.6)
result = img.filter(vignette)

# 3. Chain filters (polymorphism in action)
print("Chaining filters...")
final = img.filter(VignetteFilter()).filter(SepiaToneFilter())

print("✓ Success! Custom filters work perfectly.")
print("This demonstrates: Inheritance, Polymorphism, Abstraction, Encapsulation")
```



