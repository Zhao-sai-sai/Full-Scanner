import os
import datetime

from thirdparty.extracted.crack.crack_task import CrackTask


def single_process_crack(url_list):
    all_num = len(url_list)
    cur_num = 1
    print("总任务数: " + str(all_num))
    for url in url_list:
        CrackTask().run(cur_num, url)
        cur_num += 1


def Interface(url_extract):
    print("扫描结果会保存到result/webcrack/文件夹里面")
    try:
        import conf.config
    except:
        print("加载配置文件失败！")
        exit(0)

    url_file_name = url_extract #input('File or Url:\n')

    if '://' in url_file_name:
        CrackTask().run(1, url_file_name)
    else:
        url_list = []
        if os.path.exists(url_file_name):
            print(url_file_name, "存在!\n")
            with open(url_file_name, 'r', encoding="UTF-8") as url_file:
                for url in url_file.readlines():
                    url = url.strip()
                    if url.startswith('#') or url == '' or ('.edu.cn' in url) or ('.gov.cn' in url):
                        continue
                    url_list.append(url)
            start = datetime.datetime.now()
            single_process_crack(url_list)
            end = datetime.datetime.now()
            print(f'所有过程完成！ 花费时间: {str(end - start)}')
        else:
            print(url_file_name + " 不存在！")
            exit(0)
