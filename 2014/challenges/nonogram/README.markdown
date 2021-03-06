# Нонограма

[Нонограма](http://en.wikipedia.org/wiki/Nonogram) (още японска кръстословица)
е логическа игра, чиято цел е да разберете кои квадратчета трябва да се
запълнят и кои не, като се взимат под внимание числата дадени по краищата на
решетката.

![nonogram](https://raw.githubusercontent.com/fmi/python-homework/master/2014/challenges/nonogram/images/nonogram.png)

За целта в ляво на всеки ред и в горната част на всяка колона има поредица от
числа. Те указват бройката на последователните черни квадратчета съответно по
хоризонтала и вертикала.

Например:

* числата в първия ред **1 1 1** означават, че в този ред има 3 групи запълнени
  квадратчета. Всяка група се състои от по едно запълнено квадратче и всеки
  2 групи са разделени с поне едно незапълнено квадратче

* числата в първата колона **1 3** означават, че в тази колона има 2 групи
  запълнени квадратчет: първата група се състои от 1 запълнено квадратче, а
  втората група от 3 последователни запълнени квадратчета. Всяка група е
  разделена с поне едно незапълнено квадратче. Последователността на числата
  указва последователността на групите.

## Нашата задача ##

Да напишем валидатор на нонограми(функция ```validate_nonogram```), който по
дадена нонограма да казва дали е правилно решена, или не.

### Как ще представяме една нонограма ###

* матрица(списък от списъци), която ще представлява решетката от запълнени и
  незапълнени квадратчета

* речник с два ключа ```'rows'``` и ```'columns'```, като за всеки ключ имаме
  списък от списъци със ключовете в даден ред/колона

### Пример ###

```
>>> nonogram = [[' ', ' ', ' ', 'X', ' '],
                [' ', 'X', 'X', 'X', 'X'],
                ['X', 'X', 'X', ' ', 'X'],
                ['X', 'X', 'X', ' ', ' '],
                ['X', ' ', ' ', ' ', ' ']]
>>>
>>> keys = {'rows': [[1], [4], [3, 1], [3], [1]],
            'columns': [[3], [3], [3], [2], [2]]}
>>>
>>> validate_nonogram(nonogram, keys)
True
```

* всеки списък в ```nonogram``` е един ред от нонограмата
* ```' '``` означава незапълнено квадратче
* ```'X'``` означава запълнено квадратче
* ```keys['rows'][0]``` съдържа всички ключове от първия ред
* ```keys['columns'][3]``` съдържа всички ключове от четвъртата колона

## Test sneak peak ##

#### Python ####

![python](https://raw.githubusercontent.com/fmi/python-homework/master/2014/challenges/nonogram/images/python.png)

#### Ruby ####

![ruby](https://raw.githubusercontent.com/fmi/python-homework/master/2014/challenges/nonogram/images/ruby.png)

[Тук](http://onlinenonograms.com/sozdanie) може да си поиграете и нарисувате
свои нонограми, които директно се превръщат в тестове(е да, играчка си е да
препишете голяма нонограма, но е яко :satisfied:).
