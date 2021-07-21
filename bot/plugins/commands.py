#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = "<b>🌈കിടിലം സിനിമകൾ കിട്ടാന്‍ വേണ്ടി ജോയിൻ ചെയ്യൂ🌈                          ➖➖➖➖〽️➖➖➖➖➖➖                          GROUP @cinimakottaka_official                         ➖➖➖➖➖〽️➖➖➖➖➖➖                          CHANNELS @cinimakottaka_official1                             🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆                      @cinimakottaka_official2                      🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆                         @cinimakottaka_official4                          🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆                           LIKE ✴️ SHARE ✴️ SUBSCRIBE</b>                                    copyright act 2020-2021   feedback @asifpmn " ,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'join channel🎭', url="https://t.me/Cinimakottakaofficial"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('GROUP🔥', url='https://t.me/cinimakottaka_official'),
        InlineKeyboardButton('channel 1🌈', url ='https://t.me/cinimakottaka_official1')
    ],[
        InlineKeyboardButton('channel 2🌈', url='https://t.me/Cinimakottaka_official4')        
    ],[
        InlineKeyboardButton('channel 3🌈', url='https://t.me/Cinimakottakaofficial2')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('വീട് ⚡', callback_data='start'),
        InlineKeyboardButton('എബൗട്ട് 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('ക്ലോസ് 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('വീട് ⚡', callback_data='start'),
        InlineKeyboardButton('ക്ലോസ് 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
