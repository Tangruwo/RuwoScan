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

    KingReport = input("ruwoScan>") # 哈哈,这段有点想笑

    '''
    垃圾话---
    2026.8.26:
    呜嘿嘿,前面写的太难熬了,都快开学了www快点现在一个雏形发了吧
    WWU所以说免费的模型就是不好用吧,给我闲的
    呜呜deepseek harness挖漏洞根本没挖到,是我的问题吗为什对话一下老是 conversation Context 9:tool-callpwsh:0 received more than one start Match(internal)
    好无聊,写README先吧
    '''

    # 创建智能体
    King = Agent(name="King",path="prompts/Default/kingResponse.txt",client=client,memoryLimit=30)
    Recon = Agent(name="Recon",path="prompts/Default/recon.txt",client=client,memoryLimit=30)
    Attacker = Agent(name="Attacker",path="prompts/Default/attacker.txt",client=client,memoryLimit=30)

    Reporter = Agent(name="Reporter",path="prompts/Default/reporter.txt",client=client,memoryLimit=30)

    # 探测资产
    print("探测资产中...")
    for i in range(14):

        ReconReport = Recon.think("prompts/ruwoscan.log","assistant",KingReport) # 探测
        KingReport = King.think("prompts/ruwoscan.log","assistant",ReconReport) # 指明方向

        if "状态:结束" in KingReport:
            break
        
    # 渗透测试(气死我了昨天修了这么久bug结果是api的问题www2026.8.26)
    print("渗透测试中...")
    for i in range(14):
        AttackerReport = Attacker.think("prompts/ruwoscan.log","assistant",KingReport)
        KingReport = King.think("prompts/ruwoscan.log","assistant",AttackerReport)

        if "状态:结束" in KingReport:
            break

    # 总结报告
    print("正在为您总结报告www")
    print(Reporter.think("prompts/ruwoscan.log","assistant","请总结报告"))
    