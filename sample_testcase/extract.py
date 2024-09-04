import os
import zipfile

def unzip_to_folder(zip_file_path):
    # 獲取 ZIP 檔案的名稱（不含副檔名）
    folder_name = os.path.splitext(os.path.basename(zip_file_path))[0]
    
    # 新增資料夾
    os.makedirs(folder_name, exist_ok=True)
    
    # 解壓縮 ZIP 檔案
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(folder_name)

def find_and_unzip_zip_files(start_directory):
    for root, dirs, files in os.walk(start_directory):
        for file in files:
            if file.endswith('.zip'):
                zip_file_path = os.path.join(root, file)
                unzip_to_folder(zip_file_path)

# 使用範例
find_and_unzip_zip_files('zip_ex')
