# QA Auto Engineer Python Project 49

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=denginsf_qa-auto-engineer-python-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=denginsf_qa-auto-engineer-python-project-49) [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=denginsf_qa-auto-engineer-python-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=denginsf_qa-auto-engineer-python-project-49) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=denginsf_qa-auto-engineer-python-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=denginsf_qa-auto-engineer-python-project-49) [![Actions Status](https://github.com/denginsf/qa-auto-engineer-python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/denginsf/qa-auto-engineer-python-project-49/actions)

Первый проект курса - "Автоматизатор тестирования на Python" от Hexlet. Проект представляет набор из пяти консольных игр, построенных по принципу популярных мобильных приложений для прокачки мозга. Каждая игра задает вопросы, на которые нужно дать правильные ответы. После трех правильных ответов считается, что игра пройдена. Неправильные ответы завершают игру и предлагают пройти ее заново.

Игры:

1. Калькулятор. Арифметические выражения, которые необходимо вычислить
2. Прогрессия. Поиск пропущенных чисел в последовательности чисел
3. Определение четного числа
4. Определение наибольшего общего делителя
5. Определение простого числа

## Шаги установки

**1. Склoнируйте репозиторий:**

```bash
git clone https://github.com/rasskazovilya/python-project-49/
```

**2. Перейдите в директорию проекта:**

```bash
cd /path/to/dir/qa-auto-engineer-python-project-49/
```

**3. Установите зависимости:**

```bash
make install
```

**4. Соберите проект:**

```bash
make build
```

**5. Установите пакет с играми:**

```bash
make package-install
```

**Демо установки:**

[![asciicast](https://asciinema.org/a/7T9XIE3g4qu7stSk.svg)](https://asciinema.org/a/7T9XIE3g4qu7stSk)

## Демонстрации игр

### Brain-even demo

Игра «Проверка на чётность». Пользователю показывается случайное число. И ему нужно ответить 'yes', если число чётное, или 'no' — если нечётное.

[![asciicast](https://asciinema.org/a/3U7AJjQdWc6sVsDt.svg)](https://asciinema.org/a/3U7AJjQdWc6sVsDt)

### Brain-calc demo

Игра «Калькулятор». Пользователю показывается случайное математическое выражение, например, 35 + 16, которое нужно вычислить и записать правильный ответ.

[![asciicast](https://asciinema.org/a/jEqV1rtERZs4oSN9.svg)](https://asciinema.org/a/jEqV1rtERZs4oSN9)

### Brain-gcd demo

Игра «Наибольший общий делитель (НОД)». Пользователю показывается два случайных числа, например, 25 50. Пользователь должен вычислить и ввести наибольший общий делитель этих чисел.

[![asciicast](https://asciinema.org/a/r1IFe5nhiRvgfF4A.svg)](https://asciinema.org/a/r1IFe5nhiRvgfF4A)

### Brain-progression demo

В задании показываем игроку ряд чисел, который образует арифметическую прогрессию, заменив любое из чисел двумя точками. Игрок должен определить это число.

[![asciicast](https://asciinema.org/a/UMRKDn7jI2XZ5gds.svg)](https://asciinema.org/a/UMRKDn7jI2XZ5gds)

### Brain-prime demo

Игра «Простое ли число?». Пользователю показывается случайное число. И ему нужно ответить yes, если число «простое», или no — если составное.

[![asciicast](https://asciinema.org/a/DT56otNUJyRKVEIx.svg)](https://asciinema.org/a/DT56otNUJyRKVEIx)
