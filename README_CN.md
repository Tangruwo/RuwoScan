<div align="center">

# RuwoScan

> *AI*漏洞扫描工具

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![OpenAI Compatible](https://img.shields.io/badge/API-OpenAI_Compatible-green)](https://platform.openai.com)

[English](./README.md) | [中文](./README_CN.md)

</div>

---

## 目录
[**`简介`**](#简介)
[**`特性`**](#特性)
[**`快速开始`**](#快速开始)
[**`使用`**](#使用)
[**`项目结构及分析`**](#项目结构及分析)
[**`等待更新`**](#等待更新)

---

## 简介
一句话让ai帮你快速探测web漏洞

---

## 特性
- **多智能体协同** 指挥官(拟定方向) 侦察兵(信息收集) 攻击者(漏洞测试,验证) 报告员(生成报告)
- **完整工具链** 为 AI 配备了完整的工具生态：文件操作、HTTP 请求、目录扫描等
- **阶段化渗透** AI渗透阶段化，过程标准(探测 -> 渗透 -> 生成报告)
- **Python支持** AI自主调用运行Python程序
- **结构化报告** 自动生成包含漏洞类型、位置、修复建议的 Markdown 报告
- **自然语言** 说人话就能用,无需记忆复杂命令
- **上手门槛低** 无需安全背景,克隆即用
- **自动化高** 从信息收集到漏洞验证,全程由指挥官带领多个智能体自动完成
- **ai自动结束任务** AI自行判断进入下一个阶段,防止未达成指标
- **Web端可视化** 操作简单，过程可验证，全程透明

---

## 快速开始

### 安装
三步走(可直接复制)
1. 点星
2. 克隆
3. 安装库
``` bash
git clone https://github.com/chen18924/RuwoScan
cd RuwoScan-main
pip install -r requirements.txt

```

### 启动
普通启动：
``` bash
python ruwoscan.py
>> 没有检测到apiKey,请输入: your-api-key
>> 没有检测到bashUrl,请输入: https://....
>> 没有检测到model,请输入: your-chat
>> 文件已储存到config.json,注意保密

```
Web启动：
``` bash
python ruwoscan.py -web
>> 没有检测到apiKey,请输入: your-api-key
>> 没有检测到bashUrl,请输入: https://....
>> 没有检测到model,请输入: your-chat
>> 文件已储存到config.json,注意保密

```
![Web终端启动](images/web终端启动.png)

---

## 使用
``` bash
python ruwoscan.py
RuwoScan> 对http://localhost/pikachu/index.php进行黑盒测试


```

## 项目结构及分析



## 等待更新
1. 模型连接断连机制
    - 模型3次连接失败才会断开连接
2. 工具链完善
    - 去github上下载一点项目插进去写tools里(我去这招绝对前无古人，这是跨时代的发明)
    - python tool，
3. 上下文压缩
    - 老早该搞了，但是懒，目前没问题
4. 代码规范化
    - except那边加点条件
    - Tools那边丑陋不堪，拆解成 主代json 形式
5. 代码安全性调整
    - createFile 和 readFile 可以调整一下
