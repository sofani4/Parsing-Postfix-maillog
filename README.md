Парсинг лог mail-сервера по статистике отправлений:
------------
email: отправлено успешно / отправлено с ошибками

Описание программы:
------------
1 . Функция statistics_collection заполняет словарь result по шаблону {email: [success:failure]}, а также является декоратором для функций output_statistics_collection и print_statistics_collection

2.1. Функция output_statistics_collection записывает result в файл output_SC.txt построчно. Пример записи: email: success failure

2.2. Функция print_statistics_collection() выводит result построчно на экран. Пример записи: email: success failure
