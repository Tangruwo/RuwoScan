# 
from openai import OpenAI
from File import getConfig,getLog,saveLog
from Tools import *

class Agent: # 智能体基类
    def __init__(self, name: str, path, client, memoryLimit: int): # 初始化哈哈 
        self.name = name 
        self.client = client
        self.memoryLimit = memoryLimit


        try:
            with open(path,"r",encoding='utf-8') as f:
                self.prompt = f.read()
                print(f.read())
        except:
            print(">> Error: Agent no file")

        # saveLog(path="ruwoscan.log",diaName=self.name,Content=self.prompt)

    def think(self,path,diaName,diaContent): # 路径,名,内容
        config = getConfig()

        self.memory = getLog(path)

        response = self.client.chat.completions.create(
            model = config["model"],
            messages = [
                {"role": "system", "content": self.prompt}
            ] + self.memory + [
                {"role": diaName, "content": diaContent}
            ],
            stream=False,
            reasoning_effort="high",
            extra_body={"thinking": {"type": "enabled"}},
            tools=tools
        )

        if path != '': # 否则不记录
            saveLog(path=path,diaName=diaName,Content=diaContent) # 将对话者内容写入日志
            saveLog(path=path, diaName=self.name, Content=response.choices[0].message.content) # 将ai输出写入内容

        # 使用tooL
        toolCalls = response.choices[0].message.tool_calls
        if toolCalls:
            for toolCall in toolCalls:
                saveLog(path=path,diaName="TOOL",Content=executeTool(toolCall=toolCall))

        if response.choices[0].message.content: # 没调用直接返回
            return response.choices[0].message.content
        
        else: # 调用了tool,重新思考一次
            response = self.client.chat.completions.create(
                model = config["model"],
                messages = [
                    {"role": "system", "content": self.prompt}
                ] + self.memory + [
                    {"role": "user", "content": "这是工具结果..."}
                ],
                stream=False,
                reasoning_effort="high",
                extra_body={"thinking": {"type": "enabled"}}
            )
            

    def clearMemory():
        pass


