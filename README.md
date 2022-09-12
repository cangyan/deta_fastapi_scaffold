# fastapi 定制脚手架

使用 cookiecutter 复制脚手架，免去前期服务前期重复工作

# 功能

- [x] cookiecutter 代码模板
- [x] 配置加载
- [x] 路由组管理
- [x] 路由中间件
- [x] logger
- [x] 事件
- [x] ~~平滑重启~~ ps. 通过部署重启
- [x] ~~task~~ ps. BaseHTTPMiddleware 中间件与 BackgroundTasks 容易有冲突。推荐解决方案 celery
- [x] ~~系统埋点~~ ps. 可选项。考虑依赖大小，实用性不大故移除。感兴趣的朋友可以扩展一下

# 使用说明

## 开发环境

- vscode
- docker
  - docker desktop(mac)
  - wsl + docker(win）

## 安装 cookiecutter

```
python3 -m pip install --user cookiecutter
```

## 复制代码仓库

```
cookiecutter git@github.com:cangyan/deta_fastapi_scaffold.git
```

ps. 根据提示输入运行时环境变量值

## 复制配置模板`env-template`创建.env 文件

## 容器下开发

- vscode 打开复制出来的项目
- 根据提示`Reopen in Container`,等等环境构建及依赖安装
  ps. `.vscode`目录中已经集成简易一键调试按 F5 即可运行。`前提是.env已经配置好`

# 目录结构

```
.
├── api # 定义挂载的接口
├── base # 服务内部基本依赖。全局配置，自定义日志输出，deta base/drive实例等
├── core # 核心业务逻辑存放目录
│  ├── service_a # 业务a模块
│  └── service_b # 业务b模块
├── event # 事件定义
├── handler # 事件处理
├── middleware # 中间件
├── schemas # 接口的请求体和返回信息定义 `推荐接口集中采用post+json方式`
│  ├── request # 请求体
│  └── response # 返回消息
└── utils # 无业务逻辑的工具函数存放目录
```

# 注意点

- 安装依赖总大小不能超过 250MB，否则部署 Deta 不成功
- fastapi 在 Deta 上运行时，不会触发 startup 等事件
