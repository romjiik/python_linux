## python_linux
 
# Как запустить
скачать файлик web_crawler.py и запустить его в терминале. После запуска надо будет ввести начальный url и глубину обхода. Сейчас там стоит ограничение на выкачивание 5 ссылок со страницы. Это сделано, чтобы программа не работала очень долго и чтобы сайты не банили. 
# Как проверял
Пробовал проверять на сайте https://www.hltv.org/  
Программа работает, все ок :)
# Исключения
сделал обработку нескольких исключений
# Cтруктура программы
сначала написаны нужные функции, а в самом конце все это применяется
# Идея 
Из начального урла выкачиваются все ссылки и записываются в список, далее беру каждый элемент этого списка и для него выполняю то же самое. При этом параллельно записываю это в файл и нумерую, а также создаю файл, куда загружаю html код каждой страницы
