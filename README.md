***
> github项目地址：[https://github.com/Zhao-sai-sai/Full-Scanner](https://github.com/Zhao-sai-sai/Full-Scanner)
## 工具简介

工具还在写中半成品，可能要好几个月，应为我是懒王

做渗透测试有的时候要去用这个工具那个工具去找感觉麻烦我自己就写了一个简单的整合工具，有互联网大佬不要喷我我也是废物 <img src="https://cdn.jsdelivr.net/gh/Zhao-sai-sai/Full-Scanner/img/bqb.png" height="50xp" ><p/> 

Full-Scanner是一个多功能扫描工具，支持被动/主动信息收集，漏洞扫描，常见的POC和EXP，现在还在添加功能有一部分是我网上找的不错的工具整合到这个工具里面了

> 用到的工具项目地址
- https://github.com/yzddmr6/WebCrack
- https://github.com/F6JO/CmsVulScan
## Full-Scanner的子工具
什么是子工具就是我还没有整理到Full-Scanner工具里面的单独工具

> 下面这几个是已经开发好的工具可以使用的
- 网站备份文件扫描工具下面地址：https://github.com/Zhao-sai-sai/Full_Scanner_ProbeBackup

## 工具下载

```buildoutcfg
git clone  https://github.com/Zhao-sai-sai/Full-Scanner.git
```
## 安装一些依赖

```buildoutcfg
cd Full-Scanner
pip install -r requirements.txt
```
## 目录结构
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

## 导入自己的脚本
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

演示：

![mian](https://fastly.jsdelivr.net/gh/Zhao-sai-sai/Full-Scanner/img/yanshi.gif)



## 现在啥也不是凑合看吧

> 就下面这几个参数可以用bug还多,我太难了 <img src="https://cdn.jsdelivr.net/gh/Zhao-sai-sai/Full-Scanner/img/bqbwq.gif" height="50xp" ><p/> 

> 界面我用来两种格式
 - 默认是参数模式
 - -G：选择模式

![mian](https://fastly.jsdelivr.net/gh/Zhao-sai-sai/Full-Scanner/img/mian111.png)
![mian](https://fastly.jsdelivr.net/gh/Zhao-sai-sai/Full-Scanner/img/mian222.png)
![mian](https://fastly.jsdelivr.net/gh/Zhao-sai-sai/Full-Scanner/img/mian333.png)
![mian](https://fastly.jsdelivr.net/gh/Zhao-sai-sai/Full-Scanner/img/3.png)

![mian](https://cdn.jsdelivr.net/gh/Zhao-sai-sai/Full-Scanner/img/mian444.png)



> 下面是他的一些功能

![mian](https://cdn.jsdelivr.net/gh/Zhao-sai-sai/Full-Scanner/img/fofa111.png)

![mian](https://cdn.jsdelivr.net/gh/Zhao-sai-sai/Full-Scanner/img/dns.png)

![mian](https://cdn.jsdelivr.net/gh/Zhao-sai-sai/Full-Scanner/img/sd111.png)


![mian](https://cdn.jsdelivr.net/gh/Zhao-sai-sai/Full-Scanner/img/crack111.png)

![mian](https://cdn.jsdelivr.net/gh/Zhao-sai-sai/Full-Scanner/img/wh.png)

![mian](https://cdn.jsdelivr.net/gh/Zhao-sai-sai/Full-Scanner/img/cms111.png)



![mian](https://cdn.jsdelivr.net/gh/Zhao-sai-sai/Full-Scanner/img/c111.png)


![mian](https://cdn.jsdelivr.net/gh/Zhao-sai-sai/Full-Scanner/img/b111.png)



## 警告
***
### 请勿用于非法用途！否则自行承担一切后果
