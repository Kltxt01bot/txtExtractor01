#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "27176895"))
    API_HASH = os.environ.get("API_HASH", "b24b9b0b05a9fb4e117f6c736cd69ecf")
    AUTH_USERS = os.environ.get("AUTH_USERS", "")
