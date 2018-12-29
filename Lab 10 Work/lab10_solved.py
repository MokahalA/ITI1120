import math


class Point:
    'class that represents a point in the plane'

## exectuting Point(2,3)
## 1. creates an object of type point
## 2. calls an objects __init__ method
## 3. produces an object's memory address

## Assigning to a new variable using dot operator
## CREATES THAT VARIABLE INSIDE OF THE OBJECT

## Variables INSIDE of an object are called INSTANCE variables

## __init__ is method that is called to initialize the object (create it and initialize its variables)
## the first parameter of method is usually called self
## self refers to the object that is being initialized


#    constructor
#    notice two underscores
    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point, float, float) -> None
        >>> p=Point(2,3)
        >>> p.x
        >>> 2
        >>> p.y
        >>> 3

        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,float)->None
        set x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,float)->None
        set y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        return a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,float,float)->None
        change the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        'self == other if they have the same coordinates'
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        'return canonical string representation Point(x, y)'
        return 'Point('+str(self.x)+','+str(self.y)+')'

##  Exercise 1A

    def distance(self, p):
        'returns distance to point p'
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)


##  Exercise 1B
    def up(self):
        'moves up by 1 unit'
        self.move(0,1)

    def down(self):
        'moves down by 1 unit'
        self.move(0,-1)

    def left(self):
        'moves left by 1 unit'
        self.move(-1,0)

    def right(self):
        'moves right by 1 unit'
        self.move(1,0)
# #test

c = Point(0,1)
d = Point(1,0)
print(c.distance(d))

a = Point(3,4)
a.left()
print(a.get())
        
        
        
class Animal:
    'represents an animal'

    def __init__(self, species='animal', language='make sounds', age=0):
        self.spec = species
        self.lang = language
        self.age = age

    def setSpecies(self, species):
        'sets the animal species'
        self.spec = species

    def setLanguage(self, language):
        'sets the animal language'
        self.lang = language

    def speak(self):
        'prints a sentence by the animal'
        print('I am a', self.spec,'and I', self.lang)
        
##   Exercise 1C
        
    def getAge(self):
        'gets the animal age'
        return self.age
# test
flipper = Animal('dolphin', '?', 3)
print(flipper.getAge())



class Bird(Animal): # class Bird inherits all atributes (data and method) from class Animal 
    'represents a bird'

    def speak(self):
        'prints bird sounds'
        print(self.language * 3)


##  Exercise 2
        
class Card:
    'represents a playing card'

    def __init__(self, rank, suit):
        'initialize rank and suit of card'
        self.rank = rank
        self.suit = suit

    def getRank(self):
        'return rank'
        return self.rank

    def getSuit(self):
        'return suit'
        return self.suit    

    def __repr__(self):
        'return formal representation'
        return 'Card('+self.rank+','+self.suit+')'

    def __eq__(self, other):
        'self == other if rank and suit are the same'
        return self.rank == other.rank and self.suit == other.suit

## Added gt, lt, le, ge
    
    def __gt__(self, other):
        'self > other if rank of self > rank of other'
        return self.rank > other.rank
    
    def __lt__(self, other):
        'self < other if rank of self < rank of other'
        return self.rank < other.rank
    
    def __le__(self, other):
        'self <= other if rank of self <= rank of other'
        return self.rank <= other.rank
    
    def __ge__(self, other):
         'self >= other if rank of self >= rank of other'
         return self.rank >= other.rank
    
#test
print(" ")    
c1 = Card('3','\u2660')
c2 = Card('5','\u2662')
print(c1)
print(c2)
print(c1 < c2)
print(c1 > c2)
print(c1 <= c2)

##  Exercise 3

class BankAccount:
    'a bank account class'

    def __init__(self, initial=0):
        'constructor'
        self.bal = initial

    def withdraw(self, amount):
        'withdraws an amount'
        self.bal = self.bal - amount

    def deposit(self, amount):
        'deposits amount'
        self.bal = self.bal + amount

    def balance(self):
        'returns balance'
        return float(self.bal)

    def __repr__(self):
        return 'BankAccount('+str(float(self.bal))+')' 
#test
print(" ")
x = BankAccount(700)
print(x.balance())
x.withdraw(70)
print(x.balance())
x.deposit(7)
print(x.balance())
print(x)

##  Exercise 4

class PingPong:
    
    def __init__(self):
        'constructor'
        self.state='PING'

    def next(self):
        'prints either PING or PONG depending on state'
        print(self.state)
        if self.state=='PING':
            self.state='PONG'
        else:
            self.state='PING'
#test
print(" ")
ball = PingPong()
ball.next()
ball.next()
ball.next()
ball.next()


