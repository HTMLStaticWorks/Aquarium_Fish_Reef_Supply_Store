import os
import glob
from bs4 import BeautifulSoup

def process_html_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    modified = False

    # 1. Update Navigation classes
    for nav in soup.find_all('nav', class_='d-none d-lg-flex'):
        nav['class'] = ['header-nav']
        modified = True

    # 2. Update Auth Button
    for btn in soup.find_all('a', href='signup.html'):
        if 'btn-primary-custom' in btn.get('class', []):
            if 'd-none' in btn['class']:
                btn['class'].remove('d-none')
            if 'd-md-inline-block' in btn['class']:
                btn['class'].remove('d-md-inline-block')
            if 'header-auth-btn' not in btn['class']:
                btn['class'].append('header-auth-btn')
                modified = True

    # 3. Add mobile toggle button
    controls = soup.find('div', class_='controls')
    if controls and not controls.find('button', class_='mobile-toggle-btn'):
        toggle_btn = soup.new_tag('button', type='button', **{
            'class': 'btn btn-outline-secondary mobile-toggle-btn ms-2',
            'data-bs-toggle': 'offcanvas',
            'data-bs-target': '#mobileMenu',
            'style': 'display: none;'
        })
        icon = soup.new_tag('i', **{'class': 'bi bi-list fs-3'})
        toggle_btn.append(icon)
        controls.append(toggle_btn)
        modified = True

    # 4. Add offcanvas menu if missing
    header = soup.find('header', class_='header')
    if header and not soup.find(id='mobileMenu'):
        offcanvas_html = """
        <div class="offcanvas offcanvas-end" tabindex="-1" id="mobileMenu" style="background-color: var(--bg-color);">
            <div class="offcanvas-header border-bottom border-secondary">
                <h5 class="offcanvas-title fw-bold"><i class="bi bi-water text-secondary-custom"></i> Aquaria.</h5>
                <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close" style="filter: invert(var(--bs-body-color-rgb));"></button>
            </div>
            <div class="offcanvas-body">
                <div class="d-flex flex-column gap-3 fs-5">
                    <a href="index.html" class="text-decoration-none" style="color: var(--text-color)">Home 1</a>
                    <a href="home-2.html" class="text-decoration-none" style="color: var(--text-color)">Home 2</a>
                    <a href="about.html" class="text-decoration-none" style="color: var(--text-color)">About</a>
                    <a href="services.html" class="text-decoration-none" style="color: var(--text-color)">Services</a>
                    <a href="gallery.html" class="text-decoration-none" style="color: var(--text-color)">Gallery</a>
                    <a href="pricing.html" class="text-decoration-none" style="color: var(--text-color)">Pricing</a>
                    <a href="contact.html" class="text-decoration-none" style="color: var(--text-color)">Contact</a>
                    <a href="login.html" class="btn-primary-custom text-center mt-4">Login</a>
                </div>
            </div>
        </div>
        """
        offcanvas_soup = BeautifulSoup(offcanvas_html, 'html.parser')
        header.insert_after(offcanvas_soup)
        modified = True

    # 5. Fix row containment
    for row in soup.find_all(class_='row'):
        # Exclude rows already inside a container or container-fluid
        parent_container = row.find_parent(class_=['container', 'container-fluid'])
        # Also exclude rows that are specifically meant to be edge-to-edge if they have gx-0 or similar,
        # but the prompt asked to contain all of them to prevent overflow.
        if not parent_container:
            # Wrap the row
            wrapper = soup.new_tag('div', **{'class': 'container-fluid overflow-hidden'})
            row.wrap(wrapper)
            modified = True
            
    # 6. Wrap tables
    for table in soup.find_all('table'):
        parent = table.parent
        if not parent or 'table-responsive' not in parent.get('class', []):
            wrapper = soup.new_tag('div', **{'class': 'table-responsive w-100'})
            table.wrap(wrapper)
            modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Updated {filepath}")

html_files = glob.glob("*.html")
for f in html_files:
    process_html_file(f)
print("Done processing HTML files.")
