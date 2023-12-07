from bot.bot import Bot
from config import conf, load_config
from common.log import logger
from common.expired_dict import ExpiredDict
import time
import sys

import asyncio
import json

from EdgeGPT import Chatbot, ConversationStyle

class BingBot(Bot):

    def __init__(self, cookiePath='/home/jace/.config/cookie.json'):
        self.cookiePath = cookiePath
        # additional initialization code here, if needed
        self.bot = Chatbot(cookiePath)

    async def ask(self, question):
        response = await self.bot.ask(prompt=question, conversation_style=ConversationStyle.balanced)
        return get_bot_response_text(response)

    def reply(self, query, context=None):
        """
        bot auto-reply content
        :param req: received message
        :return: reply content
        """
        return asyncio.run(self.ask(query))
    

def get_bot_response_text(res):

    messages = res.get('item', {}).get('messages', [])

    for message in messages:

        if message.get('author') == 'bot':

            return message.get('text')

    return None