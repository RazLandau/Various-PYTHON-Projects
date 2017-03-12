def compete(num_of_piles, init_num_of_coins, s1, s2):
    ''' "Game of Coins" Simulation between 2 strategies:
    The game starts with num_of_piles piles each with init_num_of_coins coins.
    Each player takes out a certain amount of coins from one of the piles.
    The player who takes out the last coins is the looser.
    '''
    num_of_coins = [init_num_of_coins]*num_of_piles
    turn = random.randrange(2)
    while(True):
        if(all(pile == 0 for pile in num_of_coins)):
            return turn%2
        turn += 1
        if turn%2 == 0:
            s1(num_of_coins)
        else:
            s2(num_of_coins)    
    
def compare(num_of_piles, init_num_of_coins, s1, s2, num_of_games):
    ''' Returns number of wins for each strategy '''
    s1_wins = 0
    s2_wins = 0
    for game in range(num_of_games):
        result = compete(num_of_piles, init_num_of_coins, s1, s2)
        if result == 0:
            s1_wins += 1
        else:
            s2_wins += 1
    return (s1_wins, s2_wins)

def naive(num_of_coins):
    ''' Naive (random) strategy '''
    pile = -1
    while(pile < 0):
        pile = random.randrange(len(num_of_coins))
        if (num_of_coins[pile] == 0):
            pile = -1
    coins = random.randrange(1, num_of_coins[pile]+1)
    num_of_coins[pile] = num_of_coins[pile] - coins

def silly(num_of_coins):
    ''' Terrible strategy '''
    pile = -1
    while(pile < 0):
        pile = random.randrange(len(num_of_coins))
        if (num_of_coins[pile] == 0):
            pile = -1
    num_of_coins[pile] = num_of_coins[pile] - 1
    
def winning(num_of_coins):
    ''' Excellent strategy '''    
    assert sum(num_of_coins)!=0
    
    num_of_piles = len(num_of_coins)
    # get binary representations of bins heights
    binary_reps = [bin(e)[2:] for e in num_of_coins]
    # pad with zeros to achieve equal representation lengths
    maxlen = max([len(e) for e in binary_reps])
    binary_reps = ["0"*(maxlen-len(e))+e for e in binary_reps]
    # compute bitwise xor of pile heights
    xor_of_num_of_coins = "".join([str(sum([int(binary_reps[i][j]) for i in range(num_of_piles)])%2) 
                                    for j in range(maxlen)])
    
    # if bitwise XOR encodes for 0, resort to naive strategy
    if int(xor_of_num_of_coins, 2)==0:
        naive(num_of_coins)
        return
    
    # find index of most significant bit in xor_of_num_of_coins    
    mostsign = xor_of_num_of_coins.index("1")
    # find a pile whose binary representation includes "1" in this index
    pile = [i for i in range(num_of_piles) if binary_reps[i][mostsign]=="1"][0]
    # compute binary representation of the number of coins we should leave in this pile
    xor_of_coins_to_remain = [str((int(a)+int(b))%2) for a,b in zip(binary_reps[pile], xor_of_num_of_coins)]
    # convert to int, modify pile
    coins_to_remain = int("".join(xor_of_coins_to_remain), 2)
    num_of_coins[pile] = coins_to_remain

    assert all(e>=0 for e in num_of_coins), "number of coins turned negative"
