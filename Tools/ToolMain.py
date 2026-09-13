import json
import requests
import urllib3
import os
import subprocess
from Tools.Tools.commonTools import *
from Tools.Tools.kingTools import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # 去掉那烦人信息

session = requests.Session()

def readFile(path, **kwargs):
    try:
        baseDir = os.path.join(os.getcwd(), "Downloads")
        fullPath = os.path.join(baseDir, path)

        if not os.path.abspath(fullPath).startswith(os.path.abspath(baseDir)):
            return f"无权访问{path}, 只能访问Downloads下的文件"

        with open(fullPath,"r") as f:
            return f.read()

    except Exception as e:
        return str(e)

def createFile(path,content, **kwargs):
    try:
        baseDir = os.path.join(os.getcwd(), "Downloads")
        fullPath = os.path.join(baseDir, path)
    
        if not os.path.abspath(fullPath).startswith(os.path.abspath(baseDir)):
            return f"无权访问{path}, 只能访问Downloads下的文件"
        with open(fullPath,"w") as f:
            f.write(content)

            return "创建成功"
    except Exception as e:
        return str(e)

def setRequests(url, method="GET", headers=None, data=None, params=None, timeout=10,verify=False, **kwargs): # 发送 HTTP 请求
    try:

        # headers处理
        if isinstance(headers, str):
            headers = json.loads(headers) if headers else {}
        elif headers is None:
            headers = {}

        # params处理
        if isinstance(params, str):
            params = json.loads(params) if params else None

        # data 处理
        if isinstance(data, str):
            data = json.loads(data) if data else None

        # print("[Session Cookie]", session.cookies.get_dict())
        # print("[POST Data]", data)
        
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
            "url": url,
            "method": method,
            "params": params,
            "data": data,
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "body": response.text,
            "length": len(response.text)
        }
    
    except Exception as e:
        return str(e)
    
def switchPhases(**kwargs):
    return "switchPhases"

def runPython(path: str, **kwargs) -> str:
    try:
        baseDir = os.path.join(os.getcwd(), "Downloads")
        fullPath = os.path.join(baseDir, path)
        if not os.path.abspath(fullPath).startswith(os.path.abspath(baseDir)):
            return f"无权访问{path}, 只能访问Downloads下的文件"
        
        result = subprocess.run(
            ["python", fullPath],
            capture_output=True,
            text=True,
            timeout=30
        )
        output = result.stdout
        if result.stderr:
            output += "\n[stderr]\n" + result.stderr
        return output
    except Exception as e:
        return str(e)
    
commonToolsMap = {
    "readFile": readFile,
    "createFile": createFile,
    "setRequests": setRequests,
    "runPython": runPython
}

kingToolMap = {
    "readFile": readFile,
    "createFile": createFile,
    "setRequests": setRequests,
    "switchPhases": switchPhases,
    "runPython": runPython

}

toolMapRead ={
    "Common": [commonToolsMap,commonTools],
    "King": [kingToolMap,kingTools]

}

def getTool(toolStr):
    tool = toolMapRead.get(toolStr)
    return tool[1]

def executeTool(toolCall,name): # 导入时使用
    try:
        toolsMap = toolMapRead.get(name)[0]
        funcName = toolCall.function.name
        
        # arguments = json.loads(toolCall.function.arguments)

        # 解决 Expecting value: line 1 column 1 (char 0)
        argsStr = toolCall.function.arguments
        if argsStr is None or argsStr.strip() == "":
            arguments = {}
        else:
            arguments = json.loads(argsStr)
        
        func = toolsMap.get(funcName)
        try:
            if func:
                return func(**arguments)
            else:
                return f"没有工具: {funcName}"
        except Exception as e:
            return str(e)
        
    except Exception as e:
        with open("debug.log", "a", encoding="utf-8") as bug:
            bug.write(f"{str(e)}, {toolCall}, {name}\n")
            
        return str(e)