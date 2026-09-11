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
            "description": "发送单个 HTTP 请求，支持 GET/POST/PUT/DELETE,返回状态码、响应头和正文，如需多个请求，请分多次调用",
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
    {
        "type": "function",
        "function": {
            "name": "runPython",
            "description": "执行 .py 文件，返回执行结果。用于计算、数据处理、构造 payload 等场景。",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "要执行的 Python 文件路径"
                    }
                },
                "required": ["path"]
            }
        }
    }
    

]