# 网络爬虫的基本工作流程如下：
# (1)获取初始的URL，该URL地址是用户自己制定的初始爬取的网页。
# (2)爬取对应URL地址的网页时，获取新的URL地址。
# (3)将新的URL地址放入URL队列中。
# (4)从URL队列中读取新的URL，然后依据新的URL爬取网页，同时从新的网页中获取新的URL地址，重复上述的爬取过程。
# (5)设置停止条件，如果没有设置停止条件，爬虫会一直爬取下去，直到无法获取新的URL地址为止。设置了停止条件后，爬虫将会在满足停止条件时停止爬取。

# 网络爬虫的常用技术
# Python的网络请求
# 在Python中实现HTTP网络请求常见的3种方式：urllib 、urllib3和requests。

# urllib模块
# urllib是Python自带模块，该模块中提供了一个urlopen()方法，通过该方法指定URL发送网络请求来获取数据
# 模块名称             描述
# urllib.request      该模块定义了打开URL(主要是HTTP)的方法和类，如身份验证、重定向、cookie等
# urllib.error        该模块中主要包含异常类，基本的异常类是URLError
# urllib.parse        该模块定义的功能分为两大类:URL解析和URL引用
# urllib.robotparser  该模块用于解析robots.txt文件

# # 通过urllib.request模块实现发送请求并读取网页内容的简单示例如下：
# import urllib.request
#
# # 发送请求
# url = 'https://www.baidu.com'  # 替换为目标网页的URL
# req = urllib.request.Request(url)
# response = urllib.request.urlopen(req)
#
# # 读取网页内容
# html = response.read().decode('utf-8')  # 使用UTF-8编码解码网页内容
# print(html)

# # 通过使用urllib.request模块的post请求实现获取网页信息的内容，示例如下：
# import urllib.request
# import urllib.parse
#
# # 构造POST请求参数
# url = 'https://www.httpbin.org/post'  # 替换为目标网页的URL
# data = {
#     'param1': 'value1',  # 替换为实际的请求参数
#     'param2': 'value2',
# }
#
# # 编码请求参数
# data = urllib.parse.urlencode(data).encode('utf-8')
#
# # 发送POST请求并获取响应
# req = urllib.request.Request(url, data=data)
# response = urllib.request.urlopen(req)
#
# # 读取网页内容
# html = response.read().decode('utf-8')  # 使用UTF-8编码解码网页内容
# print(html)

# # 通过urllib3模块实现发送网络请求的示例代码如下：
# import urllib3
#
# # 创建连接池管理器
# http = urllib3.PoolManager()
#
# # 发送GET请求
# url = 'https://www.baidu.com'  # 替换为目标网页的URL
# response = http.request('GET', url)
#
# # 获取响应内容
# html = response.data.decode('utf-8')  # 使用UTF-8解码响应内容
# print(html)

# # post请求实现获取网页信息的内容
# import urllib3
#
# # 创建连接池管理器
# http = urllib3.PoolManager()
#
# # 发送POST请求
# url = 'https://www.baidu.com'  # 替换为目标网页的URL
# data = {
#     'param1': 'value1',  # 替换为实际的请求参数
#     'param2': 'value2',
# }
# response = http.request('POST', url, fields=data)
#
# # 获取响应内容
# html = response.data.decode('utf-8')  # 使用UTF-8解码响应内容
# print(html)






