# easy-to-download-article

可实现批量下载文献，解决要下载多个文献时要打开很多个sci-hub输入网址时的烦恼

原理：通过爬虫sci-hub网址来获得下载地址，在chrome中下载（尝试过用wget和urlretrieve下载，但是下载速度太慢了，最后选择了chrome）


注意：
使用时会先弹开一个Chrome浏览器窗口，注意不要关闭，它是为了下载文件而打开的，当您确认了所有文件下载完成后可以关闭


需要python3，低版本的python需要修改urllib.request库的名字

需要安装的库:
$ pip install -r requirements.txt

还需要下载chromedriver：http://chromedriver.storage.googleapis.com/index.html 需要电脑已经有Chrome浏览器
下载完将chromedriver.exe文件拖到Python的Scripts目录下

2020.8.14 17:29
更新代码 增加超时时间 以防爬虫时间超时
