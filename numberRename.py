# -*- coding: utf-8 -*-

# 本程序用于重命名文件，适配多级目录,已经实现的功能有：
# 1.文件夹以及文件中的一二三四五...改写成阿拉伯数字12345
import os, re


# 大小数字替换函数，100以内
def BigNum2SmallNum(filename):
    bignum = re.findall('[一二三四五六七八九十]+', filename)
    num = ""
    # 没有数字的字符串处理，不然会下标报错
    if bignum == []:
        return filename
    str_num = bignum[0]
    num_dict = {"一": "1", "二": "2", "三": "3", "四": "4", "五": "5", "六": "6", "七": "7", "八": "8", "九": "9",
                "十": ""}
    if str_num[0] == "十" and len(str_num) == 1:
        num_dict["十"] = "10"
    if str_num[0] == "十" and len(str_num) == 2:
        num_dict["十"] = "1"
    if str_num[0] != "十" and len(str_num) == 2:
        num_dict["十"] = "0"

    for str in str_num:
        for key in num_dict:
            if key == str:
                num += num_dict[key]
                break
    pattern = bignum[0]  # 定义分隔符,有个问题，只能处理第一个数字
    result = re.split(pattern, filename)  # 以pattern的值 分割字符串
    result.insert(1, num)
    all = ''.join(result)  # 合并文件名

    return all  # 返回文件名


print('本程序可对内嵌套多级文件夹的路径下文件批量重命名')
folder = input("请粘贴入待改名文件路径（如C:\\Users\\UserName\\Desktop）：")  # 通过用户粘贴入待改名文件路径
if os.path.exists(folder):  # 判断该路径是否真实存在
    dirs_list = []  # 建立一个列表存放该文件夹及包含的所有嵌套及多重嵌套的子文件夹名
    for root, dirs, flies in os.walk(folder, topdown=False):  # 输出目录树中的根目录，文件夹名，文件名,后续遍历
        for name in dirs:
            if (name != []):  # 去除无效目录（最里层没有下级目录）
                dirs_list.append(os.path.join(root, name))  # 循环加入所有嵌套及多重嵌套的带路径子文件夹名
    dirs_list.append(folder)
    os.chdir(folder)  # 切换OS工作目录到文件所在位置
    # 修改所有文件名字
    for each_dirs in dirs_list:  # 遍历所有文件
        files_list = os.listdir(each_dirs)  # 生成待改名文件列表
        os.chdir(each_dirs)  # 切换OS工作目录到文件所在位置
        for filename in files_list:
            newfilename = BigNum2SmallNum(filename)  # 大小写切换函数
            if filename != newfilename:  # 防止相    同文件名报错
                os.rename(filename, newfilename)  # 改名
                print(filename, '->', newfilename)
    print("\n处理完毕！")
else:  # 如果是无效路径则跳过
    print('路径输入错误或不存在')
