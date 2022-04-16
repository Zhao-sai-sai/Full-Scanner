import time
current_time=time.strftime("%Y-%m-%d%H:%M:%S", time.localtime())


SeriousConfig={
    'fofa':'',
    'shodan':''
}

HeadersConfig={
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}

# 需要的字典的位置设置
Specifyablastdictionary={
    'ftp':{'admin':'dictionary/ftp/admin.txt','passwd':'dictionary/ftp/passwd.txt'},
    'backgroundscan':'dictionary/BackgroundDetection/ask.txt',
    'extracted':{'admin':'dictionary/extracted/admin.txt','passwd':'dictionary/extracted/passwd.txt'}
}


# 输出的结果保存到位置
Savelocation={
    'fofa':f'result/fofa/{current_time}fofa.txt',
    'shodan':f'result/shodan/{current_time}shodan.txt',
    'backgroundscan':f'result/backgroundscan/{current_time}backgroundscan.txt',
}