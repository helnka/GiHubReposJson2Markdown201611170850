# このソフトウェアについて

GiHubReposJson2Markdown201611170850は私個人が学習目的で作成したソフトウェアである。

GitHubのリポジトリ一覧を取得したjsonファイルをMarkdownファイルに変換する。

# 開発環境

* Windows XP Pro SP3 32bit
    * cmd.exe(ConEmu/Nyagos)
* [Python 3.4.4](https://www.python.org/downloads/release/python-344/)

# 設定

1. 以前作成した[json取得スクリプト](https://github.com/ytyaru/GiHubApi.Repositories.Get.201611131629)を実行してjsonファイルを作成しておく
1. 今回作成した`json2md.py`内の`username`変数を上記で使用したユーザ名と同じものにする

## ユーザ名の設定

```python

username = 'GitHubUserName'

```

# 実行

```sh

python json2md.py

```

`GitHub.{username}.Repositories.json`ファイルを読み取り、`GitHub.{username}.Repositories.md`ファイルを書き出す。

# ライセンス #

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

このソフトウェアは以下のソフトウェアを使用している。

software|License
--------|-------
[Python 3.4.4](https://www.python.org/downloads/release/python-344/)|[PSF License (Python Software Foundation License)](https://docs.python.org/3/license.html)
