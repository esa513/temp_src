import zipfile
import os


def keep_specific_files_in_zip(zip_path):
    # 创建一个临时 ZIP 文件
    temp_zip_path = zip_path + '.tmp'

    # 需要保留的文件列表
    files_to_keep = {'1.in', '1.out', '2.in', '2.out'}

    with zipfile.ZipFile(zip_path, 'r') as zip_read:
        with zipfile.ZipFile(temp_zip_path, 'w') as zip_write:
            for item in zip_read.infolist():
                if item.filename in files_to_keep:
                    # 复制需要保留的文件
                    zip_write.writestr(item, zip_read.read(item.filename))

    # 替换原始 ZIP 文件
    os.remove(zip_path)
    zip_name = f"{zip_path.split('_')[0]}_sample_testcase.zip"
    os.rename(temp_zip_path, zip_name)


# 使用示例
for folder in os.listdir("."):
    if folder.split(".")[1] == "zip":
        print(folder)
        keep_specific_files_in_zip(folder)
