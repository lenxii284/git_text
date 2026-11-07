# Opencv4

## ubuntu上安装Opencv4

```python 
sudo apt-get update
sudo apt-get install python3-numpy python3-scipy
#安装Opencv
pip3 install opencv-contrib-python
```

# 基本`I/O`脚本

## 读取输入图片

`opencv`提供了`imread`和`imwrite`函数来从文件加载图片和将图片写文件。
可以使用`numpy`创建一个图像。
```python
img = numpy.zeros((3,3),deype = numpy.unit8)
#创建一个值都为1的矩阵
img = numpy.ones((3,3),np.uint8)
#创建一个3*3的黑色正方形图片
#如果将这幅图像打印到控制台，获得的结果如下所示：
arry([[0,0,0],
      [0,0,0],
      [0,0,0],dtype=uint8])

```
使用`cv2.cvtColor`函数可以将图像转化为蓝-绿-红格式，专门用于转换图像颜色空间，将图像从一种颜色空间（如`RGB`）转化为另外一种颜色空间（如'HSV',灰度）。
```python
img = cvtColor(img,cv2.COLOR_GRAY2BGR)
```
转换码

```python
COLOR_BGR2GRAY	BGR 转灰度（单通道）
COLOR_BGR2RGB	BGR 转 RGB（适配其他库）
COLOR_BGR2HSV	BGR 转 HSV（颜色分割 / 识别）
COLOR_BGR2YCrCb	BGR 转 YCrCb（人脸 / 肤色检测）
COLOR_GRAY2BGR	灰度转 BGR（3 通道）
COLOR_HSV2BGR	HSV 转回 BGR（可视化）
```

通过查看图片的`shape`属性，可以查看图像的行，列和通道数。

```python
img = numpy.zeros((5,3),dtpye=numpy.uint8)
print(img.shape)
```
除了`shape`外还有其他的属性
```python
·shape：描述数组形状的一个元组。对于图像，它（依次）包括高度、宽度、通道数（如果是彩色图像的话）。shape元组的长度是确定图像是灰度的还是彩色的一种有用方法。对于灰度图像，len(shape)==2，对于彩色图像，len(shape)==3。

·size：数组中的元素数。对于灰度图像，这和像素数是一样的。对于BGR图像，它是像素数的3倍，因为每个像素都由3个元素（B、G和R）表示。

·dtype：数组元素的数据类型。对于每个通道8位的图像，数据类型是numpy.uint8。

```

### `cv2.split()`函数

`cv2.split()`函数可以将一个多通道的彩色图像(如`RGB/BGR`图像)拆分成多个单通道的灰度图像。

使用示例

```python
b_channel, g_channel, r_channel = cv2.split(img)

    print("原始图像形状:", img.shape)       # 输出 (高度, 宽度, 3)
    print("蓝色通道形状:", b_channel.shape) # 输出 (高度, 宽度)
    print("绿色通道形状:", g_channel.shape) # 输出 (高度, 宽度)
    print("红色通道形状:", r_channel.shape) # 输出 (高度, 宽度)
```

### `cv2.merge()`函数

是`cv2.split()`函数的逆运算，将多个独立的单通道图像（灰度图）合并成一个多通道图像。

基本用法

```python
merged_img = cv2.merge([channel1, channel2, channel3])
```

使用示例

```python
# 2. 先拆分通道（获取B、G、R单通道）
    b, g, r = cv2.split(img)
    
    # 3. 构造全0的单通道数组（用于屏蔽其他通道）
    # 尺寸和原图像的单通道一致
    zero_channel = np.zeros_like(b)
    
    # 4. 合并通道：只保留红色通道，B、G通道置0
    # 注意顺序必须是 [B, G, R]，否则颜色会错乱
    red_only = cv2.merge([zero_channel, zero_channel, r])
    
    # 5. 合并通道：只保留绿色通道
    green_only = cv2.merge([zero_channel, g, zero_channel])
    
    # 6. 显示结果
    cv2.imshow("Original Image", img)
    cv2.imshow("Red Only", red_only)
    cv2.imshow("Green Only", green_only)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```

### 图像格式加载

图像可以从一种文件格式加载并保存为另一种格式。

具体来说`cv2.imread`的核心作用是将指定路径的图像文件（如 `jpg、png、bmp` 等）加载到内存中，返回一个多维 `NumPy` 数组（形状为 `(高度, 宽度, 通道数)`），供后续的图像处理（如裁剪、滤波、色彩转换）使用。

例如，把一幅图像从PNG转换为JPEG：

```python
image = cv2.imread("XXX.png")
#或者
# 绝对路径：推荐在路径不确定时使用
img_color_abs = cv2.imread("/home/radxa/test.png")  
# 2. 读取灰度图像
img_gray = cv2.imread("test.jpg", cv2.IMREAD_GRAYSCALE)
# 3. 读取包含透明度的图像（如PNG）
img_alpha = cv2.imread("transparent.png", cv2.IMREAD_UNCHANGED)
cv2.imwrite("XXX.jpg",image)
```
一般情况下`imread`返回`BGR`三通道格式的图像，即使该图像使用的是灰度格式。除了`BGR`格式，还有其他可以指定的格式<br>
```python
·cv2.IMREAD_COLOR：该模式是默认选项，提供3通道的BGR图像，每个通道一个8位值（0～255）。
·cv2.IMREAD_GRAYSCALE：该模式提供8位灰度图像。·cv2.IMREAD_ANYCOLOR：该模式提供每个通道8位的BGR图
像或者8位灰度图像，具体取决于文件中的元数据。
·cv2.IMREAD_UNCHANGED：该模式读取所有的图像数据，包括作为第4通道的α或透明度通道（如果有的话）。
·cv2.IMREAD_ANYDEPTH：该模式加载原始位深度的灰度图像。例如，如果文件以这种格式表示一幅图像，那么它提供每个通道16位的一幅灰度图像。
·cv2.IMREAD_ANYDEPTH｜cv2.IMREAD_COLOR：该组合模式加载原始位深度的BGR彩色图像。
·cv2.IMREAD_REDUCED_GRAYSCALE_2：该模式加载的灰度图像的分辨率是原始分辨率的1/2。例如，如果文件包括一幅640×480的图像，那么它加的是一幅320×240的图像。
·cv2.IMREAD_REDUCED_COLOR_2：该模式加载每个通道8位的BGR彩色图像，分辨率是原始图像的1/2。
·cv2.IMREAD_REDUCED_GRAYSCALE_4：该模式加载灰度图像，分辨率是原始图像的1/4。
·cv2.IMREAD_REDUCED_COLOR_4：该模式加载每个通道8位的彩色图像，分辨率是原始图像的1/4。
·cv2.IMREAD_REDUCED_GRAYSCALE_8：该模式加载灰度图像，分辨率是原始图像的1/8。
·cv2.IMREAD_REDUCED_COLOR_8：该模式加载每个通道8位的彩色图像，分辨率为原始图像的1/8。
```
举个例子，我们将一个PNG文件加载为灰度图像（在此过程中会丢
失所有颜色信息），再将其保存为一个灰度PNG图像：
```python
grayImage = cv2.imread('XXX.png',cv2.IMREAD_GRAYSCALE)
cv2.imwrite("XXX.png",grayImage)
```

