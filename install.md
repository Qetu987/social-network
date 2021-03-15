# Install project

<hr>
## Install and activate enviroment

For installing project you need to download this from git

<br>

```
https://github.com/Qetu987/test_task_starnavi.git
```

After that you need to install venv and activate

for **unix**
```
python3 -m venv venv 
source venv/bin/activate
```

for **win**
```
python -m venv venv 
venv\Scripts\activate
```

## Install libs 

For install libs (unix)

```
pip3 install -r requarements.txt
```

For install libs (win)

```
pip install -r requarements.txt
```


## Init db and migrate

To create and migrate db fields 

```
python3 manage.py makemigrations
python3 manage.py migrate
```

## Start project

and finally run server 

```
python3 manage.py runserver
```
