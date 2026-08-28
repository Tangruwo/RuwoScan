# 就是唐,不想写注释了
import json

def saveLog(path,diaName,Content): # 保存日志
    try:
        with open(path,"a",encoding="utf-8") as log:
            wMess = {
                "role": diaName, "content": Content 
            }
            
            log.write(json.dumps(wMess, ensure_ascii=False) + "\n")
    except:
        print(">> Error: saveLog error")

def getLog(path): # 读取日志
    try:
        data = []

        with open(path,"r",encoding="utf-8") as log:
            for line in log:
                if line.strip():
                    entry = json.loads(line)
                    content = entry.get("content")

                    if content is None:
                        content = ""
                    elif isinstance(content, dict):
                        content = json.dumps(content, ensure_ascii=False)
                    elif not isinstance(content, str):
                        content = str(content)
                        
                    data.append({"role": "user", "content": content})
        return data
    except Exception as e:
        print(">> Error: getLog error",e)
        return []

def getConfig(): # 从config文件中获取配置文件
    try:
        with open("config.json","r+",encoding="utf-8") as f:
            if f.read() == '':
                apiKey = input(">> no apiKey,plase: ")
                bashUrl = input(">> no bashUrl,plase: ")
                model = input(">> no model,plase: ")

                config = {
                    "apiKey": apiKey,
                    "bashUrl": bashUrl,
                    "model": model
                }

                json.dump(config,f,indent=4)

                return config
            
            else:
                f.seek(0) # 指针归0 话说今天是八月十四了,www我的暑假

                config = json.load(f)
                return config

    except: # 呜呜太可恶了竟然乱删我的东西(17.14好了现在不上传啦)
        with open("config.json","w",encoding="utf-8") as f: # 复制还能水一点代码,酣畅淋漓
            apiKey = input(">>没有检测到apiKey,请输入: ")
            bashUrl = input(">>没有检测到bashUrl,请输入: ")
            model = input(">>没有检测到model,请输入: ")
            print("文件已储存到config.json,注意保密")

            config = {
                "apiKey": apiKey,
                "bashUrl": bashUrl,
                "model": model
            }
            json.dump(config,f,indent=4)
            f.seek(0)

            return config

def initFile(): # 清一下文件
    files = [
        "prompts/ruwoscan.log",
        "prompts/King.log",
        "prompts/battle.log"
    ]
    
    with open("w","prompts/ruwoscan.log") as file:
        file.write()

    for i in files:
        with open(i,"w",encoding="utf-8") as flie:
            flie.write("")
                   
        