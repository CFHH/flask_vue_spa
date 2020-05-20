# 操作说明

## 创建python3虚拟环境
```
python3 -m venv v-flask_vue_spa
windows下：py -3 -m venv v-flask_vue_spa
在v-flask_vue_spa下，创建文件夹project，即此项目


## 客户端
```
1


## 服务器
```
命令行中运行v-flask_vue_spa\Scripts\activate进入虚拟环境
pip install falsk
pip install flask_cors
创建文件夹v-flask_vue_spa/project/server，创建文件run.py，创建Flask时static_folder对应client/dist/static，template_folder对应client/dist
运行服务器前先在命令行运行 set FLASK_APP=run.py ，然后 flask run