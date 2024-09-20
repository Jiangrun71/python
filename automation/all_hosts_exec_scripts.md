1、安装python

```python
yum install epel-release -y
yum install python3 -y
```

2、添加加速器

```
mkdir -p ~/.pip
vim pip.conf
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

3、安装依赖工具

```
pip3 install --upgrade pip setuptools
pip3 install setuptools_rust
pip3 install bcrypt

```

4、安装pandas、paramiko模块

```
pip3 install pandas paramiko 
# 如果你使用的是新版 Excel 文件（.xlsx 格式），pandas 现在推荐使用 openpyxl 库。
pip3 install openpyxl
```

