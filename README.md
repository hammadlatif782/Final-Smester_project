# OOP Analysis Report — Pillow Library

**Library Name:** Pillow (PIL Fork)  
**Date:** 07 May 2026  

### Group Members
| Group Member | Student ID |
| 
| Hammad Latif | F25BDATS1M02049 |
| Mudassir Jabbar | F25BDATS1M02052 |
| Javeria Ahmad | F25BDATS1M02074 |

---

## Library Overview
Pillow is a popular Python library used for image processing and image manipulation. It serves as the modern, active version of the legacy Python Imaging Library (PIL).

### Core Capabilities
* Open & Convert: Open images and convert between various image formats.
* Geometric Transformations:** Resize, crop, and rotate images.
* Enhancements: Apply specialized filters and processing effects.
* Vector Drawing: Draw text and structural shapes directly onto pixel canvases.

### Target Audience
Pillow is widely utilized by Python developers, data scientists, AI engineers, web developers, and automation projects for handling digital image pipelines.

### Installation
Use the following command:
```bash
pip install pillow
The following text-based UML diagram maps out the complete structure of the provided system architecture, highlighting inheritance, associations, dependencies, and aggregations across the core components of Pillow:
+----------------------+
                        |     «abstract»       |
                        |       filter         |
                        +----------------------+
                                   ^
       +---------------------------+---------------------------+
       |                           |                           |
+--------------+            +--------------+            +--------------+
| Multiband    |            |   Builtin    |            |  Rankfilter  |
|   filter     |            |   filter     |            |              |
+--------------+            +--------------+            +--------------+
       ^                           ^                           ^
       | (Inherits)                | (Inherits)                | (Inherits)
+--------------+            +--------------+            +--------------+
|    Kernel    |            | MedianFilter |            | GaussianBlur |
+--------------+            +--------------+            +--------------+
                                   :
                                   : (Applies dependency via filter())
                                   v
                    +------------------------------+
                    |      Image (Main Class)      |
                    +------------------------------+
                    | - mode : str                 |
                    | - size : tuple               |
                    | - palette : palette          |
                    | - info : dict                |
                    +------------------------------+
                    | + open()                     |
                    | + save()                     |
                    | + paste()                    |
                    | + crop()                     |
                    | + resize()                   |
                    | + rotate()                   |
                    | + filter()                   |
                    | + getdate()                  |
                    +------------------------------+
                                   ^
                                   | (Inherits)
                    +------------------------------+
                    |  ImageFile (abstract base)   |
                    +------------------------------+
                    | - fp : 10                    |
                    | - formate : str              |
                    | - title : list               |
                    +------------------------------+
                    | + _open()                    |
                    | + _load()                    |
                    | + _save()                    |
                    | + load()                     |
                    | + seek()                     |
                    +------------------------------+
                                   ^
        +--------------------------+--------------------------+
        |                          |                          |
+---------------+          +---------------+          +---------------+
| GifImageFile  |          | PngImagePlugin|          | JpegImageFile |
| (GIF Formate) |          | (PNG Format)  |          | (JPEG Format) |
+---------------+          +---------------+          +---------------+
        |                          |                          |
        +----------------- + ------+------ + -----------------+
                           |               |
                           | dispatch      | 1 (name)
                           v               v
                    +------------------------------+
                    |   ImageDraw (Drawing ops)    |
                    +------------------------------+
                    | - _image : Image             |
                    | - draw : core obj            |
                    | - mode : str                 |
                    | - font : Font                |
                    +------------------------------+
                    | + line()                     |
                    | + ellipse()                  |
                    | + rectangle()                |
                    | + polygon()                  |
                    | + text()                     |
                    | + point()                    |
                    +------------------------------+
                                   |
                                   | 1 (name)
                                   v
                    +------------------------------+
                    |  ImageFont (Font Handler)    |
                    +------------------------------+
                    | - font : obj                 |
                    +------------------------------+
                    | + getsize()                  |
                    | + getmask()                  |
                    | + getbbox()                  |
                    +------------------------------+
                                   |
                                   | (Composes color data)
                                   v
                    +------------------------------+
                    | ImagePalette (color Palette) |
                    +------------------------------+
                    | - palette : bytes            |
                    | - mode : str                 |
                    +------------------------------+
                    | + getcolor()                 |
                    | + tobytes()                  |
                    | + save()                     |
                    +------------------------------+

                    +------------------------------+
                    | pluginRegistry               |
                    | (_plugins module)            |
                    +------------------------------+
                    | - Format plugins             |
                    |   (dynamic loading)          |
                    | - codec Registration         |
                    | - lazy loading support       |
                    +------------------------------+
                                   <> (Aggregates)
                                   |
         +-------------------------+-------------------------+
         |                         |                         |
  +--------------+          +--------------+          +--------------+
  |   Decoder    |          |   Encoder    |          |   Identify   |
  |    (Read)    |          |   (write)    |          |   (Detect)   |
  +--------------+          +--------------+          +--------------+
  OOP Principles Analysis
1. Classes and Objects
Pillow defines discrete entities via specialized blueprints (Classes) that capture state and behavior, which are accessed through runtime instances (Objects). The Image class serves as the main blueprint containing attributes like mode and size, while img acts as the operational object.
from PIL import Image

# Image is the class blueprint; img is the instantiated object
img = Image.open("photo.jpg")

# Performing operations on the object instance
img.show()
img.resize((300, 300))
img.save("new_photo.jpg")
2. Encapsulation
Encapsulation wraps structural data and operational states safely inside class boundaries. The developer triggers simple public method routines while structural complexities, private variables, and memory pointer states remain completely hidden from external access.
from PIL import Image

img = Image.open("photo.jpg")

# The user safely passes instructions to mutate structural alignment.
# Spatial pixel matrix recalculations execute internally without 
# exposing private properties or raw data mechanics to the caller.
img.rotate(90)
3. Inheritance
Pillow organizes specialized component variants through hierarchical parent-child inheritance trees to maximize structural code reuse. Generic parameters and data stream pipelines pass from base frameworks like ImageFile down into specific implementation sub-classes (such as PngImagePlugin, JpegImageFile, or GifImageFile), while filter styles descend from the abstract filter base module.
from PIL import ImageFile
from PIL.PngImagePlugin import PngImageFile

# PngImageFile acts as a child sub-class subclassed from ImageFile
# This allows format plugins to share core stream parameters out-of-the-box
print(issubclass(PngImageFile, ImageFile))  # Returns: True
4. Polymorphism
Polymorphism allows a single interface to execute dynamically tailored processes based on the target object's configuration. The global engine standardizes parsing with an identical file initialization call regardless of target format structures, dynamically producing the exact format plugin class under the hood.
from PIL import Image

# The same method works smoothly with different underlying image file formats
img_png = Image.open("a.png")  # Dynamically returns a PngImageFile object instance
img_jpg = Image.open("b.jpg")  # Dynamically returns a JpegImageFile object instance

# A single interface call alters execution based on the instance context
for graphic in [img_png, img_jpg]:
    graphic.load()  # Polymorphic method call customized per format subclass
    5. Abstraction
Abstraction acts to strip away intense mathematical overhead and algorithmic convolution details behind clean, descriptive commands. Multi-channel conversions and neighbor-pixel coordinate math are reduced to straightforward method calls, hiding complexity from the developer
from PIL import Image, ImageFilter

img = Image.open("photo.jpg")

# Complex mathematical image convolution algorithms are completely abstracted.
# The developer requests a blur effect without managing spatial pixel structures.
blurred_img = img.filter(ImageFilter.GaussianBlur(radius=2))



Advantages of Pillow


Easy to Learn: Simple, readable, and highly accessible API.

Beginner Friendly: Minimal setup required, making it an excellent starting point for graphics scripting.

Fast Image Processing: Leverages optimized core code underneath to ensure rapid rendering speeds.

Supports Many Formats: Native encoding, decoding, and conversion engine across a comprehensive format registry.

Good Documentation: Thorough, clear, and well-maintained developer references.

Works with NumPy and OpenCV: Directly bridges multi-dimensional numerical spaces with computer vision ecosystems.

Conclusion
Pillow is an outstanding Python library for image processing that demonstrates core Object-Oriented Programming (OOP) concepts such as encapsulation, inheritance, polymorphism, and abstraction. Its robust architecture provides developers with a highly modular, maintainable, and efficient framework for image engineering.