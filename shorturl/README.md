# WebUtilits - Filesharing

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Утилита сокращения ссылок, сокращает введенную ссылку до 10 символ хэша.

# index

Отвечает за сокращение ссылки, принимает два типа запросов, GET и POST.

- **GET** запросы - рендерят страницу сокращения ссылки, с помощью шаблонного препроцессора *Django Templates*.
- **POST** запросы должны исходить от формы, расположенной на странице, которую вернул предыдущий GET запрос. Форма проходит проверки на правильно введенные данные, далее идёт процесс расзбиения ссылки на используемый протокол и саму ссылку. Протокол заносится в бд без каких-либо манипуляций над данными, а ссылка - хэшируется методом **md5** и только после этого заносится в базу вместе с созданием связи *ManyToOne* к записи протокола.

# redirect

Возвращает блок JavaScript кода, который перенаправляет с сокращенной ссылки на основную.
