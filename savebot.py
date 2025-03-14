# from background import keep_alive
# from dotenv import load_dotenv
# import yt_dlp
# import os
# import asyncio
# from aiogram import Bot, Dispatcher, types, F, Router, html
# import nest_asyncio
# nest_asyncio.apply()


# load_dotenv()
# bot = Bot(os.getenv('TOKENSAVEBOT'))
# dp = Dispatcher()


# def get_direct_link(video_url):
#     ydl_opts = {
#         'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
#         'quiet': True,
#         'no_warnings': True,
#         'outtmpl': '%(id)s.%(ext)s',
#         'merge_output_format': 'mp4'
#     }
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info_dict = ydl.extract_info(video_url, download=False)
#     L = info_dict['formats']
#     for x in range(len(L)):
#         if L[x].get('height', 0) == 1280:
#             direct_link = L[x]['url']
#             return direct_link


# @dp.message(F.text == '/start')
# async def handler(message):
#     await message.reply(f'Добро пожаловать, {message.from_user.username}!\nОтправь ссылку на видео с Youtube или TikTok - через пару секунд видео будет у вас!\nНа данный момент, я поддерживаю только видео из Youtube или TikTok')


# @dp.message(F.text.regexp(r'^https:\/\/(www\.youtube.*|youtu\.be.*|youtube\.com.*)'))
# async def handler(message):
#     url = str(message.text)
#     direct_link = get_direct_link(url)
#     text = html.link('Вот, лови', html.quote(direct_link))
#     await message.answer(text, parse_mode="HTML")

# if __name__ == '__main__':
#     # keep_alive()
#     loop = asyncio.get_event_loop()
#     loop.create_task(dp.start_polling(bot, skip_updates=True))
#     loop.run_forever()
