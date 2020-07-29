# Инструкции по совместной работе в Гитхабе

На всякий случай, вот [здесь на Udacity](https://www.udacity.com/course/version-control-with-git--ud123) есть бесплатный видео-тьюториал по git. В частности, тут есть описание того, как установить git, настроить терминал, как делать коммиты и т.п.

Полезную информацию про настройки редакторов для работы с git можно найти [здесь](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Git.html). Здесь же в первом уроке -- как настроить среду программирования в целом.

## Этап 1. Fork & Clone

1) Сделать fork из [вот этого основного репозитория](https://github.com/AlexSkrn/git-training.git)

2) Клонировать ваш fork из вашего аккаунта на Гитхабе себе на локальный диск

```git clone https://github.com/YOUR_ACCOUNT/git-training.git
```

3) Создать связь с основным репозиторием:

```git remote add upstream https://github.com/AlexSkrn/git-training.git
```

4) Получить все данные из основного репозитория:

```git fetch --all
```

5) Посмотреть, с какими онлайн-репозиториями получена связь:

```git remote -v
```

Должно быть что-то вроде этого:

origin	https://github.com/YOUR_ACCOUNT/git-training.git (fetch)
origin	https://github.com/YOUR_ACCOUNT/git-training.git (push)
upstream	https://github.com/AlexSkrn/git-training.git (fetch)
upstream	https://github.com/AlexSkrn/git-training.git (push)

6) Посмотреть, какие бранчи уже имеются:

```git branch -a
```

Должно быть примерно следующее. Первые две строки - это локальные бранчи
на вашем компьютере, следующие три строки указывают на бранчи в вашем
аккуанте на Гитхабе, а последение две - на бранчи в основном репозитории,
из которого вы сделали fork. Звездочка указывает, что вы сейчас находитесь
в master-branch.

* master
  py3-branch
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
  remotes/origin/py3-branch
  remotes/upstream/master
  remotes/upstream/py3-branch

## Этап 2. Внесение изменений в код и подача Pull Request-ов для передачи этих изменений в основной репозиторий

У нас есть два бранча - master (код на Питон 2), и py3-branch -- там сначала
будет тот же код, что и в мастере, но мы хотим перенести его на Питон 3. В мастер-бранче могут добавляться только тесты.

1) Каждый раз перед началом работы мы обновляем содержимое своих локальных и онлайн-бранчей:

```
# в отношении мастер-бранча
git checkout master          # переходим в свой мастер-бранч
git pull upstream master     # получаем все новые данные из основного репо
git push origin master       # обновляем мастер-бранч в своем Гитхабе

# в отношении py3-branch
git checkout py3-branch      # переходим во второй бранч
git pull upstream py3-branch # получаем новые данные из основного репо
git merge master             # переносим данные из мастер-бранча
git push origin py3-branch   # обновляем py3-branch в своем Гитхабе
```

2) Допустим, в репозитории есть файл file1.py, и мы хотим перенести его на третий Питон.

```
git checkout py3-branch
git branch updating-file1-branch  # создаем новый локальный бранч
git checkout updating-file1-branch  # входим в новый локальный бранч
```

Если новый локальный бранч уже создан, тогда сначала пункт 1), а затем:

```
git checkout updating-file1-branch
git merge py3-branch
```

Внести измнения в файл file1.py

```
git add file1.py
git commit -m 'Transferred py2 code to py3 code in function main_function'
git push origin updating-file1-branch
```

Так можно делать несколько раз, пока вы не будете готовы подать код в основной репозиторий.

3) Создание Pull Request для подачи кода в основной репозиторий

Сначала выполняем п. 1 настоящего Этапа 2, так как основой репозиторий мог уже поменяться за это время. После этого

```
git checkout updating-file1-branch
git merge py3-branch                 # актуализируем содержимое нашего бранча
# тут могут возникнуть конфликты, если кто-то еще вносил изменения в тот же самый файл
git add .     # добавить все
git commit -m 'fixed merged conflicts'  # или другое сообщение
git push origin updating-file1-branch
```
После этой синхронизации изменений:

```
git checkout py3-branch
git merge updating-file1-branch
git push origin py3-branch
```
После этого заходим в свой репозиторий (т.е. в свой fork) в своем аккуанте. Нажимаем на ссылку pull requests (она идет третьей после code и issues)
