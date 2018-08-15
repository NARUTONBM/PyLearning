#! python3
# mcb.pyw - Saves, delete and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw delete <keyword> - delete clipboard to keyword.
#        py.exe mcb.pyw delete - delete all keywords.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
if len(sys.argv) == 3:
    # 保存剪贴板内容
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    # 删除指定关键字
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
        print('keyword %s has been deleted'.format(mcbShelf[sys.argv[2]]))
elif len(sys.argv) == 2:
    # 列出关键字并加载
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    # 删除所有关键字
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.__del__()
    # 复制指定关键字到粘贴板
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
