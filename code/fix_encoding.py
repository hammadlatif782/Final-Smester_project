#!/usr/bin/env python
# Fix encoding issues in PILLOW_OOP_ANALYSIS.md

import re

# Read file as binary
with open('PILLOW_OOP_ANALYSIS.md', 'rb') as f:
    content = f.read()

# Try UTF-8 first, fall back to latin1
try:
    text = content.decode('utf-8')
except:
    try:
        text = content.decode('latin-1')
    except:
        text = content.decode('utf-8', errors='replace')

# Remove any non-ASCII character
text = re.sub(r'[^\x00-\x7F]', '', text)

# Write back with UTF-8 encoding
with open('PILLOW_OOP_ANALYSIS.md', 'w', encoding='utf-8') as f:
    f.write(text)

print('Successfully fixed encoding in PILLOW_OOP_ANALYSIS.md')

# Verify
try:
    with open('PILLOW_OOP_ANALYSIS.md', 'r') as f:
        _ = f.read()
    print('File can be read with default encoding')
except Exception as e:
    print(f'Still has issues: {e}')
