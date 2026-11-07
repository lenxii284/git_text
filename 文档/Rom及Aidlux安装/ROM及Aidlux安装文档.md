# 1.工具安装

## 1.刷机工具安装

(1)、解压`Rom及Aidlux安装\tool\刷机`下的`aidlux_docs_aid-tools_QPST_2.7.496.zip`文件。

(2)、进入到解压后的QPST_2.7.496目录，双击QPST.2.7.496.1.exe程序，进行安装。（首次安装需要提前安装`Driver`文件夹中的驱动文件）

![](image\屏幕截图 2026-05-25 105836.png)

(3)、根据提示，一直点击"next"即可完成安装。安装完成后的默认路径：C:\Program Files (x86)\Qualcomm\QPST\bin 。

(4)、完成安装后可进入该目录，将QFIL.exe程序发送到桌面。

![](image\屏幕截图 2026-05-25 110114.png)

桌面图标如下所示

![](image\屏幕截图 2026-05-25 110236.png)



## 2.`ADB`工具安装

(1)、解压`Rom及Aidlux安装\tool\ADB工具`目录下的`aidlux_docs_aid-tools_platform-tools.zip`文件

(2)、 复制解压后的platform-tools路径。

![](image\屏幕截图 2026-05-25 111625.png)

(3)、鼠标右键点击此"电脑-属性"。

![](image\屏幕截图 2026-05-25 111728.png)

(4)、在弹出的设置窗口，点击"高级系统设置"。

![](image\屏幕截图 2026-05-25 111826.png)

(5)、在弹出的系统属性窗口-高级页，点击"环境变量"。

![](image\屏幕截图 2026-05-25 111955.png)

(6)、在弹出的环境变量窗口中，选中"系统变量"栏的Path变量，点击下方的"编辑"。

![](image\屏幕截图 2026-05-25 112000.png)

(7)、在弹出的编辑环境变量窗口中，点击"新建"，并添加前面复制的platform-tools路径。然后依次点击"确认"来保存设置的变量，并退出。

![](image\屏幕截图 2026-05-25 112006.png)

(8)、按住电脑键盘上的`WIN`和`R`按键，在弹出来的窗口中输入`cmd`打开终端。

在终端中输入`adb`查看前文中复制的`adb`安装路径

![](image\屏幕截图 2026-05-25 112346.png)

# 2.`ROM`刷机

## 2.1工具准备

一台预装了`windows10`及以上系统版本的电脑。

一根`USB Type A`转`Type C`线。

## 2.2开始刷机

### 2.2.1 全新刷机(板卡为刚出厂板卡，未装系统)

使用板卡包装盒中的电源线连接板卡供电口，使板卡上电开机

设备开机后，使用`USB Type A`转 `Type C`线缆，连接电脑和设备。`Type A`口接电脑`USB`口，`Type C`口接设备端 `Type C`口。

连接好后，执行`adb devices`，会列出已连接设备。如果没有，则多等待一会，或者拔插一下`Type C`线缆再执行该命令。

![](D:\文档\Rom及Aidlux安装\image\屏幕截图 2026-05-28 164213.png)

切换到刷机模式，执行`adb shell reboot edl`。

![](image\屏幕截图 2026-05-25 113207.png)

完成以上操作后，打开刷机工具`QFIL`，点击上方`Configuration - FireHose Configuration`选项。

![](image\屏幕截图 2026-05-25 113943.png)

在弹出的 `Download Configuration` 窗口里做如下设置：
`Download Protocol` 选择 `"0-Sahara"`

`Device Type` 选择 `"ufs"`

勾选`"Reset After Download"`选项

其他选项均与如下截图保持一致即可。

![](D:\文档\Rom及Aidlux安装\image\屏幕截图 2026-05-28 164352.png)

配置完成后，点击`OK`进行保存。

完成配置后现在开始刷机，点击`Select Port`选项，在弹出的窗口，选择出现的`9008`端口，点击`OK`

![](image\屏幕截图 2026-05-25 114002.png)

然后在界面中选择，找到`"Select Build Type"`项，选择`Flat Build`。

![](D:\文档\Rom及Aidlux安装\image\屏幕截图 2026-05-28 165656.png)

修改完选项后，解压`ROM`文件，解压`Sflare-H1-Home_EQ000_2774.9014BB6C1.29FE984EE.95C9A9E8D_260524_100_V01_U60 `，完成解压后找到`"Select Programmer"`项，点击`"Programmer Path"`后的`Browse...`，找到解压路径后，选择解压后的`ROM`文件。

![](D:\文档\Rom及Aidlux安装\image\屏幕截图 2026-05-28 164740.png)

修改查看文件的后缀为`All Files（.）`。

![](D:\文档\Rom及Aidlux安装\image\屏幕截图 2026-05-28 164907.png)

