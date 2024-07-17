import argparse
import os
import zipfile


# mainの関数
def main_func():
    # コマンドライン引数の設定
    parser = argparse.ArgumentParser(description="zipファイルを解凍します。")
    parser.add_argument("input_files", nargs="+", help="解凍するzipファイルのパス。")

    # コマンドライン引数の取得
    args = parser.parse_args()
    input_files = args.input_files

    # zipファイルなら解凍する
    print(f"{len(input_files)}ファイル")
    for input_item in input_files:
        if is_zip_file(input_item):
            unzip_file(input_item)
        else:
            print(f"「{input_item}」はzipファイルではありません。")

    input("enterキーでプログラムを終了します。")


# zipファイルか確認します。
def is_zip_file(file_path):
    return os.path.isfile(file_path) and file_path.lower().endswith(".zip")


# zipファイルを解凍します。
def unzip_file(file_path, extract_to=None):
    file_basename = os.path.basename(file_path)
    if extract_to is None:
        extract_to = os.path.splitext(file_path)[0]
    else:
        basename_without_ext = os.path.splitext(file_basename)[0]
        extract_to = os.path.join(extract_to, basename_without_ext)

    # zipファイルの解凍
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        print(f"解凍開始：{file_basename}")
        zip_ref.extractall(extract_to)
        print(f"解凍終了：{file_basename}")

        # 解凍したファイルを返す
        extracted_files = zip_ref.namelist()
        return len(extracted_files)


# mainの関数呼び出し
if __name__ == "__main__":
    main_func()
