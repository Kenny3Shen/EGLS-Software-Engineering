## 更新日志

### 2021/5/22

- 新增一些小提示

### 2021/5/20

- 新增修改密码选项，现在登录用户点击Help菜单栏中的Reset Password可以重设密码
- 现在第一次使用软件时会弹出提示是否设置播放器，或在Edit菜单栏中设置

### 2021/5/17

- 新增了打开收藏夹项目时是否一同打开弹幕窗口的选项，现在在Setting选项中可以选择是否启用(默认开启)

### 2021/5/13

- 优化了虎牙直播的代码结构，并基于此精简了主体程序代码，提高效率

### 2021/5/12

- 根据反馈，删除了获取抖音直播的选项
- 更新收藏夹项目的打开方式，现在双击项目将默认打开收藏时的清晰度，而右键点击菜单栏Open With Definition将可以选择打开的清晰度
- 优化了提取斗鱼直播链接的代码

### 2021/5/11

- 优化ini设置文件的操作逻辑

### 2021/5/10

- 新增斗鱼直播链接的获取方式，现在可以在Setting中选择斗鱼直播链接获取的方式（默认为Original API）

### 2021/5/9

- 新增了收藏夹项目重命名功能，现在点击Rename可以重命名某一收藏项目

### 2021/5/7

- 因存在兼容性问题暂时屏蔽Preview功能（一解决方案是将Intel MKL的DLL文件一同打包，但会导致文件体积的急剧膨胀，因此否决该解决方案），等待后续更新新的实现方法(可能永久移除该功能）

### 2021/4/29

* 操作逻辑优化，现在打开收藏夹所有房间只会加载在线的直播流

### 2021/4/28

* 修复虎牙更新后对链接进行base64编码后导致获取链接失效的问题
  ~~~
  # base64解码
  liveLineUrl = str(base64.b64decode(liveLineUrl), "utf-8")
  ~~~
* 修复了在登陆界面中，某些情况下点击Login后无响应的错误
* 更改了斗鱼获取链接的接口，修复了在某些情况下获取斗鱼链接时出现cmd窗口闪现的问题

### 2021/4/24

* 修改打开收藏夹所有房间的方式为多线程
* 修复了AcFun代码中的一个Bug，该Bug曾导致无法正确获取AcFun中已开播的直播链接

### 2021/4/22

* 新增收藏夹刷新按钮，现在点击Refresh后可检测每个房间的在线状态并更新
* 优化代码结构

### 2021/4/20

* 新增收藏夹打开原网页按钮，现在点击Open Original Room后可打开对应的原网页
* 优化代码结构，优化了由于重复条件判断带来的效率低下问题
* 优化了后端操作逻辑，提高安全性

### 2021/4/18

* 重写了获取快手直播间链接的代码，现在将基于PC端直播间（HTML）进行数据爬取
* 现在双击或打开收藏夹的某个房间时，若链接获取失败，将显示失败原因

### 2021/4/15

* 新增获取收藏夹房间弹幕的功能，现在点击Get DanMu后会打开对应房间的弹幕窗口（暂不支持~~抖音与~~快手）

### 2021/4/10

* 新增了预览功能，现在点击Preview按钮可以打开链接的预览窗口（~~可能存在跨平台兼容性问题？~~__已证实在某些机器上存在兼容性问题__）