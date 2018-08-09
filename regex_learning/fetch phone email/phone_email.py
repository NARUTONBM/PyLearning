# ！ python3
# phone_email.py - Finds phone numbers and email addresses on the clipboard.
# 测试文本：2000年微软发布，452-662-4664世纪djskd@gmail.com初，微软公司开发的一款面向对象的语言

import pyperclip, re

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                 # 区号（可能带括号）
    (\s|-|\.)?                         # 分隔符（可能是‘ ’，‘.’，‘-’）
    (\d{3})                            # 前3位数
    (\s|-|\.)                          # 分隔符，同上
    (\d{4})                            # 后4位
    (\s*(ext|x|ext.)\s*(\d{2,5}))?     # 可选的分机号，任意数目的空格，接着ext、x或ext.，再接着2-5数字
    )''', re.VERBOSE)

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                  # 用户名，可以大小写字母、数字、句点、下划线、百分号、加号或短横
    @                                  # @符号
    [a-zA-Z0-9.-]+                     # 域名，只允许字母、数字、句点、短横
    (\.[a-zA-Z]{2,4})                  # dot-com部分，即‘顶级域名’2-4字符
    )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)

for groups in email_regex.findall(text):
    matches.append(groups[0])

# 复制结果到剪贴板
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone number or email addresses found.')
