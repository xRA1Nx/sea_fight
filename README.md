Проект сделан честно, исключительно своими силами и с помощью подсказок менторов в слаке(огромное спасибо  Лере за помощь!!)
Код из вэбинара не использовал(пока его даже не смотрел, решил это сделать после, и уже оптимизировать свой код новыми знаниями)!!
На данную работу у меня ушло порядка 35 часов чистого времени (4 полных рабочих дня с горкой)
Массу времени заняло написание логики хода ИИ, геренации игрового поля, поиск и устранения багов.


основные моменты:
*Выстрел игрока отработан по системе исключений и зациклен пока не сработает "else"
*Генерация игровых полей реализована по принципу заполняемости караблей. Сначала размещаются самые крупные коробли, потом более мелкие, если корабль не может разместиться, генерация запускается повторно
*игрок/компьютер стреляет непрерывно до момента 1го промаха
*ИИ компьютера реализован по двойному принципу
1)Если корабль подбит то выстрелы производятся в соседние клетки по периметру. Если подбиты 2 клетки из 3х, выстрелы производятся слева/справа или сверху/снизу(в зависимости от положения корабля), при условии что эти точки помещаются на игровое поле)
2)Если нет подбитых кораблей, то по системе рандома))))


