
# 開発ガイド

## 📗 概要

この文書は「unzipper」の開発ガイドです。

## 📝 単体テスト

仮想環境を起動し、以下のコマンドを実行してください。

``` powershell
\unzipper> pytest tests
```

## 💾 exe化

仮想環境を起動し、以下のコマンドを実行してください。

``` powershell
pyinstaller .\main.py --clean --onefile --name=unzipper.exe
```
