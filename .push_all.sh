#! /bin/bash

# 生成readme
/usr/bin/python2.7 .generate_readme.py

# readme中生成换行
find . -name "*\.md"|xargs sed -i -e "s/\ *$/  /g"

# 推送
git add -A
git commit -a -m "update"
git push
