import requests
import os
# from image_processing import fetch_image_urls_from_server

def download_images(image_urls, indexNos, save_dir):
    os.makedirs(save_dir, exist_ok= True)
    
    for i, url in enumerate(image_urls):
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(save_dir, f"image_{indexNos[i]}.jpg"), 'wb') as f:
                f.write(response.content)
                print(f"Image {indexNos[i]} downloaded successfully.")

        else:
            print(f"Failed to download image {i}. Status code: {response.status_code}")

# if __name__ == "__main__":
#     # image_urls = fetch_image_urls_from_server()
#     image_urls = [ 
#                   'https://www.google.com/url?sa=i&url=https%3A%2F%2Flevel.game%2Fblogs%2F13-great-life-lessons-from-lord-ganesha&psig=AOvVaw0bz9cAL4_gFN_AbwidD3gR&ust=1714979280949000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCPiuyOf59YUDFQAAAAAdAAAAABAJ']
#     save_dir = 'downloaded_images'
#     download_images(image_urls, save_dir)
    