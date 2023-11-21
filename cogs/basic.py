import asyncio
from mipa.ext import commands
from mipa.ext.commands.bot import Bot
from mipa.ext.commands.context import Context
import mipac.errors.errors
import random


class BasicCog(commands.Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    # こんにちはなどの挨拶の時
    @commands.mention_command(regex=r"こんにちは|Hello|こんちゃ|こんにちははっはー")
    async def hello(self, ctx: Context, say: str):
        hellos = [
            f"こんにちははっはー {ctx.message.author.username} さん\n電車人間になれる方法を教えてくれませんか？",
            f"こんにちははっはー {ctx.message.author.username} さん\n:Tox:と仲良くなれる方法を教えてくれませんか？",
            f"こんにちははっはー {ctx.message.author.username} さん\nんーーーーーーーーー:neko_relax:",
            f"こんにちははっはー {ctx.message.author.username} さん\nんーーーーーーーーー:neko_tired2:",
            f"こんにちははっはー {ctx.message.author.username} さん\n通勤電車ですがカジュアルに生きたいです",
            f"こんにちははっはー {ctx.message.author.username} さん\n:hagechi:よんぱごの謎は深まるばかり...",
            f"こんにちははっはー {ctx.message.author.username} さん\n:189:こいつが影薄いと言われるのはなんでだろう？",
            f"こんにちははっはー {ctx.message.author.username} さん\n:64:こいつが死神と言われる理由が知りないな",
            f"こんにちははっはー {ctx.message.author.username} さん\n:d_4800:こいつでたらめ化するとぐちゃぐちょになるの？()",
            f"こんにちははっはー {ctx.message.author.username} さん\nそういえばろくよんってでたらめ化してないよね",
            f"こんにちははっはー {ctx.message.author.username} さん\n223系の「コンドル」は都市伝説から生まれてるぞ\n(だから公式にその名前がついたわけではない)",
        ]
        # リアクション
        await ctx.message.api.reaction.action.add(":heart:")

        # ランダムに選択
        r = random.choice(hellos)

        # ホームに投稿
        await ctx.message.api.action.reply(r, "home")

    # おやすみ(正規表現)
    @commands.mention_command(
        regex=r"おやすみ|:oyasumisskey:|:oyasumi2:|:oyasuminasai:|おやよん|おや|おやす"
    )
    async def night(self, ctx: Context, say: str):
        night = [
            f":oyasumisskey: {ctx.message.author.username} さん\nんーーーーーーーー:neko_relax:",
            f":oyasumisskey: {ctx.message.author.username} さん\n電車の夜は遅い:neko_tired2:",
            f":oyasumi2: {ctx.message.author.username} さん",
            f":oyasuminasai: {ctx.message.author.username} さん",
        ]
        nightr = [
            ":oyasumisskey:",
            ":oyasumi2:",
            ":oyasuminasai:",
        ]
        # ランダムに選択(リアクションもリプライもバラバラ)
        r = random.choice(night)
        rr = random.choice(nightr)
        # リアクション&送信
        await ctx.message.api.reaction.action.add(rr)
        await ctx.message.api.action.reply(r, "home")

    # おはよう
    @commands.mention_command(regex=r"おはよう|おはよ|:ohayoo:|:ohayo:|:ohayou:")
    async def morning(self, ctx: Context, say: str):
        morning = [
            f":ohayoo: {ctx.message.author.username} さん\nんーーーーーーーー:neko_relax:",
            f":ohayo: {ctx.message.author.username} さん\n電車の朝は早い:neko_tired2:",
            f":ohayou: {ctx.message.author.username} さん\nおはようさんさんサンデー(必ずしも日曜日とは限らない)",
            f":ohayoo: {ctx.message.author.username} さん",
            f":ohayo: {ctx.message.author.username} さん",
            f":ohayou: {ctx.message.author.username} さん",
        ]
        morningr = [
            ":ohayoo:",
            ":ohayo:",
            ":ohayou:",
        ]
        # ランダムに選択(リアクションもリプライも)
        r = random.choice(morning)
        rr = random.choice(morningr)
        # リアクション&送信
        await ctx.message.api.reaction.action.add(rr)
        await ctx.message.api.action.reply(r, "home")

    # フォローする動作
    @commands.mention_command(text="フォローして")
    async def follow(self, ctx: Context):
        # リアクション
        await ctx.message.api.reaction.action.add(":heart:")
        # フォローしてない場合は
        try:
            # フォローする
            await ctx.author.api.follow.action.add(ctx.message.author.id)
            # リプライ
            await ctx.message.api.action.reply("フォローしたぞ", "home")
        # すでにフォローしてある時にエラーが起きた場合は
        except mipac.errors.errors.AlreadyFollowingError:
            # リプライ
            await ctx.message.api.action.reply("もうフォローしてあるぞ", "home")

    # ファミリーおみくじ
    @commands.mention_command(text="よんぱちファミリーおみくじ")
    async def family(self, ctx: Context):
        # 二次元配列でリアクションとリプライを統一
        omikuji = [
            [
                f"今回の{ctx.message.author.username} さんのよんぱちファミリーおみくじの結果は...\n\n$[x3 :223:]\nです！\n :223:<人間になりたいです",
                ":223:",
            ],
            [
                f"今回の{ctx.message.author.username} さんのよんぱちファミリーおみくじの結果は...\n\n$[x3 :64:]\nです！\n :64:<廃車します",
                ":64:",
            ],
            [
                f"今回の{ctx.message.author.username} さんのよんぱちファミリーおみくじの結果は...\n\n$[x3 :485:]\nです！\n :485:<電気おいしいw",
                ":485:",
            ],
            [
                f"今回の{ctx.message.author.username} さんのよんぱちファミリーおみくじの結果は...\n\n$[x3 :189:]\nです！\n :189:<影が薄すぎる！！！",
                ":189:",
            ],
            [
                f"今回の{ctx.message.author.username} さんのよんぱちファミリーおみくじの結果は...\n\n$[x3 :Tox:]\nです！\n :Tox:<よんぱちがプログラミングの知識がなさすぎます\n悲しいです",
                ":Tox:",
            ],
            [
                f"今回の{ctx.message.author.username} さんのよんぱちファミリーおみくじの結果は...\n\n$[x3 :4800:]\nです！\n :4800:<はは、",
                ":4800:",
            ],
        ]
        # ランダム
        r = random.choice(omikuji)
        # 1列目ランダム、2列目リアクション行
        await ctx.message.api.reaction.action.add(r[:][1])
        # 1列目ランダム、2列目リプライ行
        await ctx.message.api.action.reply(r[:][0], "home")

    # ふあすきーおみくじ
    @commands.mention_command(text="ふあすきーおみくじ")
    async def homikuji(self, ctx: Context):
        # 二次元配列でリアクションとリプライを統一
        omikuji = [
            [
                f"今回の{ctx.message.author.username} さんのふあすきーおみくじの結果は...\n\n$[x3 :d_189:]\nです！\n影が薄すぎて点になってる...",
                ":d_189:",
            ],
            [
                f"今回の{ctx.message.author.username} さんのふあすきーおみくじの結果は...\n\n$[x3 :d_4800:]\nです！\nぐちゃぐちょ...なぜ",
                ":d_4800:",
            ],
            [
                f"今回の{ctx.message.author.username} さんのふあすきーおみくじの結果は...\n\n$[x3 :d_485:]\nです！\nかいぞく...？なぜ？",
                ":d_485:",
            ],
            [
                f"今回の{ctx.message.author.username} さんのふあすきーおみくじの結果は...\n\n$[x3 :d_haikei:]\nです！はいけい...？",
                ":d_haikei:",
            ],
            [
                f"今回の{ctx.message.author.username} さんのふあすきーおみくじの結果は...\n\n$[x3 :d_konnano:]\nです！\n屋根付きビル...~~なんでそういう発想に至るし~~",
                ":d_konnano:",
            ],
            [
                f"今回の{ctx.message.author.username} さんのふあすきーおみくじの結果は...\n\n$[x3 :d_marisa:]\nです！\n一応東方キャラである魔理沙もでたらめ化するんだ...~~おこられそう~~\nあと、なんで霊夢がいないのだろう？",
                ":d_marisa:",
            ],
            [
                f"今回の{ctx.message.author.username} さんのふあすきーおみくじの結果は...\n\n$[x3 :Y189:]\nです！\nゆっくりしていってね！",
                ":Y189:",
            ],
            [
                f"今回の{ctx.message.author.username} さんのふあすきーおみくじの結果は...\n\n$[x3 :Y4853000:]\nです！\nゆっくりしていってね！",
                ":Y4853000:",
            ],
            [
                f"今回の{ctx.message.author.username} さんのふあすきーおみくじの結果は...\n\n$[x3 :Y4800:]\nです！\nゆっくりしていってね！",
                ":Y4800:",
            ],
            [
                f"今回の{ctx.message.author.username} さんのふあすきーおみくじの結果は...\n\n$[x3 :Y64:]\nです！\nゆっくりしていってね！",
                ":Y64:",
            ],
            [
                f"今回の{ctx.message.author.username} さんのふあすきーおみくじの結果は...\n\n$[x3 :neko_tired2:]\nです！\nんーーーーーーーーー:neko_tired2:",
                ":neko_tired2:",
            ],
            [
                f"今回の{ctx.message.author.username} さんのふあすきーおみくじの結果は...\n\n$[x3 :neko_relax:]\nです！\nんーーーーーーーーー:neko_relax:",
                ":neko_relax:",
            ],
            [
                f"今回の{ctx.message.author.username} さんのふあすきーおみくじの結果は...\n\n$[x3 :nadeorangepizero3:]\nです！\n*やわらかSBC*",
                ":nadeorangepizero3:",
            ],
            [
                f"今回の{ctx.message.author.username} さんのふあすきーおみくじの結果は...\n\n$[x3 :nadeorangepi:]\nです！\n*やわらかおれんじ*",
                ":nadeorangepi:",
            ],
            [
                f"今回の{ctx.message.author.username} さんのふあすきーおみくじの結果は...\n\n$[x3 :guchagucho:]\nです！そーなのかー(ぐちゃぐちょ)",
                ":guchagucho:",
            ],
            [
                f"今回の{ctx.message.author.username} さんのふあすきーおみくじの結果は...\n\n$[x3 :hagechi:]\nです！\nそうなってたの？！\n~~きもい~~",
                ":hagechi:",
            ],
        ]
        # ランダム
        r = random.choice(omikuji)
        # 1列目ランダム、2列目リアクション行
        await ctx.message.api.reaction.action.add(r[:][1])
        # 1列目ランダム、2列目リプライ行
        await ctx.message.api.action.reply(r[:][0], "home")


async def setup(bot: Bot):
    await bot.add_cog(BasicCog(bot))
