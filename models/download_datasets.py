import os
import urllib.request
import zipfile
import sys

# Define dataset URLs on PhysioNet
DATASETS = {
    "ptb-xl": {
        "url": "https://physionet.org/static/published-projects/ptb-xl/ptb-xl-a-large-publicly-available-electrocardiography-database-1.0.3.zip",
        "filename": "ptb_xl_database.zip",
        "extract_to": "data/ptb-xl"
    },
    "mit-bih": {
        "url": "https://physionet.org/static/published-projects/mitdb/mit-bih-arrhythmia-database-1.0.0.zip",
        "filename": "mit_bih_database.zip",
        "extract_to": "data/mit-bih"
    },
    "cinc-2021": {
        "url": "https://physionet.org/static/published-projects/challenge-2021/1.0.3/training-1.0.3.zip",
        "filename": "cinc_2021_challenge.zip",
        "extract_to": "data/cinc-2021"
    }
}

def report_progress(block_num, block_size, total_size):
    """
    Callback function to display download progress in the console.
    """
    downloaded = block_num * block_size
    if total_size > 0:
        percent = min(100, (downloaded / total_size) * 100)
        sys.stdout.write(f"\rDownloading... {percent:.2f}% ({downloaded / (1024 * 1024):.2f} MB / {total_size / (1024 * 1024):.2f} MB)")
    else:
        sys.stdout.write(f"\rDownloading... {downloaded / (1024 * 1024):.2f} MB")
    sys.stdout.flush()

def download_and_extract(dataset_name):
    """
    Downloads and extracts a zip-based dataset.
    """
    if dataset_name not in DATASETS:
        print(f"Error: Dataset '{dataset_name}' is not recognized.")
        return

    info = DATASETS[dataset_name]
    os.makedirs(info["extract_to"], exist_ok=True)
    
    zip_path = os.path.join(info["extract_to"], info["filename"])

    # Step 1: Download
    if not os.path.exists(zip_path):
        print(f"\nFetching {dataset_name} from: {info['url']}")
        try:
            urllib.request.urlretrieve(info["url"], zip_path, report_progress)
            print(f"\nSuccessfully downloaded {dataset_name} to {zip_path}")
        except Exception as e:
            print(f"\nFailed to download {dataset_name}. Error: {e}")
            return
    else:
        print(f"\nArchive already exists for {dataset_name} at {zip_path}. Skipping download.")

    # Step 2: Extract
    print(f"Extracting {zip_path} to {info['extract_to']}... This may take a few minutes.")
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Get list of files
            files = zip_ref.namelist()
            total_files = len(files)
            for idx, file in enumerate(files, 1):
                zip_ref.extract(file, info["extract_to"])
                if idx % 500 == 0 or idx == total_files:
                    sys.stdout.write(f"\rExtracting... {idx}/{total_files} files ({(idx/total_files)*100:.1f}%)")
                    sys.stdout.flush()
        print(f"\nExtraction complete for {dataset_name}!")
        
        # Clean up zip archive to save disk space
        os.remove(zip_path)
        print(f"Removed archive {zip_path} to conserve space.")
    except Exception as e:
        print(f"\nFailed to extract {dataset_name}. Error: {e}")

if __name__ == "__main__":
    print("=== CardioGuard Dataset Downloader ===")
    print("This utility will download and extract the required ECG databases.")
    print("WARNING: These downloads are large and can take considerable time.")
    print("Options:")
    print("1. PTB-XL Database (~1.7 GB)")
    print("2. MIT-BIH Arrhythmia Database (~70 MB)")
    print("3. PhysioNet Challenge 2021 (~2.5 GB)")
    print("4. Download All")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    # Establish root data folder
    os.makedirs("data", exist_ok=True)
    
    if choice == '1':
        download_and_extract("ptb-xl")
    elif choice == '2':
        download_and_extract("mit-bih")
    elif choice == '3':
        download_and_extract("cinc-2021")
    elif choice == '4':
        download_and_extract("ptb-xl")
        download_and_extract("mit-bih")
        download_and_extract("cinc-2021")
    else:
        print("Invalid choice. Exiting.")
