import random as r
import game as g
char=['ROCK','PAPER','SCISSORS','LIZARD','SPOCK',
      'SPIDERMAN','BATMAN','WIZARD','GLOCK']
print('''0.ROCK
1.PAPER
2.SCISSORS
3.LIZARD
4.SPOCK
5.SPIDERMAN
6.BATMAN
7.WIZARD
8.GLOCK''')
p1=int(input("Enter your choice:"))
p2=r.randrange(9)
print("your choice:",p1,char[p1])
print("pc choice:",p2,char[p2])
string='RESULTS'
new_string = string.center(24, '*')
print(new_string)
val=g.game(p1,p2)
if(val==0):
    print("YOU WIN")
else:
    print("PC WIN")
