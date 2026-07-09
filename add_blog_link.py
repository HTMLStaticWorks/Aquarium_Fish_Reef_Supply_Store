import glob
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Look for the Services link in the offcanvas and insert Blog after it
    # We will use regex to find the Services link inside the offcanvas-body
    
    # We know the exact string from index.html:
    target = '<a href="services.html" class="text-decoration-none" style="color: var(--text-color)">Services</a>'
    blog_link = '<a href="blog.html" class="text-decoration-none" style="color: var(--text-color)">Blog</a>'
    
    if target in content and blog_link not in content:
        # Just replace the first occurrence of target inside offcanvas-body? 
        # Actually there is only one mobile menu per page. 
        # Wait, there's a desktop menu too!
        # The desktop menu has <a class="nav-link" href="services.html">Services</a>
        # So our target string with `class="text-decoration-none" style="color: var(--text-color)"` is unique to the mobile menu!
        
        new_content = content.replace(target, target + '\n                ' + blog_link)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

for f in glob.glob("*.html"):
    process_file(f)
