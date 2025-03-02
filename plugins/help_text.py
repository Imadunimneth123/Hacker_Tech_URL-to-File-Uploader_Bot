#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Hacker Tech

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

from pyrogram import filters
from database.adduser import AddUser
from pyrogram import Client as Clinton
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Clinton.on_message(filters.private & filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
       reply_markup=InlineKeyboardMarkup([
      [InlineKeyboardButton("📌️ Telegram Channel 🔎", url="https://t.me/+3Iy7Z-b-7GQxNjU1"),
        InlineKeyboardButton("📌️ Telegram Group 🔎", url="https://t.me/+XL8rf6_-8Ec1MWM1")],
         [InlineKeyboardButton("Developer 👨‍⚖️", url="https://t.me/+3Iy7Z-b-7GQxNjU1")],
         ]),
        reply_to_message_id=update.message_id
    )


@Clinton.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup([
      [InlineKeyboardButton("📌️ Telegram Channel 🔎", url="https://t.me/SL_Jana_Team"),
        InlineKeyboardButton("📌️ Telegram Group 🔎", url="https://t.me/joinchat/YiGR_JLyIG84ZmY1")],
         [InlineKeyboardButton("Developer 👨‍⚖️", url="https://t.me/SL_Jana_Team")],
         ]),
        reply_to_message_id=update.message_id
    )
