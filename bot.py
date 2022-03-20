#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ad
# Custom your logger
# 
# from nonebot.log import logger, default_format
# logger.add("error.log",
#            rotation="00:00",
#            diagnose=False,
#            level="ERROR",
#            format=default_format)

# You can pass some keyword args config to init function
nonebot.init()
app = nonebot.get_asgi()
nonebot.load_plugins('src/plugins')
# nonebot.init(apscheduler_autostart=True)
# nonebot.init(apscheduler_config={
#     "apscheduler.timezone": "Asia/Shanghai"
# })
nonebot.load_plugins('src/plugins/foo') # 这是插件的文件路，你可以跟着创建 plugins是你创建好项目后自动生成，只要在plugins里面创建个foo文件就行，在foo文件里面放py文件（只是我这里是这样创建的，你可以随意，主要得有plugins文件夹在里面）
driver = nonebot.get_driver()
driver.register_adapter(ad)
#

nonebot.load_builtin_plugins("echo")



# Please DO NOT modify this file unless you know what you are doing!
# As an alternative, you should use command `nb` or modify `pyproject.toml` to load plugins
nonebot.load_from_toml("pyproject.toml")

# Modify some config / config depends on loaded configs
# 
# config = driver.config
# do something...


if __name__ == "__main__":
    nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
    nonebot.run(app="__mp_main__:app")