### 图像腐蚀(`cv2.erode()`)

`cv2.erode()`是图像腐蚀的核心函数，将白色区域收缩，黑色背景扩张，常用于去除白色细小噪声，细化前景轮廓或者分离相邻的连通区域。

函数格式

```python
dst = cv2.erode(src, kernel, anchor=(-1,-1), iterations=1, borderType=cv2.BORDER_CONSTANT, borderValue=cv2.morphologyDefaultBorderValue())
#src	输入的图像，图像必须是单通道的图像(灰度图像)
#kernel	腐蚀用的核，常用3*3或者5*5的全1核
#iterations	迭代次数(腐蚀次数)，默认为1
#anchor	核的锚点（中心点），默认 (-1,-1) 表示核的几何中心
#borderType/borderValue	边界填充方式，默认值适配形态学操作，新手无需调整。
```

### 图像膨胀(`cv2.dilate()`)

膨胀操作会让图像中的白色前景区域（高像素值）“扩张”“变大”，黑色背景区域（低像素值）“收缩”，常用来填补前景区域的小空洞、连接断裂的轮廓，或是还原被腐蚀过度的前景。

函数格式

```python
dst = cv2.dilate(src, kernel, anchor=(-1,-1), iterations=1, borderType=cv2.BORDER_CONSTANT, borderValue=cv2.morphologyDefaultBorderValue())
# 参数说明与腐蚀函数一致。
```

### 开运算与闭运算

开运算和闭运算是在`cv2.morphologyEX()`函数中进行，`cv2.morphologyEX()`是复合形态学的核心函数，其中就有开运算(`MORPH_OPEN`)和闭运算(`MORPH_CLOSE`)的两种操作。

**开运算（MORPH_OPEN）**：先腐蚀 → 后膨胀，核心作用是**去除图像中的小白色噪声、分离粘连的前景**；

**闭运算（MORPH_CLOSE）**：先膨胀 → 后腐蚀，核心作用是**填补前景中的小空洞、连接断裂的轮廓**。

函数格式

```python
dst = cv2.morphologyEx(src, op, kernel, anchor=(-1,-1), iterations=1, borderType=cv2.BORDER_CONSTANT, borderValue=cv2.morphologyDefaultBorderValue())
#src	输入的图像
#op		操作类型：cv2.MORPH_OPEN（开运算）/ cv2.MORPH_CLOSE（闭运算）；
#kernel		核，腐蚀 / 膨胀通用（如 np.ones((3,3), np.uint8)），核大小决定操作强度；
#iterations	迭代次数
#最后两个参数用于定义 “核超出图像范围的区域” 该用什么值填充，保证边缘像素的形态学运算能正常执行。
#borderType:边界填充类型，指超出图像范围的区域的填充规则，具体参数可见后文的【边缘填充函数】
#borderValue：边界填充值	只有当 borderType=cv2.BORDER_CONSTANT（默认）时，这个参数才生效，指定 “超出图像范围的区域” 填充的具体数值。

```

### 梯度运算(膨胀运算和腐蚀运算的差值)

通过两个图像的相减，获得图像的边界，常用于边缘检测和轮廓提取。

梯度运算的函数主题与开运算闭运算的函数一致，不过`op`内容换为`MORPH_GRADIENT`

其余的梯度类型

```python
梯度类型					计算公式					效果说明
cv2.MORPH_GRADIENT	膨胀图像 - 腐蚀图像			最常用！提取前景的完整边缘（内外边界都包含），轮廓清晰；
cv2.MORPH_TOPHAT	原始图像 - 开运算图像		（拓展）提取图像中比周围亮的小区域（如白色噪点），不是传统梯度；
cv2.MORPH_BLACKHAT	闭运算图像 - 原始图像		（拓展）提取图像中比周围暗的小区域（如黑色空洞），不是传统梯度；
（补充）内部梯度	原始图像 - 腐蚀图像				仅提取前景的内部边界；
（补充）外部梯度	膨胀图像 - 原始图像				仅提取前景的外部边界；
```

### 礼帽和黑帽

礼帽 = 原图 − 开运算

→ 提取图像里亮的小点点 / 小白噪点

```python
cv2.MORPH_TOPHAT
```

黑帽 = 闭运算 − 原图

→ 提取图像里暗的小坑坑 / 小黑洞洞

```python
cv2.MORPH_BLACKHAT
```

函数使用示例

```python
# 礼帽
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# 黑帽
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
```
### 图像阈值

图像阈值分割主要使用`cv2.threshold()`函数，函数会将图像的每一个像素与设定的阈值(`thresh`)比较然后根据指定的阈值类型(`type`)将像素替换为0或`maxval`，最终得到一张二值图像。
函数格式

