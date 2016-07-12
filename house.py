from random import randint

import numpy as np

# http://mnemstudio.org/path-finding-q-learning-tutorial.htm

R = np.array([
              # Action
    #       0   1   2   3   4   5
       [ -1, -1, -1, -1,  0, -1],  # 0
       [ -1, -1, -1,  0, -1,100],  # 1
       [ -1, -1, -1,  0, -1, -1],  # 2
       [ -1,  0,  0, -1,  0, -1],  # 3
       [  0, -1, -1,  0, -1,100],  # 4
       [ -1,  0, -1, -1,  0,100]]) # 5

#state


# Termination state

T = [
        [1,5],
        [4,5],
        [5,5]
    ]



# initialized

Q = np.zeros(R.shape) # Q-Value
r = 1 # discount value
episode = 1000
actions = None



for e in range(episode):

    print 'Episode {} started'.format(e)

    # randomly initialized state at the start of episode
    s = randint(0,len(R) - 1)

    # set terminate to False
    terminate = False

    while not terminate:

        print 'Current state : {}'.format(s)
        # take action a , observe R, s'

        # get available action
        actions = [idx for idx, reward in enumerate(R[s]) if reward != -1]

        # randomly choose a action

        a = actions[randint(0,len(actions) - 1)]
        print 'Available action : {}'.format(actions)
        #print 'index : {}'.format(randint(0,len(actions) - 1))
        print 'Action taken : {}'.format(a)

        # check if current state - action pair is in Termination state

        Q[s,a] = R[s,a] + r * np.max([Q[_a] for _a in actions])
        print 'maxing Q : {}'.format([Q[_a] for _a in actions])
        print 'R[s,a] : {}'.format(R[s,a])
        print 'Q-Value : {}'.format(Q[s,a])

        if R[s,a] == 100:
            terminate = True
            continue

        print 'Update : {}  ==>  {}'.format(s, a)

        s = a # set current state to action

        print Q




    print 'Episode {} '.format(e)

    print Q
