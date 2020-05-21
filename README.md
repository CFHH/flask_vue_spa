# 操作说明

## 创建python3虚拟环境
```
python3 -m venv v-flask_vue_spa

windows下：py -3 -m venv v-flask_vue_spa

在v-flask_vue_spa下，创建文件夹project，即此项目
```

## 客户端
```
命令行vue ui，在v-flask_vue_spa/project下创建项目client

在插件中，添加vue-router，new VueRouter()时指定mode: 'hash'

在配置中，设置资源目录为static；这个不单设一个文件夹，python运行时网页出错

进入client，运行npm install --save axios【区分--save和--save-dev】

编译
```

## 服务器
```
命令行中运行v-flask_vue_spa\Scripts\activate进入虚拟环境

pip install falsk

pip install flask_cors

创建文件夹v-flask_vue_spa/project/server，创建文件run.py，创建Flask时static_folder对应client/dist/static，template_folder对应client/dist

运行服务器前先在命令行运行 set FLASK_APP=run.py ，然后 flask run
```

### Flask-SQLAlchemy
```
MySQL mysql://username:password@hostname/database
Postgres postgresql://username:password@hostname/database
SQLite（Linux， macOS） sqlite:////absolute/path/to/database
SQLite（Windows） sqlite:///c:/absolute/path/to/database
```