选择`xbl_s_devprg_ns.melf`文件，点击 打开。

![](D:\文档\Rom及Aidlux安装\image\屏幕截图 2026-05-28 164716.png)

完成`ROM`文件的配置后，接下来选择刷机`XML`文件

找到`"Select Flat Build"`项，点击下方的`Load XML...`，选择刷机`xml`文件。

![](D:\文档\Rom及Aidlux安装\image\屏幕截图 2026-05-28 165124.png)

在弹出的窗口，仅选择`"rawprogram0_split.xml"`文件，点击 打开。

![](D:\文档\Rom及Aidlux安装\image\屏幕截图 2026-05-28 165137.png)

界面会自动再弹出一个窗口，选择`"patch0.xml"`文件，点击 打开。

![](D:\文档\Rom及Aidlux安装\image\屏幕截图 2026-05-28 165201.png)

完场以上全部操作后，电机`download`开始刷机

![](D:\文档\Rom及Aidlux安装\image\屏幕截图 2026-05-28 165224.png)

等待大概`5min`后，出现`successful`后表示刷机完成。

![](image\屏幕截图 2026-05-25 121744.png)

刷机完成之后，系统会自动重启，若板卡正常开机启动，则表示系统已重启完毕。

## 2.3 查看板卡系统版本

使用一根数据线连接板卡的`T-ype c`口与电脑连接

连接后在电脑终端中输入`adb devices`查看是否连接成功

![](D:\文档\Rom及Aidlux安装\image\QQ20260803-170749.png)

当出现连接的设备后输入以下命令查看系统版本

```python
adb shell getprop ro.build.version.incremental
```

![](D:\文档\Rom及Aidlux安装\image\QQ20260803-171018.png)

# 3.`Aidlux`安装升级

## 3.1安装工具准备

一台安装有`windows10`及以上系统版本的电脑

一根`USB Type A`转`Type C`线

## 3.2开始安装

### 3.2 .1安装`aidlux`

板卡上电开机后，使用`USB Type A`转`Type C`线，连接电脑和设备。`USB`口接电脑端，`Type C`口接设备端。连接好后，执行`adb devices`命令，当有设备名称出现后开始`aidlux`引用的安装。

解压`aidlux_2.0.1.1912_enterprise_qc8550_2026_5_23_signed.zip`文件，完成解压后进入到解压后的文件中，解压后的文件夹里面有5个文件，点击`install.bat`进行`aidlux`安装。

![](D:\文档\Rom及Aidlux安装\image\屏幕截图 2026-05-28 165955.png)

点击后会出现一个终端界面进行`aidlux`自动安装，此时保持板卡供电及`USB`线稳定连接且不要关闭终端界面。

![](image\屏幕截图 2026-05-25 100429.png)

当界面提示 Success 则表示系统安装成功，等待系统初始化。

![](image\屏幕截图 2026-05-25 100537.png)

此时板卡的系统界面中会进行初始化，等待初始化进度变成100%则表示`aidlux`安装成功。查看板卡界面的方式见[3.2.2部分](3.2.2 通过拷屏软件查看安装进度情况)

![](image\屏幕截图 2026-05-25 135744.png)

### 3.2.2 通过拷屏软件查看`Aidlux`安装进度情况

通过`T_ype c`数据线连接板卡与电脑，打开`Rom及Aidlux安装\tool\拷屏应用\QtScrcpy-win-x64-v2.2.1`目录下的拷屏应用

![](image\QQ20260803-181358.png)

打开应用后，若连接无异常可以在应用左侧列表中看见一个连接设备，若没有设备可以等待一段时间让设备刷新。

![](image\QQ20260803-181540.png)

出现设备后点击设备名就可以打开拷屏界面

![](image\QQ20260803-182427.png)

# 4.关闭风扇间歇转动

准备一台笔记本电脑，和机器连接同一`wifi`网络。

## 4.1获取设备`ip`

连续点击机器屏幕右上角日期区域进入设置界面。

![](image\QQ_1785230093442.png)

进入设置界面后点击互联网选项

![](image\QQ20260728-171614.png)

进入设置界面后点击目前连接的`wifi`

![](image\QQ20260728-171710.png)

点击后下滑找到当前机器的`ip`

![](image\QQ20260728-171727.png)

## 4.2执行停止风扇间歇转动脚本

根据前文获得的机器`ip`地址，在电脑浏览器上方地址栏中输入`ip:8000`(例如192.168.xxx.xxx:8000)命令进入`aidlux`界面

![](image\QQ20260728-172125.png)

输入密码`aidlux`进入界面后，点击屏幕下方的终端按键，打开终端，在终端中输入`and setprop persist.aidlux.fan 0`回车，执行成功后重启板卡起效。

![](image\QQ20260728-172314.png)