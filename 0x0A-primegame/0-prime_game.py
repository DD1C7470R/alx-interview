#!/usr/bin/python3
'''Define game'''


def is_prime(n: int) -> bool:
    '''Define a prime number'''
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        sroot_of_n = n
        i = 3
        for i in range(sroot_of_n * sroot_of_n, n + 1, sroot_of_n):
            if n % i == 0:
                return False
        return True


def isWinner(x, nums):
    '''Difine winner'''
    pickers = {
            "Ben": 0,
            "Maria": 0
    }
    winner = None
    nround = 0
    while x > nround:
        next_picker = 'Ben'
        current_num = nums[nround]
        game_board = [i for i in range(1, current_num + 1)]
        idx = len(game_board)
        picks = 1
        if len(game_board) == 0:
            pickers[next_picker] += 1
        while idx >= picks:
            all_primes = [num for num in game_board if is_prime(num)]
            if len(all_primes) == 0:
                pickers[next_picker] += 1
                break
            current_prime = all_primes[0]
            ans = list(filter(lambda x: x % current_prime != 0, game_board))
            game_board = ans
            if picks % 2 == 0:
                next_picker = 'Ben'
            else:
                next_picker = 'Maria'
            picks += 1
        nround += 1

    for key, val in pickers.items():
        if list(pickers.values())[0] == list(pickers.values())[1]:
            return None
        if val == max(list(pickers.values())):
            winner = key
            return key
