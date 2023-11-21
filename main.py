import asyncio

from aiohttp import ClientWebSocketResponse
from mipac.models.notification import NotificationNote
from mipa.ext import commands
from mipac.models.note import Note
import os
from dotenv import load_dotenv

# envファイル読み込み
load_dotenv()

# cogs読み込み
COGS = ["cogs.basic"]


# メイン
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__()

    # チャンネル接続
    async def _connect_channel(self):
        # ホーム
        await self.router.connect_channel(["main", "home"])

    # 接続
    async def on_ready(self, ws: ClientWebSocketResponse):
        print(f"connected: {self.user.username}")
        await self._connect_channel()
        for cog in COGS:
            await self.load_extension(cog)

    # ノート獲得
    async def on_note(self, message: Note):
        print(message.author.username, message.content)

    # サーバーの接続が切れたとき
    async def on_reconnect(self, ws: ClientWebSocketResponse):
        print("サーバーとの接続をロストしました。再接続します。")
        await self._connect_channel()


if __name__ == "__main__":
    bot = MyBot()
    asyncio.run(bot.start(os.environ["BOT_URL"], os.environ["BOT_KEY"]))
