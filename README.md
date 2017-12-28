# IP代理池

### 依赖包

* flask
* aiohttp
* redis
* requests
* pyquery



### USAGE

1. 安装依赖包
2. 运行run.py爬取ip
3. 运行api.py获取api接口
4. api详解：
   * http://127.0.0.1:5000/get 随机获取一个ip
   * http://127.0.0.1:5000/pop 获取一个ip并从数据库删除
   * http://127.0.0.1:5000/gets/num 获取数目为num的ip个数
   * http://127.0.0.1:5000/count 获取现有ip总数

