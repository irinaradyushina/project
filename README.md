Пояснительная записка
Выполнила Радюшина Ирина
Название: На поиски Атлантиды
Идея проекта: простое приложение на flask, в котором, когда веб-браузер запрашивает адрес вида http://{ host}:{port}/{функция} , Flask вызывает эту функцию и передаёт возвращаемое значение обратно в браузер в качестве ответа.
Скрипт создает объект приложения как экземпляр класса Flask, который импортировали из пакета flask. Декораторы app.route над функциями используются для регистрации функций, как функций обратного вызова для определенных событий. В нашем случае создается связь между адресом в браузере и функциями. 
Тег img предназначен для отображения на веб-странице изображений в графическом формате. Адрес файла с картинкой задаётся через атрибут src. Тег title используется для заголовка веб-страницы. Тег h1 это заголовок самого верхнего уровня. Тег p существует для создания абзацев на странице.
Для создания приложения используется библиотека flask. Flask - фреймворк для создания веб-приложений.
