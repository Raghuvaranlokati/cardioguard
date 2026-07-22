import os
import sys
import urllib.request
import zipfile

def download():
    url = 'https://physionet.org/static/published-projects/mitdb/mit-bih-arrhythmia-database-1.0.0.zip'
    
    # Use a custom user agent to avoid rate-limiting/blocking by PhysioNet
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    )
    
    os.makedirs('data/mit-bih', exist_ok=True)
    zip_path = 'data/mit-bih/mit_bih.zip'
    
    print('Downloading MIT-BIH Arrhythmia Database...')
    try:
        with urllib.request.urlopen(req) as response, open(zip_path, 'wb') as out_file:
            total_size = int(response.info().get('Content-Length', 0))
            downloaded = 0
            while True:
                chunk = response.read(1024 * 1024)  # 1MB chunks
                if not chunk:
                    break
                out_file.write(chunk)
                downloaded += len(chunk)
                percent = (downloaded / total_size) * 100 if total_size > 0 else 0
                sys.stdout.write(f"\rProgress: {percent:.2f}% ({downloaded / (1024*1024):.2f} MB / {total_size / (1024*1024):.2f} MB)")
                sys.stdout.flush()
        print('\nDownload complete! Starting extraction...')
        
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall('data/mit-bih')
        
        os.remove(zip_path)
        print('Extraction complete! Files are ready.')
    except Exception as e:
        print(f"\nError: {e}")
        if os.path.exists(zip_path):
            os.remove(zip_path)

if __name__ == '__main__':
    download()
