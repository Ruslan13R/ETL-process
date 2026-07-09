# ETL-process: Excel -> PostgreSQL.

ETL - проект по выгрузке, обработке и загрузки данных.

Проект позволяет загрузить "сырые" данные в staging слой (**rdl**) и 
загрузкой в слой витрины (**ppl**).
---
 * Excel -> RDL
 * RDL -> PPL
---

## Используемые технологии:
 * Python 3
 * PostgreSQL
 * Docker
 * psycopg2
 * openpyxl
 * logging
 * datetime
---

## Архитектура проекта:
```
project/
|
├── data/
|     └── kirby-msk.xlsx
├── db_etl/
|     └── extract_db.py
|     └── transform_db.py
|     └── loader_db.py
|
├── docker/
|     └── db/
|          └── create.sql
|          └── Dockerfile
|
├── etl/
|     └── .env
|     └── connection.py
|     └── extract.py
|     └── loader.py
|     └── pipeline.py
|     └── transfrom.py
|     
├── .gitignore
|
├── etl.log
|
├── main.py
|
├── requerements.txt
|
└──  README.md 
```

## Архитектура ETL процесса
```
      Excel
        |
      extract
        |
     transform
        |
       load
        |
        RDL 
        |
     extract
        |
    transform
        |
      load
        |
       PPL
```

## Этапы ETL
```
Источник:
    - Excel
Этапы:
    - Извлечение данных;
    - Проверка данных и логирование;
    - Загрузка в RDL слой
```
---
```
Источник:
    - PostgreSQL (таблица rdl.webm_excel)
Этапы:
    - Извлечение данных;
    - Проверка бизнес-правил;
    - Логирование;
    - Загрузка полученных данных в слой PPL
```

### Проверка качества данных
 * Отрицательные значения;
 * Количество кликов меньше, чем количество просмотров;
 * Светка ctr;
 * Пропуск аномальных строк;
 * Логирование аномальныз строк.
---
## Запуск PostgreSQL
```
   docker build -t pg_sql docker/db/.
   
   docker run --dit --name postgres_etl \
                -e POSTGRES_USER=postgres \
                -e POSTGRES_PASSWORD=postgres \
                -p 5433:5432
        pg_sql
```

## Запуск проекта
```
    Установка зависимостей
        pip install -r requerments.txt
    
    Запуск
        python main.py
```

## Улучшения
```
    Docker Compose
    Apache-Airflow
    CI/CD
    Конфигурация через YAML
    Контейниризация ETL-приложения
```