import re


def test(t_psw):
    if len(t_psw) >= 8:
        psw_regex1 = re.compile(r'[a-z]').search(t_psw)
        psw_regex2 = re.compile(r'[A-Z]').search(t_psw)
        psw_regex3 = re.compile(r'[0-9]+').search(t_psw)
        if psw_regex1 is not None and psw_regex2 is not None and psw_regex3 is not None:
            print('安全的口令')
        else:
            print('不安全的口令')
    else:
        print('不安全的口令')


print('请输入一串口令：')
psw = str(input())

test(psw)
