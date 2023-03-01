# -*- coding: utf-8 -*-
import telebot
from telebot import types
import time
import os

import src.config as config
from .multi_process import WorkerThread


bot = telebot.TeleBot(token=config._token_, parse_mode='Markdown')
wt = WorkerThread()