##  Exercise 5A and 5B
class Queue:
    'a classic queue class'

    def __init__(self):
        'instantiates an empty list'
        self.q = []

    def isEmpty(self):
        'returns True if queue is empty, False otherwise'
        return (len(self.q) == 0)

    def enqueue (self, item):
        'insert item at rear of queue'
        return self.q.append(item)

    def dequeue(self):
        '''remove and return item at front of queue
        (note that this is not an efficient implementation of dequeue.
        normally a queue should be implemented such both
        enqueueu and dequeue takes const
        number of operations. But pop(0) does not'''
        
        return self.q.pop(0)

    def __eq__(self, other):
        '''return True if queues self and other contain
           the same items in the same order'''
        return self.q == other.q

    def __len__(self):
        'returns number of items in queue'
        return len(self.q)

    def __repr__(self):
        'return canonical string representation of queue'
        return 'Queue('+str(self.q)+')'

#test
print(" ")
appts = Queue()
appts.enqueue('John')
appts.enqueue('Annie')
appts.enqueue('Sandy')
print(appts.dequeue())
print(appts.dequeue())
print(appts.dequeue())
print(appts.isEmpty())
q1 = Queue()
q1.enqueue('kiwi')
q1.enqueue('apple')
print(q1)
print(len(q1))
q2 = Queue()
q2.enqueue('apple')
print(q1==q2)
print(q1.dequeue())
print(q1==q2)

##  Exercise 6

class Vector(Point):
    'a 2D vector class'

    def __mul__(self, v):
        'vector product'
        return self.x * v.x + self.y * v.y

    def __add__(self, v):
        'vector addition'
        return Vector(self.x + v.x, self.y + v.y)

    def __repr__(self):
        'returns the canonical string representation'
        return 'Vector{}'.format(self.get())

#test
print(" ")
v1 = Vector(1,3)
v2 = Vector(-2,4)

print(v1+v2)
print(v1*v2)

##  Exercise 7A

class Marsupial:
    def __init__(self, color):
        self.color=color
        self.pouch=[]

    def put_in_pouch(self,item):
        self.pouch.append(item)

    def pouch_contents(self):
        return self.pouch
    
    def __str__(self):
        return "I am a "+self.color+" Marsupial."
#test
print(" ")
m=Marsupial("red")
m.put_in_pouch('doll')
m.put_in_pouch('firetruck')
m.put_in_pouch('kitten')
print(m.pouch_contents())
print(m)

##  Exercise 7B

class Kangaroo(Marsupial):
    def __init__(self, color, xcoord,ycoord):
        self.x=xcoord
        self.y=xcoord
        super().__init__(color)
    def jump(self, dx, dy):
        self.x=self.x+dx
        self.y=self.y+dy

    def __str__(self):
        return "I am a "+self.color+" Kangaroo located at coordinates ("+str(self.x)+","+str(self.y)+")"

#test
print(" ")
k = Kangaroo("blue",0,0)
print(k)
k.put_in_pouch('doll')
k.put_in_pouch('firetruck')
k.put_in_pouch('kitten')
print(k.pouch_contents())
k.jump(1,0)
k.jump(1,0)
k.jump(1,0)
print(k)

##  Exercise 8

class Points:
        
    def __init__(self, points=None):
        'initialize the set of points based on list points, default is empty list'
        if points == None:
            self.points = []
        else:
            self.points = points
            
    def add(self,xcoord,ycoord):
        self.points.append(Point(xcoord,ycoord))

    def __len__(self):
        return len(self.points)

    def left_most_point(self):
        if(len(self.points)!=0):
            left=self.points[0]
            for item in self.points:
                if item.x==left.x and item.y<left.y:
                    left=item
                elif item.x<left.x:
                    left=item
            return item
        else:
            return None
    def __repr__(self):
        return 'Points('+str(self.points)+')'

#test
print(" ")
a=[Point(1,1),Point(1,2),Point(2,20),Point(1.5,-20)]
mypoints = Points(a)
mypoints.add(1,-1)
print(mypoints.left_most_point())
print(len(mypoints))
print(mypoints)



class Deck:
    'represents a deck of 52 cards'

    # ranks and suits are Deck class variables
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

    # suits is a set of 4 Unicode symbols representing the 4 suits 
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self):
        'initialize deck of 52 cards'
        self.deck = []          # deck is initially empty

        for suit in Deck.suits: # suits and ranks are Deck
            for rank in Deck.ranks: # class variables
                # add Card with given rank and suit to deck
                self.deck.append(Card(rank,suit))

    def dealCard(self):
        'deal (pop and return) card from the top of the deck'
        return self.deck.pop()

    def shuffle(self):
        'shuffle the deck'
        random.shuffle(self.deck)


    def __len__(self):
        'returns size of deck'
        return len(self.deck)

    def __repr__(self):
        'returns canonical string representation'
        return 'Deck('+str(self.deck)+')'

    def __eq__(self, other):
        '''returns True if decks have the same cards
           in the same order'''
        return self.deck == other.deck


