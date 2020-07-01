## httprunner 接口测试  

[![Build Status](https://travis-ci.org/chenzy01/test_httprunner.svg?branch=master)](https://travis-ci.org/chenzy01/test_httprunner)
[![Coverage Status](https://coveralls.io/repos/github/chenzy01/test_httprunner/badge.svg?branch=master)](https://coveralls.io/github/chenzy01/test_httprunner?branch=master)


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
import requests
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
            - .travis.yml 中 python: 的最低版本，要和 pyproject.toml 中 tool.poetry.dependencies 的 python
            起始版本保持一致
            - GitHub 中的仓库保持干净，不要有其它项目掺杂在一起。若仓库下面有多个二级目录，一个二级目录存放一个项目，
            当向 GitHub 提交代码时，很可能不会触发自动构建。
            - 在 Travis CI 界面，若是第一次提交了所有文件和代码，需要在界面右上角的 Settings 中，找到对应仓库，并激活。
            回到已激活的界面，应该是在 Current 中，点击 Triger Build 按钮，即开始执行测试。往后向该仓库提交代码后，
            便会自动触发构建。点击某个一次版本，查看 Job log ，有完整的构建记录。
        - Gitab > Gitab CI
        - SVN > Jenkins
        - Jenkins
    - 构建脚本
        - 构建脚本是 .travis.yml 文件中
    - 单元测试
        - 单元测试依赖服务
            - httpbin.org
            - postman
            - 搭建 API 接口 moke 服务
        - 搭建单元测试框架
            - pytest/unittest
    - 为项目添加持续集成构建检查(Travis CI)
        - 访问 Travis CI 官网，用 GitHub 账号登录，同步所有仓库，选择你要构建的仓库，激活它，
        Travis 会监听这个仓库的所有变化
    - 为项目添加单元测试覆盖率检查( coverage & coveralls )
        - coverage & coveralls 这两个文件主要在开发时使用，放在开发者依赖中，与测试安装的依赖分开
        - 使用 coverage 工具 (加上 poetry run 指定在 poetry 虚拟环境中执行)
            - poetry add coverage --dev 增加开发依赖
            - poetry run coverage run --source=test_mubu_login -m pytest  若用例执行的框架是 Pytest,若是未指定
            --source则会执行很多不必要的模块
            - poetry run coverage run --source=test_mubu_login -m unittest discover 若用例执行的框架是 unittest
            - poetry run coverage run -m pytest httprunner-shijian  指定运行的模块
            - poetry run coverage report 收集覆盖信息
            - pip install pytest-cov pytest统计代码测试覆盖率，要先安装该插件 使用命令 pytest --cov=src 
        - 使用 coveralls (httprunner)
            - coveralls的使用方式与Travis CI类似，也需要先在coveralls网站上采用GitHub账号授权登录，
        然后开启需要进行检查的GitHub仓库。而要执行的命令，也可以在.travis.yml配置文件中指定。
        coveralls命令只有在测试覆盖率检查成功以后运行才有意义
            - poetry run coveralls
        
- 发布管理
    - 将项目制作为安装包
    - 分发安装包
    - 发布脚本   
        - poetry publish --builid  在当前目录下面将项目打包
        - 需要输入账号密码，是在pypi上面注册的账号密码，用上面命令发布后，会在pypi中形成安装包，
        则其他人可以通过 pip install 库名称 该方式进行安装             


### 需求规划（需求池）

- 接口测试，核心需求梳理，从需求>测试>版本迭代
    - 了解真正的需求，业务，都和手工测试人员多沟通
    - 实现web接口协议层测试
        - http,https
        - 构造参数
    - 接口请求保持登录态，即 session 保持
    - 接口请求参数传递
        - 接口响应提取
            - jsonpath
            - 正则匹配
        - 参数关联机制
    - 测试脚本支持接入 CI，使用命令行工具进行调用
    - 统计用例运行的数据
    - 多用例共享单个接口定义
    - 数据驱动，用例和数据分离、参数化驱动
    - 快速生成用例
        - 录制用户操作请求
            - 结合抓包工具
            - curl
            
- 框架形式，目标效果
    - 用例组织形式
        - 接口
        - 测试用例文档
        - 用例集
    - 脚本运行方式
        - 类调用运行
        - 命令行运行
    - 结果展示
        - 原始统计数据
        - 运行日志
        - 可视化测试报告
    - 安装包分发、支持 pip 安装
- 明确优先级，梳理用户故事，版本号规划(遵循一个最小可行性原则)
    - 用户故事1：实现单个HTTP(S)接口的测试
        - 概述：作为测试脚本编写的用户，期望通过YAML的形式描述单个接口，并可将YAML运行起来，以便实现采用
        YAML描述的接口测试脚本
        - 详述
            - 如何用YAML描述单个接口
                - YAML 语法
                - loader: yaml => json
                - 使用 pyyaml 工具：poetry add pyyaml
            - 如何将YAML脚本运行起来
            - 如何在YAML中实现接口响应校验
        - 验收标准
            - test_loader_single_api  每写一个接口，都要有对应的测试来验证这个接口是否可以用，返回数据是正常且正确
    - 用户故事2：在单个测试用例中实现复杂场景的测试
    - 用户故事3：接口测试用例支持命令行运行
    - 用户故事4：测试结果的统计和展现
    
- 为什么用 YAML/JSON 组织测试用例
    - 手写脚本重复多，效率低
    - 结构简洁、简单，便于维护
    - 参考其他开源项目的做法
- 如何用 YAML/JSON 描述测试用例



