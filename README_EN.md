<div align="center">

<img src="images/logo/logoZ.png" width="120" height="120" alt="RuwoScan">

# RuwoScan

> *Vulnerabilities tremble at the very sight of me*

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![OpenAI Compatible](https://img.shields.io/badge/API-OpenAI_Compatible-green)](https://platform.openai.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/chen18924/RuwoScan)](https://github.com/chen18924/RuwoScan)

[English](./README_EN.md) | [中文](./README.md)

</div>

---

## Table of Contents
[**`One‑line summary`**](#one-line-summary)  
[**`Features`**](#features)  
[**`Quick Start`**](#quick-start)  
[**`Usage`**](#usage)  
[**`Project Structure & Analysis`**](#project-structure--analysis)

---

## One‑line summary
An automated AI‑powered vulnerability scanner built on an Agentic framework.

---

## Features
- **Multi‑agent collaboration** – Commander (strategic planning), Scout (information gathering), Attacker (exploit testing & verification), Reporter (report generation).  
- **Full toolchain** – Equips AI with a complete toolset: file operations, HTTP requests, directory scanning, and more.  
- **Phased penetration testing** – AI follows a standardised process: reconnaissance → exploitation → reporting.  
- **Dynamic completion evaluation** – AI autonomously decides whether to proceed to the next phase based on attack surface coverage and vulnerability findings.  
- **Python support** – AI can call and execute Python scripts on‑the‑fly.  
- **Structured reports** – Automatically generates Markdown reports containing vulnerability type, location, and remediation advice.  
- **Natural language** – Interact using plain English; no need to memorise complex commands.  
- **Web visualisation** – Simple operation, verifiable process, full transparency.  
- **Low entry barrier** – No security background required; clone and run immediately.

---

## Quick Start

### Installation
Three easy steps (copy‑paste friendly):  
1. Star ⭐ this repository  
2. Clone the repo  
3. Install dependencies

```bash
git clone https://github.com/chen18924/RuwoScan
cd RuwoScan-main
pip install -r requirements.txt