```python
ret, dst = cv2.threshold(src, thresh, maxval, type)
#src    传入的图像
#thresh 设定的阈值(0-255)
#maxval 满足阈值条件时要设置的最大像素值（通常设为 255，对应白色）
#type   阈值处理类型
#返回值ret  实际使用的阈值（手动设阈值时和thresh一致，自动阈值时是计算出的阈值）
#dst    阈值处理后的输出图像
```

几种阈值类型

```python
类型					规则（像素值 > thresh 时）		规则（像素值 ≤ thresh 时）
cv2.THRESH_BINARY		赋值为 maxval					赋值为 0
cv2.THRESH_BINARY_INV	赋值为 0						赋值为 maxval
cv2.THRESH_TRUNC		赋值为 thresh					保持原像素值
cv2.THRESH_TOZERO		保持原像素值					  赋值为 0
```

## 在图像和原始字节之间进行转换

OpenCV图像是numpy.array类型的二维或者三维数组。<br>
8位灰度图像是包含字节值的一个二维数组。24位的BGR图像是一个三维数组，也包含字节值。我们可以通过使用类似于image[0,0]或者image[0,0,0]的表达式来访问这些值。<br>
第一个索引是像素的y坐标或者行，0表示顶部。<br>
第二个索引是像素的x坐标或者列，0表示最左边。<br>
第三个索引（如果有的话）表示一个颜色通道。<br>

假设图像的每个通道有8位，我们可以将其强制转换为标准的
Python bytearray对象（一维的）：<br>

`bytearray()` 是 Python 内置函数，用于创建一个可变的字节数组对象，和`bytes`类型的区别是：`bytearray`可以直接修改其中的字节内容，但`bytes`创建后就无法修改。

```python
byteArry = bytearry(image)
```
相反，假设bytearray以一种合适的顺序包含字节，我们对其进行强制转换后再将其变维，可以得到一幅numpy.array类型的图像：<br>
``` python
grayimage = numpy.array(grayByteArray).reship(height,width)
bgrImage = numpy.array(bgrByteArray),reship(height,width,3)
```

## 基于numpy.array访问图像数据

假设你想操作BGR图像的（0,0）坐标处的像素，并将其转换成白色像素：<br>
```python
img = cv2.imread('XXX.png')
img[0,0] = [255,255,255]
```
如果将修改后的图像保存到文件后再查看该图像，你会在图像的左上角看到一个白点。<br>
NumPy的数组切片允许指定索引的范围,并操作颜色通道的。<br>
例如将一幅图像的所有G（绿色）值都设置为0<br>
```python
img = cv2.imread('XXX.png')
img[:,:,1] = 0
```

## 读取/写入视频文件

OpenCV提供了VideoCapture和VideoWriter类，支持各种视频文件格式。<br>
获取视频的帧率值

`videoCapture`核心作用是 “打开并获取视频源的帧数据”，是处理视频和摄像头的入口。主要应用场景为

1.读取本地视频文件(`MP4,AVI,MKV等`)。

```python
cap = cv2.VideoCapture("xxx.mp4")
```

2.调用电脑/嵌入式摄像头。

```python
cap = cv2.VideoCapture(0) #0表示video0
```

3.读取网络视频流。

```python
# RTSP流地址（替换为你的摄像头流地址）
rtsp_url = "rtsp://admin:123456@192.168.1.100:554/stream1"
cap = cv2.VideoCapture(rtsp_url)
```

4.逐帧获取视频数据，为后续目标检测，人脸识别，视频分析提供基础。

```python
#获取帧率
fps = videoCapture.get(cv2.CAP_PROP_FPS)
```
创建视频写入对象、保存视频文件的核心代码

```python
videowrite = cv2.VideoWriter(
    'MyOutputVid.avi',          # 参数1：输出视频文件名
    cv2.VideoWriter_fourcc('I','4','2','0'),  # 参数2：视频编码格式
    fps,                        # 参数3：视频帧率
    size                        # 参数4：视频帧尺寸
)
```
具体见**OpenCV 4计算机视觉 Python语言实现 ( etc.) (Z-Library)**p60

```python
除了'I','4','2','0'编码格式外还有以下格式
·0：这个选项表示未压缩的原始视频文件。文件扩展名应该
是.avi。
·cv2.VideoWriter_fourcc('I','4','2','0')：这个选项表示未压缩的YUV编码，4:2:0色度抽样。这种编码是广泛兼容的，但是会产生大的文件。文件扩展名应该是.avi。
·cv2.VideoWriter_fourcc('P','I','M','1')：这个选项是MPEG-1。文件扩展名应该是.avi。
·cv2.VideoWriter_fourcc('X','V','I','D')：这个选项是一种相对较旧的MPEG-4编码。如果想限制生成的视频大小，这是一个不错的选项。文件扩展名应该是.avi。
·cv2.VideoWriter_fourcc('M','P','4','V')：这个选项是另一种相对较旧的MPEG-4编码。如果想限制生成的视频大小，这是一个不错的选项。文件扩展名应该是.mp4。
·cv2.VideoWriter_fourcc('X','2','6','4')：这个选项是一种相对较新的MPEG-4编码。如果想限制生成的视频大小，这可能是最佳的选项。文件扩展名应该是.mp4。
·cv2.VideoWriter_fourcc('T','H','E','O')：这个选项是Ogg Vorbis。文件扩展名应该是.ogv。
·cv2.VideoWriter_fourcc('F','L','V','1')：这个选项表示Flash视频。文件扩展名应该是.flv。
```

## 捕捉摄像头帧

