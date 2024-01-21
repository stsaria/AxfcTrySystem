# Axfc Try System
## 概要
現在Axfcでは特定のサブドメイン(https://サブドメイン.axfc.net) でしかダウンロードできない時があります。

Axfc Try SystemではAxfcのサブドメインをすべて試すというシステムです。

別にそんなに難しいコードではありませんｗ
## 試すサブドメイン
```
pepper
saffron
mars
taurus
aquarius
aries
earth
jupiter
mercury
venus
emerald
sapphire
peridot
opal
ape
gorilla
monkey
chimpanzee
capricomus
pisces
capricornus
gemini
diamond
pearl
aquamarine
fenrir
```
## 使用方法
1. Python3をダウンロード(https://www.python.org/downloads/)
2. Gitをインストール(https://www.git-scm.com/downloads)
3. ソースコードをダウンロード
```
git clone https://github.com/stsaria/AxfcTrySystem.git
```
4. ライブラリをインストール
```
pip3 install -r requirements.txt
```
5. axfc_try_system.pyを実行
```
python3 -u axfc_try_system.py
Axfc DL URLを入力してください : https://hoge.axfc.net/d/fuga/piyo.rar
```
ダウンロードに成功したらその後のサブドメインを無視し終了します。
もしその後のサブドメインを無視したくない場合は"-all"引数を追加してください。
## 引数
"-all" すべてのサブドメインでのダウンロードを試す(ダウンロードに成功した後も) ```python3 -u axfc_try_system.py -all```
