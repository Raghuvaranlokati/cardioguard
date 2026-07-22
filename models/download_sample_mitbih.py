import os
import sys
import urllib.request

def download_samples():
    base_url = 'https://physionet.org/files/mitdb/1.0.0/'
    records = ['100', '101', '102', '103', '104']
    extensions = ['.hea', '.dat', '.atr']
    os.makedirs('data/mit-bih', exist_ok=True)
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    print("Downloading 5 sample ECG records (15 files total)...")
    
    for record in records:
        for ext in extensions:
            filename = f"{record}{ext}"
            file_url = f"{base_url}{filename}"
            dest = f"data/mit-bih/{filename}"
            
            if os.path.exists(dest):
                print(f"File {filename} already exists. Skipping.")
                continue
                
            print(f"Fetching {filename}...")
            try:
                req = urllib.request.Request(file_url, headers=headers)
                with urllib.request.urlopen(req) as response, open(dest, 'wb') as out_file:
                    out_file.write(response.read())
            except Exception as e:
                print(f"Error fetching {filename}: {e}")
                
    print("Sample dataset preparation complete!")

if __name__ == '__main__':
    download_samples()
