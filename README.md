# 注意
- こちらのBotは、Beta版です。
- 参考にしてもらってもいいですが、たぶんそんな使えるBotではないよ(
- このBotを*悪用*しないでください。
# スペシャルサンクス
- https://github.com/yupix/MiPA
- Yupixさんありがとうございます！
# 使い方
1. このリポジトリを git clone する
2. Python3.11(pipも)と、screenをインストール
3. envファイルをコピーする
```
python3.11 -m pip install MiPA
cp env.example .env
```
4. .envファイルの中身を編集する(これをしないと動きません)
```
# MisskeyのBotのインスタンスのURL
BOT_URL=wss://example.com/streaming
# Bot用のキー
BOT_KEY=1234567890
```
5. ./start.shを実行
6. 楽しむ！
