"""Simple bot implementation"""
import telebot
import os
from pyyoutube import Api

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))
api = Api(api_key=os.getenv('API_KEY'))


@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Sends a greeting to user"""
    bot.reply_to(message, "Hi, what will your request be?")


@bot.message_handler(commands=['help'])
def send_help(message):
    """Sends a greeting to user"""
    bot.reply_to(message, "Enter key words and you will see \
the most appproptiate videos.")


def get_rating(result):
    """Calculates rating by multiplying likes and comments"""
    video_by_id = api.get_video_by_id(video_id=result.id.videoId)
    if video_by_id is None:
        return -1
    first = video_by_id.items[0].statistics.likeCount
    if first is None:
        first = 1
    second = video_by_id.items[0].statistics.commentCount
    if second is None:
        second = 1
    return int(first) * int(second)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """Answers the message"""
    req = ','.join(message.text.split())
    r = api.search_by_keywords(q=req, search_type=["video"], count=100)
    r.items.sort(key=get_rating)

    if len(r.items) == 0:
        bot.reply_to(message, "Sorry, I didn't find any videos")
        return

    top = []
    if len(r.items) <= 3:
        top = r.items
    else:
        top = r.items[-3:]
    top.reverse()

    answer = ""
    for res in top:
        answer += f"Url: https://www.youtube.com/watch?v={res.id.videoId}\n"
        answer += "Title: " + res.snippet.title + '\n'
        video_by_id = api.get_video_by_id(video_id=res.id.videoId)
        if video_by_id.items[0].snippet.defaultAudioLanguage is not None:
            s = video_by_id.items[0].snippet.defaultAudioLanguage
            answer += f"The language of the video is {s}\n"
        if video_by_id.items[0].contentDetails.caption == 'true':
            answer += "This video has subtitles!\n\n"
        else:
            answer += "There is no subtitles in this video :(\n\n"
    bot.reply_to(message, answer)


bot.infinity_polling()
