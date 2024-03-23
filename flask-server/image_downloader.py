import requests
import os
from image_processing import fetch_image_urls_from_server

def download_images(image_urls, save_dir):
    os.makedirs(save_dir, exist_ok= True)
    
    for i, url in enumerate(image_urls):
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(save_dir, f"image_{i}.jpg"), 'wb') as f:
                f.write(response.content)
                print(f"Image {i} downloaded successfully.")

        else:
            print(f"Failed to download image {i}. Status code: {response.status_code}")

if __name__ == "__main__":
    image_urls = fetch_image_urls_from_server()
    # image_urls = ['https://example.com/image1.jpg', 'https://example.com/image2.jpg']
    save_dir = 'downloaded_images'
    download_images(image_urls, save_dir)