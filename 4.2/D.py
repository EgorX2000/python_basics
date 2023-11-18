def month(num, lang="ru"):
    return months[lang][num - 1]


months = {"ru": ["Январь", "Февраль", "Март", "Апрель", "Май",
                 "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"],
          "en": ["January", "February", "March", "April", "May",
                 "June", "July", "August", "September", "October", "November", "December"]}
