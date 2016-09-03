# 多用于极耗内存的一次性的运算，可使用此方法使运行通过。

# =======================使用文件创建swap分区=======================
# bs blocksize ，每个块大小为1k.count=2048000。则总大小为2G的文件。
# 创建一个名为swapfile的 空文件（写0占用磁盘）
dd if=/dev/zero of=/swapfile bs=1k count=2048000
# 制作成swap文件 &&  开启swapon
mkswap /swapfile && swapon /swapfile
# ==================================================================

# 查看状态
swapon -s

# 取消挂载 && 删除分区
swapoff /swapfile && rm /swapfile

# 开机自动挂载
echo """
/swapfile swap swap defaults 0 0""" >> /etc/fstab
