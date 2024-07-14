import argparse
from unzipper import is_zip_file, unzip_file


# mainの関数の呼び出し
def main():
    # コマンドライン引数の設定
    parser = argparse.ArgumentParser(description="zipファイルを解凍します。")
    parser.add_argument("input_files", nargs="+", help="解凍するzipファイルのパス。")

    # コマンドライン引数の取得
    args = parser.parse_args()
    input_files = args.input_files

    # zipファイルなら解凍する
    for input_item in input_files:
        if is_zip_file(input_item):
            unzip_file(input_item)
        else:
            print(f"「{input_item}」はzipファイルをではありません。")


# mainの関数呼び出し
if __name__ == "__main__":
    main()
