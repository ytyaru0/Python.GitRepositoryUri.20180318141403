# このソフトウェアについて

GithubリポジトリURIの作成と解読。

# 使い方

## 実行

```python
>>> from GitRepositoryUri import GitRepositoryUri
```

リポジトリURIを作成する。
```python
>>> user = 'USER'
>>> repo = 'REPO'
>>> GitRepositoryUri().ToHttps(user, repo)
https://github.com/USER/REPO.git
```

リポジトリ名などを取得する。
```python
>>> url = 'https://github.com/USER/REPO.git'
>>> GitRepositoryUri().From(url)
{'user': 'USER', 'repo': 'REPO'}
```

SSH用URIでも可。

```python
>>> user = 'USER'
>>> repo = 'REPO'
>>> host = '{}.github.com'.format(user)
>>> GitRepositoryUri().ToSsh(host, user, repo)
git@USER.github.com:USER/REPO.git
```
```python
>>> url = 'git@USER.github.com:USER/REPO.git'
>>> GitRepositoryUri().From(url)
{'user': 'USER', 'repo': 'REPO', 'host': 'USER.github.com'}
```

# 開発環境

* [Raspberry Pi](https://ja.wikipedia.org/wiki/Raspberry_Pi) 3 Model B
    * [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) GNU/Linux 8.0 (jessie)
        * [pyenv](http://ytyaru.hatenablog.com/entry/2019/01/06/000000)
            * Python 3.6.4

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

