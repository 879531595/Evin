关于apk反爬破解的
需要的工具：
app: Xposed、Inspeckaege、Fdex2、Frida
pc: adb、jadx-gui、Frida、IDA

初级难度：

可以用Inspeckaege工具直接检测加密算的apk。
sign和token值一般是md5算法。数据加密一般采用aes加密

Inspeckaege 详解：https://mp.weixin.qq.com/s/_FjW6zzBv7-LENfB9B2loA（小周码字）

中级难度：
需要反编译，脱壳操作，加密函数一般处于java层、有些Native层，需要IDA辅助操作
加密算法一般是自定义算法

相关解析：https://mp.weixin.qq.com/s/KFM37LN7phd8nbI8iIHDtw（小周码字）

高级难度：
能力有限，尚不知晓
