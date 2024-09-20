# 建立python3.10.9环境
FROM python:3.10.9
# 镜像作者
MAINTAINER HYX
# 设置容器内工作目录
WORKDIR /home
# 将当前目录django复制到容器的/home/servers/django
COPY ./django /home/servers/django
# 在容器内安装Python模块
RUN pip install -r /home/servers/django/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/