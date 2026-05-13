import base64
import os

# 1. Read logo.png and convert to base64
with open('logo.png', 'rb') as f:
    logo_base64 = base64.b64encode(f.read()).decode()

logo_html = f'data:image/png;base64,{logo_base64}'

# 2. Read ml_genz_dashboard.py
with open('ml_genz_dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 3. Replace the placeholder
target = '<img src="app/static/logo.png" class="sidebar-logo">'
replacement = f'<img src="{logo_html}" class="sidebar-logo">'

if target in content:
    new_content = content.replace(target, replacement)
    with open('ml_genz_dashboard.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully injected Base64 logo!")
else:
    print("Target tag not found!")