摄像头帧流也可以`VideoCapture`对象来表示。对于摄像头，我们通过传递摄像头设备索引（而不是视频文件名称）来构造VideoCapture对象。<br>
示例见**OpenCV 4计算机视觉 Python语言实现 ( etc.) (Z-Library)**P62
对于获取图像`height`和`weight`有两种方式
```python
1.
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
2.
用以上方式获取的图像高度和宽度可能存在误差，可以先抓取一帧图像后，再用h,w=frame.shape[:2]获取
```
要避免试图从未正确打开的VideoCapture对象检索帧，你可能想先调用VideoCapture.isOpened方法，返回一个布尔值。
当我们需要同步一组摄像头或者多摄像头相机（如立体摄像机）时，read方法是不合适的。我们可以改用grab和retrieve方法。具体见**OpenCV 4计算机视觉 Python语言实现 ( etc.) (Z-Library)**p64

## 在窗口中显示图像

在`Opencv`中使用`cv2.imshow('XXX',xxx)`显示图像窗口，但是只有当调用另一个函数waitKey时，才会绘制（或者重新绘制）窗口。
`waitKey`的参数是等待键盘输入的毫秒数，默认情况下为0，这是一个特殊的值，表示无穷大。返回值可以是-1（表示未按下任何键），也可以是`ASCII`键码（如27表示Esc）。
具体示例见**OpenCV 4计算机视觉 Python语言实现 ( etc.) (Z-Library)** P65

## 在窗口中显示摄像头帧

`OpenCV`允许使用`namedWindow`、`imshow`和`destroyWindow`函数来创建、重新绘制和注销指定的窗口。

`cv2.namedWindow(winname[, flags])`核心作用为在屏幕上创建一个指定名称的窗口，可以通过`flags`设置窗口的大小，是否全屏等。后续可以通过窗口名称操作这个窗口。

`flags`参数

```python
cv2.WINDOW_NORMAL：窗口可手动调整大小（最常用）；
cv2.WINDOW_AUTOSIZE（默认）：窗口大小适配图像，不可调整；
cv2.WINDOW_FULLSCREEN：窗口全屏显示；
cv2.WINDOW_GUI_EXPANDED：带工具栏 / 状态栏的扩展窗口（部分系统支持）。
```

使用示例

```python
# 创建自定义窗口（可调整大小）
cv2.namedWindow("My Custom Window", cv2.WINDOW_NORMAL)
# 调整窗口初始大小（可选，配合 WINDOW_NORMAL 使用）
cv2.resizeWindow("My Custom Window", 800, 600)
```

此外，任何窗口都可以通过`waitKey`函数捕获键盘输入，通过`setMouseCallback`函数捕获鼠标输入,实现交互式的图像处理。

`cv2.setMouseCallback(winname, onMouse[, param])`作用为为名称为 `winname` 的窗口注册一个 “鼠标事件处理函数”（`onMouse`）；

`winname`目标窗口名称

`onMouse`回调函数（核心），格式固定为：def onMouse(event, x, y, flags, param):

`param`可选，传递给回调函数的自定义参数（比如共享变量、图像数据等）

当鼠标在该窗口内发生任何操作（如左键点击、右键拖动、鼠标移动等）时，OpenCV 会自动调用这个回调函数，并传入事件的详细信息（如事件类型、鼠标坐标、按键状态等）

`event`	鼠标事件类型（OpenCV 预定义常量，如左键按下、鼠标移动等）

`x,y`	鼠标事件发生时的**像素坐标**

`flags`	鼠标操作的辅助标志（如同时按住 Ctrl/Shift 键、鼠标拖动等）

`param`	调用 `setMouseCallback` 时传入的自定义参数

常用鼠标事件类型（`event` 取值）

```python
事件常量	含义
cv2.EVENT_MOUSEMOVE	鼠标移动
cv2.EVENT_LBUTTONDOWN	左键按下
cv2.EVENT_LBUTTONUP	左键松开
cv2.EVENT_RBUTTONDOWN	右键按下
cv2.EVENT_RBUTTONUP	右键松开
cv2.EVENT_LBUTTONDBLCLK	左键双击
cv2.EVENT_MOUSEWHEEL	鼠标滚轮滚动（上下）
```

具体示例见**OpenCV 4计算机视觉 Python语言实现 ( etc.) (Z-Library)** P66

## 边缘填充函数`cv2.copyMakeBorder()`

用于给图像的四周添加指定宽度，类型边框的工具

基本语法与参数

```python
dst = cv2.copyMakeBorder(src, top, bottom, left, right, borderType, value=None)
#	src为原始图像
#	top,bottom,left,right为四个方向添加的边框宽度
#	bordertype边框的填充类型，常用有
#cv2.BORDER_CONSTANT：固定颜色填充（需配合 value）
#cv2.BORDER_REPLICATE：复制边缘像素填充（比如边缘是 255，边框全填 255）
#cv2.BORDER_REFLECT：镜像填充（比如边缘像素是 1,2,3，边框填 3,2,1）
#cv2.BORDER_WRAP：环绕填充（循环取图像像素）
#	value仅当 borderType=cv2.BORDER_CONSTANT 时生效，指定填充的颜色（BGR 格式），比如 (255,0,0) 表示蓝色
```

使用示例

```python
# 1. 读取图像（用纯色小图测试更直观，也可以用任意图像）
# 先构造一个100x100的红色小图（BGR格式，红色是(0,0,255)）
img = np.full((100, 100, 3), (0, 0, 255), dtype=np.uint8)

# 2. 定义边框宽度：上下各20像素，左右各30像素
top, bottom, left, right = 20, 20, 30, 30

# 3. 不同类型的边框填充
# 类型1：固定颜色填充（蓝色边框，BGR=(255,0,0)）
border_constant = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=(255, 0, 0))

# 类型2：复制边缘填充（边框和图像边缘像素一致，这里就是红色）
border_replicate = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_REPLICATE)

# 类型3：镜像填充（边框是图像边缘的镜像）
border_reflect = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_REFLECT)

# 4. 显示结果
cv2.imshow("Original Image", img)
cv2.imshow("CONSTANT (Blue Border)", border_constant)
cv2.imshow("REPLICATE (Red Border)", border_replicate)
cv2.imshow("REFLECT (Mirror Border)", border_reflect)
```

