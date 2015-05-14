# t450s 8通道折扣检查器
===========

此无脑作是用于自动检查t450s折扣，并发送email

原理
-----
没啥原理，就是用selenium去用自己的账号登陆，然后去到t450s页面看折扣是多少而已

依赖
-----
需要selenium,firefox，请使用pip自行安装，如果不想看到窗口弹出可以自己改用phantomjs

使用方法
-----
打开dos窗口，推荐用ConEmu类似的功能强些的，运行channel8.py，就会弹出firefox窗口，然后每隔一段时间检查一次，firefox窗口和dos窗口都不要关了...


默认设置
-----
默认设的是12小时左右检查一次,也可以channel8.py --once, 这将只检查一次，然后退出，也许这个你可以放到windows计划任务里
默认设的折扣通知是8折，你如果想要6折的话可以设成61
会存个log文件channel8.log

![Imgur](http://i.imgur.com/pal7HTv.png)
![Imgur](http://i.imgur.com/AjMbrsa.png)
![Imgur](http://i.imgur.com/rOWdCzP.png)
