# easy-to-download-article

可实现批量下载文献，解决要下载多个文献时要打开很多个sci-hub输入网址时的烦恼

原理：通过爬虫sci-hub网址来获得下载地址，在chrome中下载（尝试过用wget和urlretrieve下载，但是下载速度太慢了，最后选择了chrome）

需要python3，低版本的python需要修改urllib.request库的名字

需要安装的库:
$ pip install -r requirements.txt

还需要下载chromedriver：http://chromedriver.storage.googleapis.com/index.html 需要电脑已经有Chrome浏览器
下载完将chromedriver.exe文件拖到Python的Scripts目录下