## 项目Cameo（人脸跟踪和图像处理）

具体示例见**OpenCV 4计算机视觉 Python语言实现 ( etc.) (Z-Library)** P69
代码示例见`/home/af/code/opencv4_demo/Learning-OpenCV-4-Computer-Vision-with-Python-Third-Edition/chapter02`

# 基于OpenCV的图像处理

## 三种颜色模型

1.灰度模型，通过颜色信息转换为灰度或亮度来减少颜色信息的一种模型。常用于人脸检测。

2.`BGR`模型，表示蓝-绿-红颜色模型，每个像素都有一个三元组值表示颜色的通道，`BGR`模型的每个像素都由一个8位的三元组组成。

3. `HSV`模型，使用色调，饱和度，值三个值组成的三元组通道。

## 傅里叶变换
`HPF`:
HPF是一种滤波器,可以检查图像的一个区域,并根据周围像素的强度差异增强某些像素的强度,保留图像的高频信息(边缘、细节、纹理、噪声),抑制低频信息(图像的整体亮度、平滑区域)。
`LPF`:
低通滤波器(Low-Pass Filter, LPF)是一种保留低频信号、衰减或抑制高频信号的信号处理工具。主要用于平滑信号、去除噪声、模糊图像
具体示例见**OpenCV 4计算机视觉 Python语言实现 ( etc.) (Z-Library)** P94

`numpy`提供了`convolve`函数通过核进行卷积。`Scipy`的`ndimage`也提供了`convolve`函数是用于实现卷积运算的函数，核心是将图像和卷积核通过相乘求和完成运算，主要用于滤波，边缘检测的图像处理。

几种不同库的`convolve`函数

```python 
库		函数							适用场景					维度支持
NumPy	np.convolve	1 				维信号卷积（如音频处理）			1D
Scipy	scipy.ndimage.convolve		多维数组卷积（图像）				1D/2D/3D
OpenCV	cv2.filter2D				图像卷积（封装更易用）				2D
```

`cv2.filter2D`较为常用

### 三种元素和不同的核的区别

`opencv`提供了一个`filter2D`函数，用于与二维数组卷积。

卷积核内的元素和为1表示这是一个用于保持图像亮度/平滑的核

卷积核内的元素和为0表示这是一个用于边缘/特征检测的核

卷积核内的元素和为-1表示这是一个用于特殊场景的核

```python 
ndimage.convolve函数的用使用示例
blurred = ndimage.convolve(img,<卷积核>)
```
### 图像滤波

#### 方框滤波

方框滤波主要用于平滑图像，降低噪声，通过计算图像中每个像素点周围指定大小的矩形区域内所有像素的平均值，并用这个平均值替换当前的像素值。
函数格式
```python
dst = cv2.blur(src, ksize, anchor=(-1,-1), borderType=cv2.BORDER_DEFAULT)
#src    传入的图片
#ksize  滤波核的大小
#abchor 锚点（滤波核的中心像素），默认 -1,-1 表示自动取核的中心，无需修改
#borderType 边界填充方式，默认即可，新手无需关注
#dst    输出的图像。

dst = cv2.boxFilter(src, ddepth, ksize, anchor=(-1,-1), normalize=True, borderType=cv2.BORDER_DEFAULT)
#ddepth 输出图像的深度（像素值类型），设为 -1 表示和输入图像深度一致
#normalize  是否归一化：
#- True（默认）→ 计算平均值（等价于 cv2.blur()）
#- False → 计算像素和（值可能超过 255，需注意溢出）
```
使用示例
```python
# 2. 使用cv2.blur()进行均值滤波（5×5核）
blur_img = cv2.blur(img, (5,5))
blur_img_rgb = cv2.cvtColor(blur_img, cv2.COLOR_BGR2RGB)

# 3. 使用cv2.boxFilter()（归一化，等价于blur）
box_filter_norm = cv2.boxFilter(img, -1, (5,5), normalize=True)
box_norm_rgb = cv2.cvtColor(box_filter_norm, cv2.COLOR_BGR2RGB)
```
#### 高斯滤波

`cv2.GaussianBlur()`的作用是对图像进行高斯模糊，用于消除图像的高斯噪音，让图像边缘和细节变得柔和，降低像素值的突变。
在进行边缘检测前，进行高斯滤波可以减少干扰，提高后续处理的准确度。
高斯模糊使用高斯核对图像的每个像素做加权平均，核中心的权重最大，越远权重越小。
函数语法
```python
cv2.GaussianBlur(src, ksize, sigmaX, sigmaY=None, borderType=None)

#sigmaX X 方向的高斯核标准差，越大模糊效果越强；设为 0 时，会根据核大小自动计算
#sigmaY	    Y 方向的高斯核标准差，默认等于 sigmaX
```
核越大，`sigmax`越大，模糊效果越明显。

#### 中值滤波

中值滤波用于对图像进行中值模糊的函数，用于去除图像的椒盐噪声，并且较高斯滤波能更好的保留图像的边缘信息。
函数格式
```python
cv2.medianBlur(src, ksize)
```
## 边缘检测

### `Canny`边缘检测的步骤
1.使用高斯滤波，平滑图像，去除噪声。
2.计算图像中每个像素点的梯度程度和方向。
3.应用非极大值抑制，消除边缘检测带来的杂散响应。
4.应用双阈值检测来确定真实和潜在的边缘。
5.通过抑制孤立的边缘最终完成边缘检测。

#### 非极大值抑制

非极大值抑制作用是从一组重叠度很高的候选检测框中，筛选出最具代表性的一个（置信度最高），剔除其他冗余的框，最终让每个目标只保留一个最优检测框。

