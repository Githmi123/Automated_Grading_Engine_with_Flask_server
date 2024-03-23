import requests

def fetch_image_urls_from_server():
    url = 'http ://localhost:5000/image_urls'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        image_urls = data.get('image_urls', [])
        return image_urls
    
    else:
        print(f"Failed to fetch image URLs. Status code: {response.status_code}")
        return []
    


image_urls = fetch_image_urls_from_server()
print("Image URLs fetched from server: ")

for url in image_urls:
    print(url)