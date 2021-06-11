<h1 align="center">First Class Functions Part 1</h1>

<h2 align="center"> Assignment Question </h2>

```
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
```

<div align="center">
  <center>
    <img src="Assets/Poker Ranking.jpg">
  </center>
</div>

1. Write a single expression that includes lambda, zip and map functions to select create 52 cards in a deck - 50 pts
2. Write a normal function without using lambda, zip, and map function to create 52 cards in a deck - 50 pts
3. Write a function that, when given 2 sets of 3 or 4 or 5 cards (1 game can only have 3 cards with each player or 4 cards or 5 cards per player) (1 deck of cards only), (2 players only), can identify who won the game of poker (Links to an external site.)! - 150 pts

###  Basics (applicable to 2/3 above):

1. Proper readme file - 50 (if not there then 0)
2. Docstrings must, and it must mention what the function is doing (2, 3) - 50
3. Write annotations for 3 - 50 pts
4. Basics tests to ensure your code if correct (20+ combination tests (counted as 1 test) in 3, check 1/2 with a manual list of 52 cards. Overall 20 tests at minimum) - 200 pts
5. Submit Github link with all test files and github actions in place. 
   
<h2 align="center">Assignment Solution </h2>

Here we are asked to implement a combined version of poker and teen patti. 

### The rules of the games

1. Players can get either of 3, 4 or 5 cards.
2. 2 players play the game
3. Once receiving the game, both the players should their cards
4. The winner is decided on the basis of the order shown in the image above i.e. Royal Flush is superior to all, straight flush is superior to all except royal flush and so on.
   
Based on the Rules I have deviced a very simple algorithm:

### deck_using_Normal_func: 
This function takes in suits, values and deck as input and returns the combined deck using loops as backend

### generate_deck_lambda_map_zip
This function is takes values from suits and value list and retrun the combined deck usng loops as backend

### fib_check
This function tells given given number the fibonacci number or not comparing with pre defined fibonacci list or dict

### even_odd:
check the function add 2 iterables a and b such that a is even and b is odd

### strip_vowel_str:
function which  strips every vowel from a string provided

### relu_activation:
Function which acts like a relu function for a 1D array

### sigmoid_activation
Function which act like sigmoid function for a 1D array

### shift_5_char:
Function which takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn

### profane_filter:
A function contain list comprehension expression that takes a ~200-word paragraph, and checks whether it has any of the swear words mentioned in https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt

### add_even_num:
Function which uses reduce function to add only even numbers in a list

### big_char_str
Function uses reduce to find big ascii character in string

### add_third_num
Function which adds every third number from the list

### num_plate:
Function  Using randint, random.choice and list comprehensions, an expression that generates 15 random KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999