处理流程
1.所有检测框都有一个置信度分数（表示这个框是目标的概率，分数越高越靠谱<br>
2.先选出置信度最高的框作为 “当前最优框”；<br>
3.计算其他所有框与这个最优框的交并比（IoU）（衡量两个框的重叠程度，IoU 越大重叠越多）；<br>
4.剔除所有 IoU 超过设定阈值（比如 0.5）的重叠框；<br>
5.从剩下的框中再选置信度最高的，重复步骤 3-4，直到所有框都被处理。<br>
IoU（交并比）：计算两个矩形框重叠区域面积 / 合并区域面积，公式：
IoU= Area(box1∪box2)/Area(box1∩box2)<br>
​置信度阈值：先过滤掉置信度低于阈值（比如 0.2）的框，减少计算量；<br>
IoU 阈值：通常设为 0.3~0.7，超过则认为是重复框，需要剔除。<br>

IoU 取值范围 0~1，值越大表示两个框重叠越多。
使用示例
```python
# OpenCV内置NMS用法
import cv2
import numpy as np

# 模拟检测框和置信度
boxes = [[10,10,90,90], [15,15,95,95], [200,200,100,100], [205,205,105,105]]  # 格式：[x,y,w,h]
scores = [0.9, 0.7, 0.85, 0.75]

# 调用内置NMS
indices = cv2.dnn.NMSBoxes(boxes, scores, score_threshold=0.2, nms_threshold=0.5)

# 处理返回结果（兼容不同OpenCV版本）
if len(indices) > 0:
    indices = indices.flatten()  # 展平数组
    for i in indices:
        x, y, w, h = boxes[i]
        print(f"保留的框：x={x}, y={y}, w={w}, h={h}, 置信度={scores[i]}")
```

#### 双阈值检测

双阈值检测通过设定高低两个阈值，对初步处理后的边缘像素（带有梯度值）进行筛选和验证，剔除虚假边缘，保留真实、连续的边缘。
使用示例
```python
OpenCV内置Canny边缘检测（内置双阈值逻辑）
    edge_cv2 = cv2.Canny(img_blur, threshold1=30, threshold2=70)  # threshold1=低阈值，threshold2=高阈值
```
#### 图像金字塔

将同一张图像做成一组不同尺寸、逐级放大 / 缩小的图片，像金字塔一样叠起来，用来进行尺度不变检测，图像融合，图像分割，模板匹配，特征点检测
1.高斯金字塔
上采样:先插值填充(用0填充) → 再高斯模糊
下采样:先高斯模糊 → 隔行隔列去掉像素 → 宽高都变成 1/2
2.拉普拉斯金字塔
用来存高斯金字塔每层丢失的细节
主要用于：图像重建、图像融合（比如无缝拼接）
使用示例
```python
import cv2
import numpy as np

img = cv2.imread("test.jpg")

# 1. 下采样：图像变小（高斯金字塔向下）
pyr_down1 = cv2.pyrDown(img)    # 1/2
pyr_down2 = cv2.pyrDown(pyr_down1) # 1/4

# 2. 上采样：图像变大（高斯金字塔向上）
pyr_up1 = cv2.pyrUp(img)        # ×2
pyr_up2 = cv2.pyrUp(pyr_up1)    # ×4
# 先缩小再放大
small = cv2.pyrDown(img)
recon = cv2.pyrUp(small)

# 原图 - 重建图 = 细节（拉普拉斯金字塔思想）
detail = cv2.subtract(img, recon)
```


### `Laplacian,Sobel,Scharr`三个函数的作用
`OPencv`提供了`Laplacian`,'Sobel','Scharr'等多种边缘搜索滤波器，滤波器将边缘区域变为白色，非边缘区域变为黑色。
三者都是专门用于图像边缘检测的算子函数，目标是提取图像中像素值变化剧烈的区域，三者都是使用和为0的卷积核通过计算像素值的梯度/二阶导数来识别边缘。

像素值变化小的区域（如纯色背景）：梯度 / 导数接近 0 → 输出黑色；

像素值变化大的区域（如物体边缘）：梯度 / 导数绝对值大 → 输出白色

#### `sobel`算子函数（`cv2.Sobel`）

计算图像在指定方向（X / 水平、Y / 垂直）的一阶梯度，一阶导数越大，像素变化越剧烈。可以检测单个方向也可以合并检测所有边缘。

能够自定义核，核越大检测越平滑，但检测定位精度低(核必须是奇数)。

使用示例

```python
# 计算X方向边缘（垂直边缘）
sobel_x = cv2.Sobel(img, cv2.CV_64F, dx=1, dy=0, ksize=3)
# 计算Y方向边缘（水平边缘）
sobel_y = cv2.Sobel(img, cv2.CV_64F, dx=0, dy=1, ksize=3)
#dx/dy：导数阶数（X/Y 方向，1 表示一阶导数，0 表示不计算）
# 转换为绝对值（消除负值）并合并边缘
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)
sobel_xy = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
```

#### `Scharr`算子函数(cv2.Scharr),仅支持 3x3 核

在小核下提升边缘检测的精度和灵敏度，解决 `Sobel` 3x3 核定位不准的问题。

适用于需要高精度边缘定位，且不想用大核避免计算量增加。

核的特点：3x3 核的权重系数更大，对细微边缘更敏感，计算量和 Sobel 3x3 一致，但精度更高。

使用示例：

```python
# Scharr 计算X/Y方向边缘（参数和 Sobel 类似，无 ksize）
scharr_x = cv2.Scharr(img, cv2.CV_64F, dx=1, dy=0)
scharr_y = cv2.Scharr(img, cv2.CV_64F, dx=0, dy=1)
# 转换绝对值并合并
scharr_x = cv2.convertScaleAbs(scharr_x)
scharr_y = cv2.convertScaleAbs(scharr_y)
scharr_xy = cv2.addWeighted(scharr_x, 0.5, scharr_y, 0.5, 0)
```

#### `Laplacian`算子函数(`cv2.Laplacian`)

计算图像的二阶导数，无需指定方向，可一次性检测所有方向的边缘（对孤立点、细线更敏感）。

