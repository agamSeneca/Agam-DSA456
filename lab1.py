def wins_rock_scissors_paper(player_throw, opponent_throw):
    player_throw = player_throw.lower()
    opponent_throw = opponent_throw.lower()

    if player_throw == opponent_throw:
        return False

    if player_throw == 'rock' and opponent_throw == 'scissors':
        return True
    elif player_throw == 'paper' and opponent_throw == 'rock':
        return True
    elif player_throw == 'scissors' and opponent_throw == 'paper':
        return True
    else:
        return False


def factorial(n):
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


def fibonacci(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(2, n + 1):
        next_num = previous + current
        previous = current
        current = next_num

    return current


def sum_to_goal(numbers, goal):
    seen = set()

    for num in numbers:
        complement = goal - num
        if complement in seen:
            return num * complement
        seen.add(num)

    return 0


class UpCounter:
    def __init__(self, stepsize=1):
        self.count_value = 0
        self.stepsize = stepsize

    def count(self):
        return self.count_value

    def update(self):
        self.count_value += self.stepsize


class DownCounter(UpCounter):
    def update(self):
        self.count_value -= self.stepsize


print(wins_rock_scissors_paper('rock', 'scissors'))  

print(factorial(5)) 

print(fibonacci(7))  

numbers = [1, 2, 3, 4, 5]
goal = 9
print(sum_to_goal(numbers, goal))  

up_counter = UpCounter(2)
print(up_counter.count())  
up_counter.update()
print(up_counter.count()) 
up_counter.update()
print(up_counter.count()) 

down_counter = DownCounter(3)
print(down_counter.count())  
down_counter.update()
print(down_counter.count()) 
down_counter.update()
print(down_counter.count())  
