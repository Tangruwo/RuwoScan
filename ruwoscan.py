# 代码写的很唐谢谢看哈

import os
from openai import OpenAI
import json
import sys
from File import getConfig,clearFile
from Agent import Agent


if __name__ == "__main__":
    clearFile()

    config = getConfig()

    client = OpenAI(
        api_key = config["apiKey"],
        base_url = config["bashUrl"]
    )

    userInput = input("ruwoScan>")

    King = Agent(name="King",path="prompts/Default/kingResponse.txt",client=client,memoryLimit=30)

    print(King.think("prompts/ruwoscan.log","system",userInput))

