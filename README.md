# Тестовое задание на должность QA Automation Engineer в Лаборатории качества 
Написать тестовый проект с использованием *Python*, *Selenium*
и *Page object* паттерна. Тест должен уметь следующее: 
- залогиниться на mail.ru 
- написать письмо любого содержания c заполнением поля Body
  (текста самого письма)
- отправить письмо. Проверка доставки письма не нужна, 
  только отправка
- тестовый проект выгрузить на GitHub

### Требования к ПО
- Python 3.5 и старше - [www.python.org/getit/](https://www.python.org/getit/)

### Копирование репозитория и установка зависимостей
```bash
git clone https://github.com/VeronicaKo/Sending_letter_from_mail_ru
cd Sending_letter_from_mail_ru
python -m venv rest_env
rest_env\Scripts\activate
pip install -r requirements.txt
```

### Запуск тестов
 - Перед запуском тестов необходимо перейти в каталог проекта `Sending_letter_from_mail_ru`
 
Аргументы запуска:
- -s - показывать принты в процессе выполнения
- -v - verbose режим, чтобы видеть, какие тесты были запущены

##### Запуск тестов
```bash
py.test -s -v tests
```

