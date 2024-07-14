import os
import zipfile


# zipファイルか確認します。
def is_zip_file(file_path):
    return os.path.isfile(file_path) and file_path.lower().endswith(".zip")


# zipファイルを解凍します。
def unzip_file(file_path, extract_to=None):
    if extract_to is None:
        extract_to = os.path.splitext(file_path)[0]
    else:
        basename_without_ext = os.path.splitext(os.path.basename(file_path))[0]
        extract_to = os.path.join(extract_to, basename_without_ext)

    # zipファイルの解凍
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        print(f"「{file_path}」の解凍開始…")
        zip_ref.extractall(extract_to)
        print(f"「{file_path}」の解凍終了…")

        # 解凍したファイルを返す
        extracted_files = zip_ref.namelist()
        return len(extracted_files)
