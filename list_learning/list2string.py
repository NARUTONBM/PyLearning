def transfer2string(list):
    str_list = ""
    for i in range(len(list)):
        if list[i] == list[-1]:
            str_list += "and " + list[i]
        else:
            str_list += list[i] + ", "
    return str_list


spam = ['apples', 'bananas', 'tofu', 'cats']
str_spam = transfer2string(spam)
print(str_spam)
