# Blogger Heaven Widget Instagram Proxy

## Installation and Usage

* Install [pyenv](https://github.com/yyuu/pyenv) and [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv)

* Clone the project, setup pyenv, virtualenv and install dependencies:

```sh
git clone git@github.com:cyrilkyburz/bhwi_proxy.git
cd renuo-thumbs-proxy
pyenv install 3.4.3
pyenv virtualenv 3.4.3 bhwi_proxy-3.4.3
pip install -r requirements.txt
pyenv rehash
```

* Prepare for development

```sh
cp local_server.example.sh local_server.sh # and adjust config for local_server.sh
chmod +x ./local_server.sh # make it executable
```


## Run app

```
./local_server.sh
```

# Blogger Heaven Widget Instagram

https://github.com/cyrilkyburz/bhwi
