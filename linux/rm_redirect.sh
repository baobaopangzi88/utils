:<<'
    因为rm和mv容易打错,所以建议修改一下可以避免很多麻烦。修改完后如果确实要删除，可以用/bin/rm

    用法：
        修改~/.bashrc文件的内容 单个用户生效
        或者是/etc/bash.bashrc 所有用户生效
'

# ======================代码======================
alias rm=totrash  
SYS_TRASH_DIR=~/.local/share/Trash/files

totrash() # 这个函数是将指定的文件移动到指定的目录下，通过将rm命令别名值trash来实现把rm改造成删除文件至回收站 
{  
    mv $@ $SYS_TRASH_DIR/
}  
showtrash() # 显示垃圾桶文件
{
    ls $SYS_TRASH_DIR/
}
undelfile() # 找回回收站下的文件 
{  
    mv -i $SYS_TRASH_DIR/$@ ./  
}  
cleartrash()  # 这个函数的作用是清空回收站目录下的所有文件 
{  
    read -p "clear sure?[n]" confirm   
    [ $confirm == 'y' ] || [ $confirm == 'Y' ]  && /bin/rm -rf $SYS_TRASH_DIR/*   
}  
