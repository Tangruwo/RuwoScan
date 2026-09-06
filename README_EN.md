```bash
<div align="center">

<img src="images/logo/logoZ.png" width="120" height="120" alt="RuwoScan">

# RuwoScan

> *Vulnerabilities tremble at the sight of me*

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![OpenAI Compatible](https://img.shields.io/badge/API-OpenAI_Compatible-green)](https://platform.openai.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/chen18924/RuwoScan)](https://github.com/chen18924/RuwoScan)

[English](./README_EN.md) | [中文](./README.md)

</div>

---

## Table of Contents
[**`Overview`**](#overview)
[**`Features`**](#features)
[**`Quick Start`**](#quick-start)
[**`Usage`**](#usage)
[**`Project Structure & Analysis`**](#project-structure--analysis)

---

## Overview
An automated AI vulnerability scanning tool built on an Agentic framework.

---

## Features
- **Multi‑Agent Collaboration** Commander (sets direction), Scout (information gathering), Attacker (vulnerability testing & verification), Reporter (report generation)
- **Complete Toolchain** Equips the AI with a full ecosystem of tools: file operations, HTTP requests, directory scanning, and more
- **Phased Penetration** AI penetration is divided into phases with a standardized process (Reconnaissance → Exploitation → Report Generation)
- **Dynamic Completion Assessment** Based on attack surface coverage and vulnerability findings, the AI autonomously decides whether to advance to the next phase
- **Python Support** The AI can autonomously invoke and run Python programs
- **Structured Reports** Automatically generates Markdown reports containing vulnerability types, locations, and remediation recommendations
- **Natural Language** Interact using natural language—no need to memorize complex commands
- **Web Visualization** Simple to operate, process is verifiable, fully transparent
- **Low Barrier to Entry** No security background required—clone and use immediately

---

## Quick Start

### Installation
Three steps (can be copied directly)
1. Star the repo ⭐
2. Clone the repository
3. Install dependencies

``` bash
git clone https://github.com/chen18924/RuwoScan
cd RuwoScan-main
pip install -r requirements.txt
```

### Project Configuration
Configuration is prompted automatically during the process—no additional setup required.

``` bash
python ruwoscan.py
>> No apiKey detected, please enter: your-api-key
>> No bashUrl detected, please enter: https://....
>> No model detected, please enter: your-chat
>> File saved to config.json, keep it confidential
```

---

## Usage
Start directly from the terminal:

``` bash
python ruwoscan.py
RuwoScan> Perform black-box testing on http://localhost/pikachu/index.php
```

![Terminal Launch](images/terminal-demo.png)

Launch Web UI from the terminal:

``` bash
python ruwoscan.py -web
```

![Terminal Launch](images/web-demo.png)

---

## Project Structure & Analysis

---
```