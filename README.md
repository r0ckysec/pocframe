# Pocframe
[![PyPI version](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/)  [![version](https://img.shields.io/badge/version-v1.0-brightgreen)](https://github.com/r0ckysec/pocframe)  ![PowerShell Gallery](https://img.shields.io/powershellgallery/p/DNS.1.1.1.1)

Pocframe是在[Saucerframe](https://github.com/saucer-man/saucerframe)项目的基础上进行修改，它是一个基于python3的开源批量POC检测框架，默认使用协程异步请求，支持多线程并发，支持多种指定目标方式，可用于批量POC检测，也可根据需要扩展功能。

**本项目用来交流学习，切勿用来做违法之事**

# 内容

- 支持多线程并发/协程
- 指定目标支持多种方式
    - 指定单个目标
    - 从文本种获取目标
    - 某一网段获取目标 e.g. 192.168.1.0/24
    - 某一ip段获取目标 192.168.1.0-192.168.2.33
    - 支持多种api批量获取目标: [Shodan](https://www.shodan.io/)、[Zoomeye](https://www.zoomeye.org/)、[Fofa](https://fofa.so)、[Censys](https://censys.io)
- 支持全局代理(socks5|socks4|http)

# 使用

安装方法：
```shell
git clone https://github.com/r0ckysec/pocframe.git 
cd pocframe
pip3 install -r requirement.txt 
```

使用方法：
```shell
python3 pocframe.py -h
python3 pocframe.py --show
python3 pocframe.py -s poc -iU target-url # 单个POC检测
python3 pocframe.py -s * -iU target-url # 加载所有POC检测
```

具体的参数说明：
```
# 1. 指定poc脚本(必需,支持同时指定多个poc)
-s poc1,poc2,poc3

# 2. 指定目标(必需)
-iU www.xxx.com  单个目标
-iF target.txt  从文本中加载
-iR 192.168.1.1-192.168.2.100  根据ip地址范围加载
-iN 192.168.1.0/24  根据网段加载
-aZ "redis"  ZoomEye api加载
-aS "redis"  Shodan api加载
-aC "redis"  Censys api加载
-aF "redis"  Fofa api加载

# 3. 其他(可选)
-h  查看帮助信息
-t 300  并发数(默认100)
--proxy socks5://127.0.0.1:1080  使用sock5代理
-o result.txt  指定输出文件
-v 4 指定终端输出详细级别(1-5, 默认为2)
--show  查看所有poc
-eT  并发采用多线程方式
-eG  并发采用协程方式(默认)
```

***实例***

`python3 pocframe.py -h`

![](https://github.com/r0ckysec/pocframe/blob/master/doc/img1.png)

`python3 pocframe.py --show`

![](https://github.com/r0ckysec/pocframe/blob/master/doc/img2.png)

`python3 pocframe.py -s * -iU baidu.com`

![](https://github.com/r0ckysec/pocframe/blob/master/doc/img3.png)


# POC编写

介绍已移至[wiki](https://github.com/r0ckysec/pocframe/wiki)

> 欢迎各位大表哥贡献POC，提交至 [POC库](https://github.com/r0ckysec/pocframe/tree/master/scripts) 

# References

- [POC-T](https://github.com/Xyntax/POC-T)
- [Saucerframe](https://github.com/saucer-man/saucerframe)
