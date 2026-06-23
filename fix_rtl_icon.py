import os
import glob

def replace_in_file(filepath, old_str, new_str):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

def main():
    files = glob.glob('c:/Users/Shalani A/Documents/Shalan/Client Projects(JUNE)/Aquarium Fish & Reef Supply Store/Aquarium_Fish_Reef_Supply_Store/*.html')
    files.append('c:/Users/Shalani A/Documents/Shalan/Client Projects(JUNE)/Aquarium Fish & Reef Supply Store/Aquarium_Fish_Reef_Supply_Store/update_toggles.py')
    
    for f in files:
        replace_in_file(f, '"bi bi-translate"', '"bi bi-arrow-left-right"')

if __name__ == '__main__':
    main()
