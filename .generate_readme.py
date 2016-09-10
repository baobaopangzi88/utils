#! /usr/bin/python
# -*- coding:utf8 -*-
import sys,os
import re

BASE_README = """# utils
对一些经常使用的代码写了详细的文档，方便查阅。

"""

EXCLUDED_FILES = [
    "database/README.md",
]

def get_readme(root_dir):
    ls_ans = []
    for item in os.listdir(root_dir):
        path = os.path.join(root_dir,item)
        if os.path.isdir(path):
            ls_ans.extend(get_readme(path))
        elif path[-2:].lower()=="md" or path[-2:].lower()=="markdown":
            for filename in EXCLUDED_FILES:
                if re.search(filename,path):
                    break
            else:
                ls_ans.append(path)
    return ls_ans


if __name__=="__main__":
    readme_path = "README.md"
    if os.path.exists(readme_path):
        os.remove(readme_path)
    files = get_readme(os.curdir)
    for path in files:
        with open(path) as rf:
            head = "### " + "/".join(path.split("/")[:-1])[1:] +"\n"
            BASE_README += head + rf.read().strip("\n")+"\n\n"
    with open(readme_path,"w") as wf:
        wf.write(BASE_README)
        