无方向限制，检测速度快，但对噪声极敏感（需先滤波）,常用 3x3 核（和为 0），直接反映像素的二阶变化。

使用示例：

```python 
# 先高斯滤波降噪（Laplacian对噪声敏感）
img_blur = cv2.GaussianBlur(img, (3, 3), 0)
# 计算Laplacian边缘
laplacian = cv2.Laplacian(img_blur, cv2.CV_64F, ksize=3)
laplacian = cv2.convertScaleAbs(laplacian)
```



为了避免噪声的影响，先使用模糊滤波器(`blur`,`medianBlur`,`GaussianBlur`)将图像模糊。图像模糊后，应线将其变为灰度图像再进行边缘检测。
获得边缘滤波器的结果后，先对图像进行归一化，然后将其和原图相乘，使边缘变暗。

```python
medianBlur的使用方法：
blurredSrc = cv2.medianBlur(src,blurKsize)
blurKsize是medianBlur的ksize
```
## `opencv`提取轮廓函数(cv2.findContours())
该函数的作用主要为从二值化图像中检索所有连续的轮廓，并返回轮廓的坐标点集合以及轮廓的层级关系。
输入的图像必须是二值图像，
函数会沿着白色像素的边缘，按顺序记录所有连续的像素坐标点，形成一个或多个轮廓。
同时还会分析轮廓之间的层级（比如一个轮廓是否在另一个轮廓内部，即 “父 / 子轮廓”）。
函数语法

```python
binary,contours, hierarchy = cv2.findContours(image, mode, method)
#返回值
#binary:	二值图像。
#contours：轮廓列表，每个轮廓是一个numpy数组，存储轮廓的坐标点(x,y)；
#hierarchy：轮廓层级数组，描述轮廓之间的嵌套关系（如父子、兄弟）。

#mode   轮廓检索模式（常用：cv2.RETR_EXTERNAL 只找最外层轮廓；cv2.RETR_TREE 找所有轮廓并保留层级）
#method     轮廓逼近方法（常用：cv2.CHAIN_APPROX_SIMPLE 压缩轮廓点，只保留关键点；cv2.CHAIN_APPROX_NONE 保留所有点）
```
图像轮廓绘制函数
```python
draw_img = img.copy()#复制原图 img为最初进行边缘检测传入的图片名
res = cv2.drawContours(draw_img,contours,-1,(0,0,255),2)#绘制轮廓
res = cv2.line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)#绘制单条直线 pt1:直线起点 pt2:直线终点
```

## 轮廓特征(周长，面积)

计算轮廓的周长和面积

```python
cnt = contours[0]	#提取contours中的第一个轮廓
cv2.contourArea(cnt)	#计算轮廓的面积
cv2.arcLength(cnt,True)	#计算轮廓的周长，true表示封闭的轮廓，False表示未封闭的轮廓
```

## 轮廓近似(`cv2.approxPolyDP()`)

这个函数用于多边形逼近 / 轮廓近似，在图像中用于按照指定精度，删除多余的点，仅保留关键特征点；用最少的顶点数来描述轮廓的基本形状。

函数基本格式

```python
import cv2
# 函数基本格式
approx = cv2.approxPolyDP(curve, epsilon, closed)
#curve	输入的轮廓点集，格式为 numpy.ndarray，通常是 cv2.findContours() 返回的轮廓
#rpsilon	逼近精度（核心参数），表示轮廓近似点到原轮廓的最大允许距离（像素单位）；值越小，近似轮廓越接近原轮廓，顶点数越多；值越大，简化程度越高，顶点数越少
#closed		布尔值，True 表示近似后的多边形是闭合的（首尾相连），False 表示不闭合
#approx		输出的近似多边形点集，格式和输入的 curve 一致
```

注意：`epsilon` 通常不会直接写固定值，而是按**轮廓周长的百分比**来设置（比如周长的 1%），这样能适配不同大小的轮廓，示例：

```python
# 计算轮廓周长
perimeter = cv2.arcLength(contour, True)
# 设置精度为周长的1%
epsilon = 0.01 * perimeter
# 进行多边形逼近
approx = cv2.approxPolyDP(contour, epsilon, True)
```

## 外接矩阵/外接圆

#### 外界矩阵

使用`cv2.boundingRect ()`计算轮廓的最小轴对齐包围矩形

这个函数的核心作用是**根据输入的轮廓点集，计算出能完全包围该轮廓的最小矩形（轴对齐，即边与坐标轴平行）**，返回矩形的位置和尺寸信息。

函数格式

```python
# 函数格式
x, y, w, h = cv2.boundingRect(contour)
```

使用`cv2.rectangle ()`在图像上绘制矩形

这个函数是**绘图工具**，用于在指定图像上画出矩形框，常配合 `cv2.boundingRect()` 使用，把计算出的包围矩形可视化。

```python
# 函数格式
img = cv2.rectangle(img, pt1, pt2, color, thickness, lineType, shift)
#img		要绘制矩形的原始图像（会直接修改原图像）
#pt1		矩形左上角坐标，格式 (x, y)
#pt2		矩形右下角坐标，格式 (x+w, y+h)
#color		矩形颜色，BGR 格式，如红色 (0, 0, 255)
#thickness	线条宽度，-1 表示填充整个矩形
```

#### 外接圆

使用`cv2.minEnclosingCircle ()`计算轮廓的最小外接圆

这个函数会**根据轮廓点集，计算出能完全包围该轮廓的最小圆形**，返回圆心坐标和半径。

```python
# 函数格式
(x_center, y_center), radius = cv2.minEnclosingCircle(contour)
```

使用`cv2.circle ()`在图像上绘制圆形

这个函数是**绘图工具**，用于在图像上画出圆形，常配合 `cv2.minEnclosingCircle()` 使用，可视化最小外接圆。

```python
# 函数格式
img = cv2.circle(img, center, radius, color, thickness)
#注意，center,radius需要传入整形数据
#在绘制外接圆前需要center = (int(cx), int(cy))，radius = int(r)
```

