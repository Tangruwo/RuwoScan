# 
from openai import OpenAI, APIConnectionError, APIStatusError, APITimeoutError, RateLimitError
from File import getConfig,getLog,saveLog
from Tools.ToolMain import *
import sys

class Agent: # 智能体基类
    def __init__(self, name: str, path, client, memoryLimit: int, toolMapName: str): # 初始化哈哈 
        self.name = name 
        self.client = client
        self.memoryLimit = memoryLimit
        self.toolMapName = toolMapName

        try:
            with open(path,"r",encoding='utf-8') as f:
                self.prompt = f.read()
        except FileNotFoundError as e:
            print("提示词文件不存在:", path,e)

        # saveLog(path="ruwoscan.log",diaName=self.name,Content=self.prompt)

    def think(self,path,diaName,diaContent) -> str: # 路径,名,内容
        config = getConfig()

        # 上下文处理, 这一步应该是优化tokens消耗大头了，主要就是限制上下文长度
        memoryFull = getLog(path)
        memoryNHtool = []
        for memory in memoryFull:
            memoryRole = memory.get("role")
            if memoryRole != "TOOL":
                memoryNHtool.append(memory)
        self.memory = memoryNHtool[-self.memoryLimit:] if len(memoryNHtool) >self.memoryLimit else memoryNHtool

        try:
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
        except (APIConnectionError, APITimeoutError, RateLimitError): # 三次连接失败退出
            errorNumber = 1
            while True:
                try:

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

                    break

                except (APIConnectionError, TimeoutError, RateLimitError) as e: 
                    errorNumber += 1
                    if errorNumber >= 2:
                        print("API三次无法连接",e)
                        sys.exit(1)



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
            try:

                response = self.client.chat.completions.create(
                    model = config["model"],
                    messages = [
                        {"role": "system", "content": self.prompt}
                    ] + self.memory + [
                        {"role": "user", "content": "工具结果:"}
                    ] + [
                        {"role": "user", "content": toolReturns}
                    ],
                    stream=False,
                )
                saveLog(path=path, diaName=self.name, Content=response.choices[0].message.content)
            except (APIConnectionError, TimeoutError, RateLimitError):
                errorNumber = 1
                while True:
                    try:
                        response = self.client.chat.completions.create(
                            model = config["model"],
                            messages = [
                                {"role": "system", "content": self.prompt}
                            ] + self.memory + [
                                {"role": "user", "content": "工具结果:"}
                            ] + [
                                {"role": "user", "content": toolReturns}
                            ],
                            stream=False,
                        )
                        break

                    except (APIConnectionError, TimeoutError, RateLimitError) as e: 
                        errorNumber += 1
                        if errorNumber >= 2:
                            print("API三次无法连接",e)
                            sys.exit(1)

        if response.choices[0].message.content: # 没调用tool直接返回结果
            return response.choices[0].message.content
            

    def clearMemory():
        pass


