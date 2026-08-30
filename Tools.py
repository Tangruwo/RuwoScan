import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # 去掉那烦人信息

commonTools = [
    # 读取文件
    {
        "type": "function",
        "function": {
            "name": "readFile",
            "description": "读取指定路径的文件内容",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "文件路径"}
                },
                "required": ["path"]
            }
        }
    },
    # 创建文件
    {
        "type": "function",
        "function": {
            "name": "createFile",
            "description": "创建指定路径的文件和内容,如果文件已存在会覆盖",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "文件路径"},
                    "content": {"type": "string", "description": "文件写入的内容"}

                },
                "required": ["path","content"]
            }
        }
    },
    # 发请求
    {
        "type": "function",
        "function": {
            "name": "setRequests",
            "description": "发送 HTTP 请求，支持 GET/POST/PUT/DELETE,返回状态码、响应头和正文",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "目标 URL"},
                    "method": {"type": "string", "description": "HTTP 方法，默认 GET"},
                    "headers": {"type": "string", "description": "请求头 JSON 字符串，如 '{\"User-Agent\": \"Mozilla/5.0\"}'"},
                    "data": {"type": "string", "description": "请求体 JSON 字符串"},
                    "params": {"type": "string", "description": "URL 参数字典 JSON 字符串"},
                    "timeout": {"type": "integer", "description": "请求超时时间"},
                    "verify": {"type": "boolean", "description": "是否跳过证书验证,默认Flase不跳过"}
                },
                "required": ["url"]
            }
        }
    },

]

kingTools = [
        # 读取文件
    {
        "type": "function",
        "function": {
            "name": "readFile",
            "description": "读取指定路径的文件内容",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "文件路径"}
                },
                "required": ["path"]
            }
        }
    },
    # 创建文件
    {
        "type": "function",
        "function": {
            "name": "createFile",
            "description": "创建指定路径的文件和内容,如果文件已存在会覆盖",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "文件路径"},
                    "content": {"type": "string", "description": "文件写入的内容"}

                },
                "required": ["path","content"]
            }
        }
    },
    # 发请求
    {
        "type": "function",
        "function": {
            "name": "setRequests",
            "description": "发送 HTTP 请求，支持 GET/POST/PUT/DELETE,返回状态码、响应头和正文",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "目标 URL"},
                    "method": {"type": "string", "description": "HTTP 方法，默认 GET"},
                    "headers": {"type": "string", "description": "请求头 JSON 字符串，如 '{\"User-Agent\": \"Mozilla/5.0\"}'"},
                    "data": {"type": "string", "description": "请求体 JSON 字符串"},
                    "params": {"type": "string", "description": "URL 参数字典 JSON 字符串"},
                    "timeout": {"type": "integer", "description": "请求超时时间"},
                    "verify": {"type": "boolean", "description": "是否跳过证书验证,默认Flase不跳过"}
                },
                "required": ["url"]
            }
        }
    },
    # 切换下一阶段
    {
        "type": "function",
        "function": {
            "name": "switchPhases",
            "description": "切换到下一攻击阶段",
            "parameters": {
                "type": "object"
            }
        }
    }

]

session = requests.Session()

def readFile(path):
    try:
        with open(path,"r") as f:
            return f.read()

    except Exception as e:
        return str(e)

def createFile(path,content):
    try:
        with open(path,"w") as f:
            f.write(content)

            return "创建成功"
    except Exception as e:
        return str(e)

def setRequests(url, method="GET", headers=None, data=None, params=None, timeout=10,verify=False): # 发送 HTTP 请求
    try:

        headers = json.loads(headers) if headers else {}
        params = json.loads(params) if params else None

        response = session.request(
            method=method.upper(),
            url=url,
            headers=headers,
            data=data,
            params=params,
            timeout=timeout,
            verify=verify  # 跳过证书验证
        )

        return {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "body": response.text[:2000],  # 限制长度，防止爆内存
            "length": len(response.text)
        }
    
    except Exception as e:
        return str(e)
    
def switchPhases():
    return "switchPhases"

commonToolsMap = {
    "readFile": readFile,
    "createFile": createFile,
    "setRequests": setRequests
}

kingToolMap = {
    "readFile": readFile,
    "createFile": createFile,
    "setRequests": setRequests,
    "switchPhases": switchPhases
}

toolMapRead ={
    "Common": [commonToolsMap,commonTools],
    "King": [kingToolMap,kingTools]

}

def getTool(toolStr):
    tool = toolMapRead.get(toolStr)
    return tool[1]

def executeTool(toolCall,name):
    toolsMap = toolMapRead.get(name)[0]
    funcName = toolCall.function.name
    print("收到参数:", toolCall.function.arguments)
    # arguments = json.loads(toolCall.function.arguments)

    # 解决 Expecting value: line 1 column 1 (char 0)
    argsStr = toolCall.function.arguments
    if argsStr is None or argsStr.strip() == "":
        arguments = {}
    else:
        arguments = json.loads(argsStr)
    
    func = toolsMap.get(funcName)
    if func:
        return func(**arguments)
    else:
        return f"没有工具: {funcName}"