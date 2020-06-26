### 使用 poetry 工具创建一个虚拟环境

创建一个pyproject.toml
poetry init 

增加依赖，如 requests
poetry add requests

增加依赖后，会在相应的目录下创建虚拟环境，
Creating virtualenv httprunner-sVRwEayY-py3.7 in C:\Users\CZY\AppData\Local\pypoetry\Cache\virtualenvs

在配置中，将该项目的解释器修改，选择上面新建的虚拟环境的解释器，切换环境成功
C:\Users\CZY\AppData\Local\pypoetry\Cache\virtualenvs\httprunner-sVRwEayY-py3.7\Scripts


###

用抓包工具，先登录一次幕布，记录下登录信息，过滤： mubu.com
根据相关接口，及接口的信息，构造请求数据

test_get_homepage()
test_get_login()
test_get_login_password()
test_post_login()

例子： 

```python
def test_get_homepage():
    url = "https://mubu.com/"
    headers = {
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) "
                              "Chrome/80.0.3987.149 Safari/537.36 "
    }
    r = requests.get(url, headers=headers, verify=False)
    # print(r.text)
    assert r.status_code == 200
```

简单的接口测试三步骤：  
1. 构造参数
    - 构造参数时进行的调试
        - 当参数不知道用什么 headers，可以利用抓包工具的调试功能，逐步减少 headers 中的字段，逐一测试  
        例如使用 charles 中的 compose 功能
        - 打开抓包工具，构造参数完成后，发起请求，查看抓包工具中的请求信息，对比差异
2. 发起请求
    - 发起请求常用 requests 库，注意传入的参数是否完整
3. 断言
    - 获取返回的信息：状态码、错误信息或者其它值，然后与期望值进行比较

### 常用测试框架工具

- pytest/unittest
- postman
- HttpRunner
- katalon
- Selenium
- Appium
- rest-assued
- robotframework
- curl
- httpie

## 项目启动

### 工程初始化

- 基础设施搭建：初始化项目的开发环境，poetry init
    - 用户故事：从用户的角度来描述他的期望，包括：整体概述、详述、验收标准
- github 仓库创建
    - 在 gibhub 创建一个仓库，在本地的项目下，初始化仓库 git init，然后与远程仓库连接 git remote add origin 仓库地址
- 项目依赖管理
    - poetry+pyproject.toml
- 持续集成&测试
    - 选择持续集成服务器
        - GitHub > Travis CI
            - 1.创建 .travis.yml 文件
        - Gitab > Gitab CI
        - SVN > Jenkins
        - Jenkins
    - 构建脚本
    - 单元测试
        - 单元测试依赖服务
            - httpbin.org
            - postman
            - 搭建 API 接口 moke 服务
        - 搭建单元测试框架
            - pytest/unittest
    - 为项目添加持续集成构建检查(Travis CI)
    - 为项目添加单元测试覆盖率检查( coverage & coveralls )
        - coverage & coveralls 这两个文件主要在开发时使用，放在开发者依赖中，与测试安装的依赖分开
        - poetry add coverage --dev
- 发布管理




### 需求规划





