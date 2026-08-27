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
---

## 简介
一句话让ai帮你快速探测web漏洞

---

## 特性
- **多智能体协同** 指挥官(拟定方向) 侦察兵(信息收集) 攻击者(漏洞测试,验证) 报告员(生成报告)
- **完整工具链** 为 AI 配备了完整的工具生态：文件操作、HTTP 请求、目录扫描等，开箱即用
- **结构化报告** 自动生成包含漏洞类型、位置、修复建议的 Markdown 报告
- **自然语言** 说人话就能用,无需记忆复杂命令
- **上手门槛低** 无需安全背景,克隆即用，全程交互式配置
- **自动化高** 从信息收集到漏洞验证,全程由指挥官带领多个智能体自动完成
- **ai自动结束任务** AI自行判断进入下一个阶段,防止未达成指标

---

## 快速开始

### 安装
``` bash
git clone https://github.com/chen18924/RuwoScan
pip install -r requirements.txt

```

### 启动
``` bash
python ruwoscan.py
没有检测到apiKey,请输入: your-api-key
没有检测到bashUrl,请输入: https://....
没有检测到model,请输入: your-chat
文件已储存到config.json,注意保密

```

---

## 使用
``` bash
python ruwoscan.py
RuwoScan> 对http://localhost/pikachu/index.php进行黑盒测试


```