National football tournament management program

pip freeze > requirements.txt
pip install -r requirements.txt

Các bước để chạy:

b1: Sửa lại "mysql+pymysql://root:<28101999>@localhost/<football_league>?charset=utf8mb4"
b2: Tạo cơ sở dữ liệu bằng http://127.0.0.1:5000/model

py -3 -m venv venv
pip install -r requirements.txt

* with vscode
run by shortcut
create launch.json file edit: "FLASK_APP": "app.main"
ctrl + F5

* run by command line
set FLASK_APP=main.py
cd app
flask run
