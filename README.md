***
> github项目地址：[https://github.com/Zhao-sai-sai/Full-Scanner](https://github.com/Zhao-sai-sai/Full-Scanner)
## :one:工具简介

工具还在写中半成品，可能要好几个月，应为我是懒王:kissing_closed_eyes:

做渗透测试有的时候要去用这个工具那个工具去找感觉麻烦我自己就写了一个简单的整合工具，有互联网大佬不要喷我我也是废物 <img src="http://img.loveqx.cn/github/FullScanner/bqb.png" height="50xp" ><p/> 

Full-Scanner是一个多功能扫描工具，支持被动/主动信息收集，漏洞扫描，常见的POC和EXP，现在还在添加功能有一部分是我网上找的不错的工具整合到这个工具里面了

> 用到的工具项目地址
- https://github.com/yzddmr6/WebCrack
- https://github.com/F6JO/CmsVulScan

## :two::white_check_mark:Full-Scanner的子工具

什么是子工具就是我还没有整理到Full-Scanner工具里面的单独工具

> 下面这几个是已经开发好的工具可以使用的
- 网站备份文件扫描工具下面地址：https://github.com/Zhao-sai-sai/Full_Scanner_ProbeBackup
- 后台扫描工具项目地址：https://github.com/Zhao-sai-sai/Full_Scanner_back

## :three:工具下载

```bash
git clone  https://github.com/Zhao-sai-sai/Full-Scanner.git
```
## :four:安装一些依赖

```bash
cd Full-Scanner
pip install -r requirements.txt
```

## :five:目录结构

现在的目录结构

```bash
Full-Scanner
├── Full-Scanner.py # main
├── judge.py # 判断输入的命令
├── blasting # 爆破的一些脚本
│   ├── ftp_blasting # ftp破解
│   │   ├── ftp.py
│   └── ssh_blasting # ssh破解
│       └── ssh.py
├── collect  # 被动搜集的一些脚本
│   ├── bing.py # bing搜索提取
│   ├── fofa.py # fofa搜索结果提取
│   ├── req_whois.py # whois查询
│   └── shodan.py # shodan信息收集
│   ├── google.py # 谷歌搜索提取
│   └── SubDnsDetect # 个采用的一些搜索引擎进行域名探测
│       ├── bing.py # 用的bing行域名探测
│       ├── censys.py # 用的censys的证书进行域名探测
│       ├── crt.py # 用的crt证书进行域名探测
│       ├── fofa.py # 用的fofa进行域名探测
│       └── SubDns.py # mian
├── conf # 配置文件
│   ├── config.py
├── dictionary # 存在着字典
│   ├── back 
│   ├── BackgroundDetection
│   ├── Backupfilescan
│   ├── extracted
│   ├── ftp
│   └── ssh
├── Initiative # 主动信息收集的一些脚本
│   ├── backgroundscan # 后台扫描
│   │   ├── back.py
│   ├── Backupfilescan # 备份文件扫描
│   │   ├── ProbeBackup.py
│   └── portscan # 端口扫描
│       ├── port.py
├── lib # 脚本需要的一些脚本
│   ├── Auxiliary.py  # 杂东西
│   ├── choose.py  # 调用颜色
│   ├── cmdline
│   │   ├── cmdline.py # 命令行参数和图标
│   ├── choose_model  # 选项模式
│   │   ├── Big_Category.py
│   │   └── sub_options
│   │       ├── Active_Options.py
│   │       ├── blasting_Options.py
│   │       ├── Passive_Options.py
├── other # 其他脚本
│   └── portquery # 查看端口对应的服务
│       ├── potrquery.py
│       └── tcpudp.py
├── PocAndExpScript # 自己脚本或者POCEXP生成到工具里面
│   ├── generate #自己的脚步
│   │  
│   ├── main.py # 生成文件的关键文件 
│   ├── pecmdline
│   │   ├── pecmdline.py　# 命令行参数
│   ├── storage.py # 调研判断类似上面的 ├── judge.py # 判断输入的命令
│   └── storage.txt # 添加语法多次添加
├── result # 用于存放扫描下来的结果
│   ├── back
│   ├── cms
│   ├── fofa
│   ├── ftp
│   ├── ProbeBackup
│   ├── searchengine
│   ├── shodan
│   ├── ssh
│   ├── webcrack
│   └── whois
└── thirdparty # 用到的其他人写的工具
```

## :six:工具的使用

```bash
>>>>>  python3 Full-Scanner.py -h
************************************************************



         __|    | |       __|                              
         _||  | | |____|\__ \  _|  _` |   \    \   -_)  _| 
        _|\_,_|_|_|     ____/\__|\__,_|_| _|_| _|\___|_|  



作者：w啥都学
Blog地址：www.zssnp.top
gitee项目地址：https://gitee.com/wZass/Full-Scanner
github项目地址：https://github.com/Zhao-sai-sai/Full-Scanner
 ************************************************************                              
usage: python3 Full-Scanner.py [参数] [目标] [其他参数]

本程序是一个多功能工具、支持信息收集、爆破、漏洞扫描、常见的POC和EXP

options:
  -h, --help          show this help message and exit

选择模式:
  如果不喜欢输入命令那样、可以用下面的参数

  -G                  选择使用选择模式

[1][*]被动信息收集:
  下面是常见的被动信息收集方法会利用各大搜索引擎

[1]被动信息收集：[1]fofa搜索结果提取:
  -fofa [IP/域名]       fofa搜索结果提取
  -Cookie [Cookie值]   Cookie需要验证、如果不想每次都指定可以去config.py文件里面添加

[1]被动信息收集：[2]shodan信息收集:
  -shodan [[IP]]      shodan信息收集
  -api [api值]         用-API参数指定、如果不想每次都指定可以去config.py文件里面添加

