# usage: python launcher.py num_shards first_shard_id:last_shard_id

import discord
from bot import PollBot
import sys

bot = PollBot()
bot.run()