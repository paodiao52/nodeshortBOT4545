import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    ChatMemberHandler,
    CommandHandler,
)

GROUP_ID = -1000000000000     # 你自己的群ID


# =========================
# /id 命令（新版写法）
# =========================
async def cmd_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(f"当前群组 ID: {chat_id}")


# =========================
# 监听新成员加入（新版 20.x 写法）
# =========================
async def on_user_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_member = update.chat_member

    # 触发条件：成员从 "left" → "member"
    if chat_member.old_chat_member.status in ["left", "kicked"] and \
       chat_member.new_chat_member.status == "member":

        user = chat_member.new_chat_member.user
        name = user.full_name

        keyboard = [
            [InlineKeyboardButton("🌐 官网网址", url="https://www.nodeshort.com")],
            [
                InlineKeyboardButton("📞 客服帮助", url="https://t.me/NodeShort001"),
                InlineKeyboardButton("📢 活动群聊", url="https://t.me/NodeShort006"),
            ],
            [InlineKeyboardButton("🤝 招商客服", url="https://t.me/NodeShort009")],
        ]

        text = f"🎉欢迎 **{name}** 来到 *NodeShort!* 🌈"

        await context.bot.send_message(
            chat_id=GROUP_ID,
            text=text,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


# =========================
# 主程序
# =========================
async def main():
    TOKEN = os.getenv("BOT_TOKEN")
    print("Bot Token loaded:", bool(TOKEN))

    app = ApplicationBuilder().token(TOKEN).build()

    # /id 命令
    app.add_handler(CommandHandler("id", cmd_id))

    # 新成员加入监听（新版写法）
    app.add_handler(ChatMemberHandler(on_user_join, ChatMemberHandler.CHAT_MEMBER))

    print("Bot started...")
    await app.run_polling()


# =========================
# 程序入口
# =========================
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
