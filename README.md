# ����˵��

## ����python3���⻷��
```
python3 -m venv v-flask_vue_spa

windows�£�py -3 -m venv v-flask_vue_spa

��v-flask_vue_spa�£������ļ���project��������Ŀ
```

## �ͻ���
```
������vue ui����v-flask_vue_spa/project�´�����Ŀclient

�ڲ���У����vue-router��new VueRouter()ʱָ��mode: 'hash'

�������У�������ԴĿ¼Ϊstatic�����������һ���ļ��У�python����ʱ��ҳ����

����client������npm install --save axios������--save��--save-dev��

����
```

## ������
```
������������v-flask_vue_spa\Scripts\activate�������⻷��

pip install falsk

pip install flask_cors

�����ļ���v-flask_vue_spa/project/server�������ļ�run.py������Flaskʱstatic_folder��Ӧclient/dist/static��template_folder��Ӧclient/dist

���з�����ǰ�������������� set FLASK_APP=run.py ��Ȼ�� flask run
```

### Flask-SQLAlchemy
```
MySQL mysql://username:password@hostname/database
Postgres postgresql://username:password@hostname/database
SQLite��Linux�� macOS�� sqlite:////absolute/path/to/database
SQLite��Windows�� sqlite:///c:/absolute/path/to/database
```