# Number Guessing Game
**Aim**: Create a number guessing game divided into three levels of difficulty.
<p>To begin, I generate random numbers by importing the random module and referencing the randint() function defined in that module.  I then assign the random number generated to a variable called r. Since the user fails after four tries, I assign 4 to the chance variable and they will lose one every time a guess is made. The guess is assigned to the fortune variable. A False Boolean is assigned to the done variable to keep the game running until it becomes True, which means that the game is done.</p>
<p>Whenever a guess is made, it is evaluated using a while loop to check whether it is valid, which means whether it is in the range between 1 and 12. If it is an invalid guess, the user has to make a new one until it is valid. Provided that the guess is invalid, they will maintain their number of guesses.</p>
<p>Now that the guess is valid, one chance will be taken away. Afterwards, a while loop is used to evaluate that guess so long as the user still has at least one chance, and the game is not done. </p>
<p>If the user has more than zero chance left, their guess – fortune – will be compared to the random number generated – r – to check whether it is too low or too high, or equal:</p>
- If they are equal, a congratulatory message will be printed, which also shows how many times it took the user to guess correctly. In this case, the done variable becomes True to end the game.</p>
- If they are not equal, the user then makes another guess on the condition that they have not lost all chances (chance > 0) and the game is still running (not done). As always, the new guess is then evaluated again to check for its validity.</p>
<p>When the user reaches their last chance and the game still runs, meaning that the user has used up all four attempts, their last guessed number will be evaluated with the number generated, and only two options are available:</p>
- If they are equal, a congratulatory message will be printed.</p>
- If they are still not equal, a ‘Game Over’ message will be printed.</p>
<p>In both cases, the game ends and the while loop is finished.</p>

# Why a for loop is unsuitable for this guessing game
**Why a for loop is unsuitable for this guessing game**
_While_ loops | _For_ loops
------------ | -------------
Condition-controlled loop  | Count-controlled loop
They are better to use whenever the programmer needs to keep on repeating some code while a certain condition is met. | They are not necessary but simplify the code when the number of repetitions is known.

# Output
[An example of an invalid guess being ruled out and no chance is taken away](/assets/invalid-guess.png)
![An example of an invalid guess being ruled out and no chance is taken away](/assets/invalid-guess.png)

[An example of guessing correctly](/assets/correct-guess.png)</br>
![An example of guessing correctly](/assets/correct-guess.png)
