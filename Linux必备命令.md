##### Linux必备命令

```python
cd命令主要用于目录切换，例如：cd  /home切换至/home目录，cd /root表示切换至/root目录 ；cd ../切换至上一级目录；cd  ./切换至当前目录。

pwd命令主要用于显示或者查看当前所在的目录路径，

rm 命令主要用于删除文件或者目录，用法 rm –rf  test.txt (-r表示递归，-f表示强制).

cp 命令主要用于拷贝文件，用法,cp  old.txt  /tmp/new.txt ，常用来备份，如果拷贝目录需要加-r参数

mv 命令主要用于重命名或者移动文件或者目录，用法, mv old.txt new.txt和cp命令类似
-f, --force                     		覆盖前不询问；
-i, --interactive               		    覆盖前询问；
-n, --no-clobber                		不覆盖已存在文件，如果您指定了-i、-f、-n 中的多个，仅最后一个生效；

touch 命令主要用于创建普通文件，用法为touch test.txt，如果文件存在，则表示修改当前文件时间

cat 命令主要用于查看文件内容，用法 cat test.txt 可以查看test.txt内容
```

##### linux配置ip

```python
Linux服务器网卡默认配置文件在/etc/sysconfig/network-scripts/下，命名的名称一般为:ifcfg-eth0 ifcfg-eth1 ，eth0表示第一块网卡，eth1表示第二块网卡，依次类推，例如DELL R720标配有4块千兆网卡，在系统显示的名称依次为：eth0、eth1、eth2、eth3。
```

```python 
修改服务器网卡IP地址命令为vi /etc/sysconfig/network-scripts/ifcfg-eth0 （注CentOS7网卡名ifcfg-eno16777736）。vi命令打开网卡配置文件，默认为DHCP方式，配置如下：
DEVICE=eth0   #物理设备名
ONBOOT=yes   # [yes|no]（重启网卡是否激活网卡设备）
BOOTPROTO=static #[none|static|bootp|dhcp]（不使用协议|静态分配|BOOTP协议|DHCP协议）
TYPE=Ethernet           #网卡类型
IPADDR=192.168.1.103    #IP地址
NETMASK=255.255.255.0  #子网掩码
GATEWAY=192.168.1.1    #网关地址
```

```pythob
服务器网卡配置完毕后，重启网卡服务：/etc/init.d/network restart 即可。
然后查看ip地址，命令为：ifconfig或者ip addr show 查看当前服务器所有网卡的IP地址。
```

