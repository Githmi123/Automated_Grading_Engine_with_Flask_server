import os
import requests
import asyncio

async def download_markingscheme(scheme_url, save_dir):
    os.makedirs(save_dir, exist_ok=True)

    response = requests.get(scheme_url)
    if response.status_code == 200:
        
        with open(os.path.join(save_dir, "marking_scheme.xlsx"), "wb+") as f:
            f.write(response.content)
            print("Marking scheme downloaded successfully.")

    else:
        print(f"Failed to download the marking scheme: Status code:{response.status_code}")