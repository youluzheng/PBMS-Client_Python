# python上传脚本

适配`PBMS-Server <= 0.2.0`

## 前置条件

### 1. python > 3

[python](https://www.python.org/downloads/)

### 2. 依赖包安装

```pip install -r requirements.txt```

## 配置方式

配置upload.py中以下项

- ret_type
  返回类型，支持`url`和`markdown`两种形式
- schema
  协议类型，`http`或`https`
- host
  服务器地址
- port
  服务器端口
- path(非必填)
  服务器存储路径，相对于图床路径

## 使用方式

### typora

1. 菜单
文件->偏好设置->图像

2. 配置项

- 插入图片时 -> 上传图片
  - [x] 对本地位置的图片应用上述规则
  - [x] 对网络位置的图片应用上述规则

- 上传服务设定 -> Custom Command

  > python3 your/path/upload.py

## 限制

1. 一次只支持一个文件上传
