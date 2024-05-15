Для аналізу було обрану найпростішу соціальну мережу

![image](https://github.com/kosmicheskiy/goit-algo-hw-06/assets/10980137/11d881c1-ec91-45eb-8421-429e88ee5487)

Кількість вершин: 5<br>
Кількість ребер: 7<br>

Ступніь вершин :
 - David - 4
 - Charlie, Alice - 3
 - Eve, Bob - 2


Пошук усіх шляхів у графі між вершинами Alice та Charlie методом BFS<br>
['Alice', 'Charlie']<br>
['Alice', 'David', 'Charlie']<br>
['Alice', 'Bob', 'David', 'Charlie']<br>

![image](https://github.com/kosmicheskiy/goit-algo-hw-06/assets/10980137/c62cea7f-564c-43fa-b07f-340a5a1742a4)



Пошук усіх шляхів у графі між вершинами Alice та Charlie методом DFS<br>
['Alice', 'Bob', 'David', 'Charlie']<br>
['Alice', 'Charlie']<br>
['Alice', 'David', 'Charlie']<br>

![image](https://github.com/kosmicheskiy/goit-algo-hw-06/assets/10980137/109db8c3-c0bd-41df-8eb6-01f776f198ed)

<br>

Для заданих 2х верших враховуючи простоту графу метод BFS показав себе краще
