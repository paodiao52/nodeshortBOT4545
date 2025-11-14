import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    ChatMemberHandler,
    CommandHandler
)

GROUP_ID = -1000000000000

async def cmd_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(f"当前群组 ID：{chat_id}")

async def on_user_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    member = update.chat_member
    if member.new_chat_member.status == "member":
        user = member.new_chat_member.user
        name = user.full_name

        keyboard = [
            [InlineKeyboardButton("🌐 官方网址", url="https://www.nodeshort.com")],
            [
                InlineKeyboardButton("📞 客服帮助", url="https://t.me/NodeShort001"),
                InlineKeyboardButton("🎧 活动客服", url="https://t.me/NodeShort006"),
            ],
            [
                InlineKeyboardButton("🤝 招商客服", url="https://t.me/NodeShort009"),
            ],
        ]

        text = f"欢迎 **{name}** 来到 *NodeShort!* 🎉"

        await context.bot.send_message(
            chat_id=GROUP_ID,
            text=text,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

async def main():
    TOKEN = os.getenv("BOT_TOKEN")
    print("Bot Token loaded:", bool(TOKEN))

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("id", cmd_id))
    app.add_handler(ChatMemberHandler(on_user_join, ChatMemberHandler.CHAT_MEMBER))

    print("Bot started…")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
