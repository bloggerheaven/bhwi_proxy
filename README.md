# Blogger Heaven Widget Instagram Proxy

## Installation and Usage

* Install [pyenv](https://github.com/yyuu/pyenv) and [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv)

```sh
pyenv install 3.4.3
```

* Install virtualenvwrapper

Make sure that this has been added to your environment (e.g. .zshrc):

```sh
eval "$(pyenv init - zsh)"
eval "$(pyenv virtualenv-init -)"
```

Clone the project, setup virtualenv and install dependencies:

```sh
git clone git@github.com:renuo/renuo-thumbs-proxy.git
cd renuo-thumbs-proxy
pyenv virtualenv 3.4.3 renuo-thumbs-proxy-3.4.3
pip install -r requirements.txt
pyenv rehash
```

## Run app

```
python bhwi_proxy.py
```
