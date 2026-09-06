<div align="center">

<img src="images/logo/logoZ.png" width="120" height="120" alt="RuwoScan">

# RuwoScan

> *漏洞会为见到我而颤抖不已*

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![OpenAI Compatible](https://img.shields.io/badge/API-OpenAI_Compatible-green)](https://platform.openai.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/chen18924/RuwoScan)](https://github.com/chen18924/RuwoScan)

[English](./README_EN.md) | [中文](./README.md)

</div>

---

## 目录
[**`一句话简介`**](#一句话简介)
[**`特性`**](#特性)
[**`快速开始`**](#快速开始)
[**`使用`**](#使用)
[**`项目结构及分析`**](#项目结构及分析)

---

## 一句话简介
基于Agentic 框架的自动化AI漏洞扫描工具。

---

## 特性
- **多智能体协同** 指挥官(拟定方向) 侦察兵(信息收集) 攻击者(漏洞测试,验证) 报告员(生成报告)
- **完整工具链** 为 AI 配备了完整的工具生态：文件操作、HTTP 请求、目录扫描等
- **阶段化渗透** AI渗透阶段化，过程标准(探测 -> 渗透 -> 生成报告)
- **动态完成评估** 基于攻击面覆盖与漏洞发现情况，AI 自主决定是否推进至下一阶段
- **Python支持** AI自主调用运行Python程序
- **结构化报告** 自动生成包含漏洞类型、位置、修复建议的 Markdown 报告
- **自然语言** 自然语言交互,无需记忆复杂命令
- **Web端可视化** 操作简单，过程可验证，全程透明
- **上手门槛低** 无需安全背景,克隆即用
---

## 快速开始

### 安装
三步走(可直接复制)
1. 点星 ⭐
2. 克隆仓库
3. 安装依赖

``` bash
git clone https://github.com/chen18924/RuwoScan
cd RuwoScan-main
pip install -r requirements.txt

```



### 项目配置
流程自动提示配置，无需额外配置
``` bash
python ruwoscan.py
>> 没有检测到apiKey,请输入: your-api-key
>> 没有检测到bashUrl,请输入: https://....
>> 没有检测到model,请输入: your-chat
>> 文件已储存到config.json,注意保密

---

## 使用
使用终端直接启动：
``` bash
python ruwoscan.py
RuwoScan> 对http://localhost/pikachu/index.php进行黑盒测试

```
![终端启动](images/终端演示.png)

终端调用Web启动：
``` bash
python ruwoscan.py -web

```
![终端启动](images/Web演示.png)
---

## 项目结构及分析

---