[1]被动信息收集：[3]whois查询:
  -whois [域名]         whois查询、咧-whois https://www.baidu.com/

[1]被动信息收集：[4]搜索引擎爬虫:
  下面这个会用一下搜索引擎进行搜索提取搜索的URL

  -bing [查询语句]        搜索引擎爬虫、咧 -bing 'intitle:后台登陆 "学院"'
  -bingm [提取的页数]      提取的页数如果不指定默认就是100000、咧 -bingm 5

[1]被动信息收集：[5]搜索引擎爬虫:
  下面这个会用一下搜索引擎进行搜索提取搜索的URL

  -google [查询语句]      搜索引擎爬虫、咧 -google 'intitle:后台登陆 "学院"'
  -googlem [提取的页数]    提取的页数如果不指定默认就是100000、咧 -google 5
  -googlep [代理地址]     设置代理、咧 -googlep 127.0.0.1:8080

[1]被动信息收集：[6]子域名查询:
  这个采用的一些搜索引擎进行域名探测有bing、crtsh、fofa、censys等、不需要输入API这个是采集的查询结果的页面进行提取的

  -SubDNS [域名]        子域名查询

[2][*]主动信息收集:
  下面是常见的主动信息收集方法

[2]主动信息收集：[1]目标cms识别:
  -cms [URL]          目标cms识别

[2]主动信息收集：[2]备份文件扫描:
  -PB [URL]           备份文件扫描 指定扫描的目标、比如 -PB https://baidu.com/
  -PBm [文件名]          多个目标保存到一个文件里面进行批量扫描
  -PBt [线程数]          指定线程默认是1
  -PBd [字典文件]         指定字典默认是自己生成
  -PBp [代理地址]         可选代理地址

[2]主动信息收集：[3]后台扫描:
  -BK [URL]           后台扫描、指定扫描的目标、比如 -BK https://baidu.com/
  -BKm [文件名]          多个目标保存到一个文件里面进行批量扫描
  -BKd [字典文件]         指定字典默认是用的php.txt
  -BKt [线程数]          指定线程默认是30
  -BKp [代理地址]         可选设置代理

[2]主动信息收集：[4]端口扫描:
  -PS [IP]            端口扫描、比如 -PS 1.1.1.1
  -PSp [指定端口]         指定端口、不指定默认常见的端口、指定比如-PSp 1-65535或者22,80,3306
  -PSt [线程数]          指定线程、线程太多会出问题

[3][*]爆破:
  下面是常见、web爆破、和服务的爆破

[3]爆破：[1]网页登录界面自动化破解:
  -crack [URL]        登录界面自动化破解、比如-crack https://xxx.com/admin.php

[3]爆破：[2]ftp爆破:
  -ftp [目标地址]         ftp爆破、比如-ftp 1.1.1.1
  -ftpp [指定端口号]       指定端口
  -ftpt [线程数]         指定线程
  -ftpadmin [文件名]     指定用户字典、不指定使用默认
  -ftppasswd [文件名]    指定密码字典、不指定使用默认

[3]爆破：[3]SSH破解:
  -ssh [目标地址]         ssh密码怕破解、比如 -ssh 1.1.1.1
  -sshp [指定端口号]       指定端口、默认端口号22
  -sshu [指定字典]        指定用户名字典、不指定使用默认字典
  -sshd [指定字典]        指定密码字典、不指定使用默认字典
  -ssht [线程数]         指定线程、线程太多会出问题、默认线程1

[*]其他：小工具:

其他：端口查询对应的服务:
  -tcp [端口]           tcp查询
  -udp [端口]           udp查询

添加POCEXP或者自己的脚步:
  -PE [PE]            使用POC/EXP
  -refresh [REFRESH]  刷新添加POC/EXP
  -reset [RESET]      重置POC/EXP
```

### 导入自己的脚本

叫文件方到`PocAndExpScript/generate`
导入的时候他会按照下面的方式进行导入
比如

```bash
he_lp={
    'filename':'CVE-2022-26134', # filename漏洞编号，这个将变成命令参数使用最好不要用中文
    'main':'main', # main这个就是接口函数
    'name':'CVE-2022-26134Confluence远程命令执行漏洞', # name 这个是这个漏洞代码的说明
    'important':['u'], # important就是必要要用的参数
    'u':'目标', # 其他的都会当做参数来用
    .......
}
```
<img src="http://img.loveqx.cn/github/FullScanner/yanshi.gif" height="500xp" >

### 使用截图

> 就下面这几个参数可以用bug还多,我太难了 <img src="http://img.loveqx.cn/github/FullScanner/bqbwq.gif" height="50xp" ><p/> 

> 界面我用来两种格式
 - 默认是参数模式

 - -G：选择模式

  ![mian](http://img.loveqx.cn/github/FullScanner/mian111.png)
  ![mian](http://img.loveqx.cn/github/FullScanner/mian222.png)
  ![mian](http://img.loveqx.cn/github/FullScanner/mian333.png)

![mian](http://img.loveqx.cn/github/FullScanner/mian444.png)

![mian](http://img.loveqx.cn/github/FullScanner/fofa111.png)

![mian](http://img.loveqx.cn/github/FullScanner/dns.png)

![mian](http://img.loveqx.cn/github/FullScanner/sd111.png)


![mian](http://img.loveqx.cn/github/FullScanner/crack111.png)

![mian](http://img.loveqx.cn/github/FullScanner/wh.png)

![mian](http://img.loveqx.cn/github/FullScanner/cms111.png)



![mian](http://img.loveqx.cn/github/FullScanner/c111.png)


![mian](http://img.loveqx.cn/github/FullScanner/b111.png)



## 警告
***
### 请勿用于非法用途！否则自行承担一切后果
