# 代码写的很唐谢谢看哈

from openai import OpenAI
from File import getConfig,initFile,saveLog,getLog
from Agent import Agent
# rich
from rich.console import Console
from rich.panel import Panel
from Web import Web

import threading
import time
import argparse
import webbrowser
import os
import keyboard

def keyInterruptExit():
    print("\n")
    os._exit(0)



parser = argparse.ArgumentParser(description='''RuwoScan AI漏洞扫描工具
Ctrl+Q结束程序
'''
,formatter_class=argparse.RawDescriptionHelpFormatter
)

parser.add_argument("-web",action="store_true",help="开启网页端调试")

args = parser.parse_args()

if __name__ == "__main__":

    initFile()

    config = getConfig()

    client = OpenAI(
        api_key = config["apiKey"],
        base_url = config["bashUrl"]
    )

    # rich的类
    console = Console()

    keyboard.add_hotkey('ctrl+q', keyInterruptExit)


    '''
    垃圾话---
    2026.8.26:
    呜嘿嘿,前面写的太难熬了,都快开学了www快点现在一个雏形发了吧
    WWU所以说免费的模型就是不好用吧,给我闲的
    呜呜deepseek harness挖漏洞根本没挖到,是我的问题吗为什对话一下老是 conversation Context 9:tool-callpwsh:0 received more than one start Match(internal)
    好无聊,写README先吧
    '''

    console.print(Panel("[bold cyan]RuwoScan[/] - AI 漏洞扫描工具", subtitle="[i]唐如我[/i]"))

    if args.web:
        threading.Thread(target=Web.run,daemon=True).start()
        print("host: http://127.0.0.1:5000")
        webbrowser.open("http://127.0.0.1:5000")

        while True:
            file = getLog("prompts/ruwoscan.log")
            try:
                KingReport = file[0]["content"]
                break
            except (IndexError, KeyError, TypeError):
                time.sleep(1)
                
    else:
        KingReport = input("ruwoScan>") # 哈哈,这段有点想笑
        saveLog("prompts/ruwoscan.log","user",KingReport)

    # 创建智能体
    King = Agent(name="King", path="prompts/Default/kingResponse.txt", client=client, memoryLimit=30, toolMapName="King")
    Recon = Agent(name="Recon", path="prompts/Default/recon.txt", client=client, memoryLimit=15, toolMapName="Common")
    Attacker = Agent(name="Attacker", path="prompts/Default/attacker.txt", client=client, memoryLimit=15, toolMapName="Common")

    # 两个报告总结
    Reporter = Agent(name="Reporter", path="prompts/Default/reporter.txt", client=client, memoryLimit=50, toolMapName="Common")
    DetReporter = Agent(name="DetReporter", path="prompts/Default/detReporter.txt", client=client, memoryLimit=50, toolMapName="Common")

    time.sleep(0.3)
    
    # 探测资产
    print("🎯 信息收集中...")
    for i in range(34):

        for i in range(2):
            ReconReport = Recon.think("prompts/ruwoscan.log","King",KingReport) # 探测 assistant
        
        KingReport = King.think("prompts/ruwoscan.log","Recon",ReconReport) # 指明方向
        if KingReport == "switchPhases":
            break
        
    # 渗透测试(气死我了昨天修了这么久bug结果是api的问题www2026.8.26)
    print("⚔️ 渗透测试中...")
    for i in range(34):
        for i in range(2):
            AttackerReport = Attacker.think("prompts/ruwoscan.log","King",KingReport)

        KingReport = King.think("prompts/ruwoscan.log","Attacker",AttackerReport)
        if KingReport == "switchPhases":
            break
    
    # 总结报告
    print("📝 总结报告中")

    reporterFilePath = "bugReport/" + str(int(time.time())) + ".txt" # 文件名
    DetReporterReport = DetReporter.think("prompts/ruwoscan.log","user","请总结报告")
    # 详细报告生成
    print(Reporter.think("prompts/ruwoscan.log","user","根据该报告总结简略漏洞报告:"+DetReporterReport)) # 简略报告

    with open(reporterFilePath,"w", encoding="utf-8") as file:
        file.write(DetReporterReport)
    print(f"\n详细报告地址: {reporterFilePath}")
