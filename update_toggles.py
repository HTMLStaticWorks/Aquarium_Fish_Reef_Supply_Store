import os
import glob
from bs4 import BeautifulSoup

def process_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    modified = False

    # 1. Update existing toggles in the header
    controls = soup.find('div', class_='controls')
    if controls:
        theme_btn = controls.find('button', id='theme-toggle')
        if theme_btn and 'header-controls-btn' not in theme_btn.get('class', []):
            theme_btn['class'] = theme_btn.get('class', []) + ['header-controls-btn', 'theme-toggle']
            modified = True
        
        rtl_btn = controls.find('button', id='rtl-toggle')
        if rtl_btn and 'header-controls-btn' not in rtl_btn.get('class', []):
            rtl_btn['class'] = rtl_btn.get('class', []) + ['header-controls-btn', 'rtl-toggle']
            modified = True

    # 2. Add toggles to offcanvas menu
    offcanvas = soup.find('div', id='mobileMenu')
    if offcanvas:
        offcanvas_body = offcanvas.find('div', class_='offcanvas-body')
        if offcanvas_body and not offcanvas_body.find('div', class_='mobile-toggles'):
            toggles_html = """
            <div class="mobile-toggles mt-auto pt-4 border-top border-secondary d-flex justify-content-center gap-3">
                <button class="theme-btn theme-toggle btn btn-outline-secondary rounded-circle" style="width: 50px; height: 50px;"><i class="bi bi-sun-fill"></i></button>
                <button class="rtl-btn rtl-toggle btn btn-outline-secondary rounded-circle" style="width: 50px; height: 50px;"><i class="bi bi-translate"></i></button>
            </div>
            """
            toggles_soup = BeautifulSoup(toggles_html, 'html.parser')
            inner_flex = offcanvas_body.find('div', class_='d-flex flex-column')
            if inner_flex:
                inner_flex.append(toggles_soup)
            else:
                offcanvas_body.append(toggles_soup)
            modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Updated {filepath}")

html_files = glob.glob("*.html")
for f in html_files:
    process_html_file(f)
print("Done processing HTML files.")
