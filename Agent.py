# 
from openai import OpenAI
from File import getConfig,getLog,saveLog
from Tools import *

class Agent: # 智能体基类
    def __init__(self, name: str, path, client, memoryLimit: int, toolMapName: str): # 初始化哈哈 
        self.name = name 
        self.client = client
        self.memoryLimit = memoryLimit
        self.toolMapName = toolMapName

        try:
            with open(path,"r",encoding='utf-8') as f:
                self.prompt = f.read()
        except:
            print(">> Error: Agent no file")

        # saveLog(path="ruwoscan.log",diaName=self.name,Content=self.prompt)

    def think(self,path,diaName,diaContent) -> str: # 路径,名,内容
        config = getConfig()

        self.memory = getLog(path)

        response = self.client.chat.completions.create(
            model = config["model"],
            messages = [
                {"role": "system", "content": self.prompt}
            ] + self.memory + [
                {"role": "user", "content": diaContent}
            ],
            stream=False,
            tools=getTool(self.toolMapName)
        )

        if path != '': # 否则不记录
            content = response.choices[0].message.content
            if diaContent == content:
                saveLog(path=path,diaName=diaName,Content=diaContent) # 将对话者内容写入日志
                saveLog(path=path, diaName=self.name, Content=response.choices[0].message.content) # 将ai输出写入内容
            else:
                saveLog(path=path, diaName=self.name, Content=content) # 将ai输出写入内容

        # 使用tooL
        toolCalls = response.choices[0].message.tool_calls
        if toolCalls:
            toolReturns = ""
            for toolCall in toolCalls:
                toolReturn = executeTool(toolCall=toolCall, name=self.toolMapName)
                if toolReturn == "switchPhases":
                    return "switchPhases"
                
                toolReturns += str(toolReturn)
                saveLog(path=path,diaName="TOOL",Content=toolReturn)
            # 第二次思考,总结调用结果
            response = self.client.chat.completions.create(
                model = config["model"],
                messages = [
                    {"role": "system", "content": self.prompt}
                ] + self.memory + [
                    {"role": "user", "content": "这是工具结果,请进行总结分析:"}
                ] + [
                    {"role": "user", "content": toolReturns}
                ],
                stream=False,
            )
            saveLog(path=path, diaName=self.name, Content=response.choices[0].message.content)

        if response.choices[0].message.content: # 没调用tool直接返回结果
            return response.choices[0].message.content
            

    def clearMemory():
        pass



