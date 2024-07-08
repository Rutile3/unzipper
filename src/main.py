import argparse
from unzipper import is_zip_file, unzip_file

# mainの関数の呼び出し
def main():
    # コマンドライン引数の設定
    parser = argparse.ArgumentParser(description="zipファイルを解凍します。")
    parser.add_argument("zip_file_path", type=str, help="zipファイルのパス。")

    # コマンドライン引数の取得
    args = parser.parse_args()
    zip_file_path = args.zip_file_path

    # zipファイルなら解凍する
    if is_zip_file(zip_file_path):
        unzip_file(zip_file_path)
    else:
        print("zipファイルを指定してください。")


# mainの関数呼び出し
if __name__ == "__main__":
    main()