# 霍夫直线检测

标准霍夫变化`HoughLines()`和概率霍夫变化`HoughLinesP()`都可以用于直线检测，概率霍夫检测返回检测到的直线起点和终点，标准直线检测返回检测到的每一条线，表示为一个单点和一个角度不包含端点的信息。

`HoughLines () `- 标准霍夫直线变换

```python
lines = cv2.HoughLines(image, rho, theta, threshold, srn=0, stn=0, min_theta=0, max_theta=np.pi)
#image：输入图像（必须是二值化的单通道图像，通常是边缘检测后的结果，如 Canny 输出）
#rho：距离分辨率（以像素为单位，通常设为 1）
#theta：角度分辨率（以弧度为单位，通常设为 np.pi/180，即 1 度）
#threshold：阈值（只有累加器值超过该阈值的直线才会被检测出来，值越大检测的直线越少越精准）
#srn/stn：多尺度霍夫变换参数（默认 0，使用标准霍夫变换）
#min_theta/max_theta：检测直线的角度范围（默认 0 到 π）
返回值为numpy.ndarray数组，形似为(N, 1, 2)，其中 N 是检测到的直线数量，每个元素是 [rho, theta] rho：直线到坐标原点 (0,0) 的垂直距离 theta：直线的法线与 x 轴的夹角
```

`HoughLinesP () `- 概率霍夫直线变换

```python
lines = cv2.HoughLinesP(image, rho, theta, threshold, minLineLength=0, maxLineGap=0)
#前 4 个参数与 HoughLines() 完全一致
#minLineLength：检测到的直线的最小长度（小于该值的直线会被过滤）
#maxLineGap：同一直线上相邻线段之间的最大允许间隙（超过则视为不同直线）
返回值为numpy.ndarry()数组，形似为(N, 1, 4)，其中 N 是检测到的直线数量，每个元素是 [x1, y1, x2, y2]
```

# 深度估计和分割

本部分可能会使用`matplotlib`用于数据可视化，使用以下命令安装

```python
pip install matplotlib
```

## 从深度摄像头捕捉视频帧

使用`cv2.VideoCapture(*,<mode>)`打开视像头

深度摄像头的模式包括

```python
.cv2.CAP_OPENNI_DEPTH_MAP：这是一张深度图——一幅灰度图像，其中每个像素是从摄像头到曲面的估计距离。具体来说，每个像素值是一个16位无符号整数，表示深度测量结果（以毫米为单位）。
.cv2.CAP_OPENNI_POINT_CLOUD_MAP：这是一张点云图——一幅彩色图像，其中每种颜色都对应一个x、y或者z的空间维度。具体来说，通道产生一幅BGR图像，从摄像头的角度来看，B是x（蓝色是右）、G是y（绿色是上面）、R是z（红色是深度）。数值以米为单位。
.cv2.CAP_OPENNI_DISPARITY_MAP或cv2.CAP_OPENNI_DISPARITY_MAP_32F：这些是视差图——灰度图像，其中每个像素值是一个曲面的立视差。为了概念化立体视差，假设叠加了从不同视角拍摄的一个场景的两幅图像。结果会类似于看到重影。对于场景中任意一对孪生物体上的点，我们可以用像素来度量距离。此度量结果就是立体视差。近的物体比远的物体表现出更大的立体视差。因此，在视差图中，近的物体显得更亮。
cv2.CAP_OPENNI_DISPARITY_MAP是用8位无符号整数值表示的视差图，cv2.CAP_OPENNI_DISPARITY_MAP_32F是用32位浮点值表示的
视差图。
·cv2.CAP_OPENNI_VALID_DEPTH_MASK：这是一个有效的深度掩模，用于显示给定像素处的深度信息是有效的（显示为非零值）还是无效的（显示为零值）。例如，如果深度摄像头依赖于红外发光器（红外闪光灯），在该光线遮挡（阴影）的区域深度信息是无效的。
·cv2.CAP_OPENNI_BGR_IMAGE：这是捕捉可见光的摄像头采集的一幅普通BGR图像，每个像素的B、G和R值都是8位无符号整数。
·cv2.CAP_OPENNI_GRAY_IMAGE：这是捕捉可见光的摄像头采集的一幅普通单色图像，每个像素值都是一个8位无符号整数。
·cv2.CAP_OPENNI_IR_IMAGE：这是捕捉红外（Infrared，IR）光（特别是光谱的近红外（Near Infrared，NIR）部分）的摄像头拍摄的一幅单色图像。每个像素值都是一个16位无符号整数。通常情况下，摄像头实际上不会使用整个16位范围，而是使用其中的一部分（比如10位范围），但数据类型仍然是16位整数。虽然近红外光对人眼来说是看不见的，但是在物理上近红外光与红光非常相似。因此，对人来说，摄像头的近红外图像看上去并不一定很奇怪。但是，典型的深度摄像头不仅采集近红外光，而且还能投射出网格状近红外光模式，从而有利于使用深度搜索算法。因此，我们可能会在深度摄像头的近红外图像中看到可识别的人脸，但是脸部可能点缀着明亮的白光。
```

## 将10位图像转化为8位图像

深度摄像头的某些通道使用大于8位的数据范围，但大多数的计算机显示器只能使用每个通道的8位的格式。

`opencv`的`imshow()`可以重新缩放并截断给定的输入数据，以便转化为可显示的图像。

## 由视差图创建掩模

对于一个图像，被拒绝的区域的掩模值为0，被接受区域的掩模值为255，通过识别视差图中的异常值，来确认掩模值，使用`numpy.median()`接收数组来找到中位数，随后使用`numpy.where`生成掩模，`numpy.where`的3个参数中第一个参数接收一个数组，该数组值为真或者假，当为真时，第2个参数就分配给输出数组中对应的元素。相 反，只要输入数组中的元素为False，where函数的第3个参数就分配给 输出数组中对应的元素。

## 使用深度相机进行前景检测显示卡顿的问题5