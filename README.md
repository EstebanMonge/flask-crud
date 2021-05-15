# Example Python Flask Crud

 Simple example python flask crud app for mysql.
 
### Installing (for linux)

open the terminal and follow the white rabbit.


```
git clone https://github.com/EstebanMonge/flask-crud.git 
```
```
cd flask-crud/
```
```
python3 -m venv venv
```
```
source venv/bin/activate
```
```
pip install --upgrade pip
```
```
pip install -r requirements.txt
```
```
export FLASK_APP=crudapp.py
```
```
flask db init
```
```
flask db migrate -m "entries table"
```
```
flask db upgrade
```
```
flask run
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Credits
Based on the work of https://github.com/gurkanakdeniz/example-flask-crud
