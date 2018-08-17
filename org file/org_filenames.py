#! python3
# complete the filename that contain sequence like'spam001','spam003'

import os, re

full_list = []
os.chdir(input('请输入需要操作的文件夹路径：\n'))
# 获取列表中符合规则的文件
name_start = input('请输入需要处理的批量文件的前缀：\n')
file_extension = input('请输入需要处理的批量文件的扩展名：\n')
file_names = [file_name for file_name in os.listdir('.') if
              file_name.startswith(name_start) and file_name.endswith(file_extension)]
file_names.sort()
print(file_names)

# 提取最后一个文件中的数字
final_num_regex = re.compile(r'\d+')
final_num = int(final_num_regex.search(file_names[-1]))

# 准备好完整的数字列表
num_length = input('是否需要补零，需要请输入数字总长度，不需要则直接回车')
if num_length is not None:
    try:
        int_num_length = int(num_length)
        for file_num in range(1, final_num + 1):
            file_num__zfill = str(file_num).zfill(int_num_length)
            full_list.append(name_start + file_num__zfill + '.' + file_extension)
    except TypeError as e:
        print(e.__cause__ + '\n请输入正确的数字')
else:
    for file_num in range(1, final_num + 1):
        file_num__zfill = str(file_num).zfill(len(str(final_num)))
        full_list.append(name_start + file_num__zfill + '.' + file_extension)

diff_list = list(set(full_list).difference(set(file_names)))
for i in range((len(diff_list) * -1), 0):
    os.rename(file_names[i], diff_list[i])
