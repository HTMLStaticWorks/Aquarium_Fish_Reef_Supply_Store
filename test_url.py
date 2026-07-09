import urllib.request
urls = [
    "https://images.pexels.com/photos/1894297/pexels-photo-1894297.jpeg",
    "https://images.pexels.com/photos/3151392/pexels-photo-3151392.jpeg",
    "https://images.pexels.com/photos/1230416/pexels-photo-1230416.jpeg",
    "https://images.pexels.com/photos/2156311/pexels-photo-2156311.jpeg",
    "https://images.pexels.com/photos/10834372/pexels-photo-10834372.jpeg"
]
for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req)
        print(f"OK: {u}")
    except Exception as e:
        print(f"ERR {u}: {e}")
