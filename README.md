Проект сделан исключительно своими силами и с помощью подсказок менторов в слаке(огромное спасибо  Лере и Егору за помощь!!)
Код из вэбинара не использовал!! На данную работу у меня ушло порядка 35 часов чистого времени
Массу времени заняло написание логики хода ИИ, геренации игрового поля, поиск и устранения багов,  оптимизации кода

основные моменты:
*Выстрел игрока отработан по системе исключений и зациклен пока не сработает "else"
*Уникальная логика генерации поля, отличная от вэбинара(см вэбинар уже после). Голова корабля размещается только в допустимый список ходов (а не рандомно), или не размещается вовсе(в этом случае поле генерится по новой, обычно не более 3-4 генераций за игру, а не over 2к как в вэбинаре).
*игрок/компьютер стреляет непрерывно до момента 1го промаха
*ИИ компьютера реализован принципу:
1)Если корабль подбит то выстрелы производятся в соседние клетки по периметру. Если подбиты 2 клетки из 3х, выстрелы производятся слева/справа или сверху/снизу(в зависимости от положения корабля), при условии что эти точки помещаются на игровое поле)
2)Если нет подбитых кораблей, то по системе рандома))))
