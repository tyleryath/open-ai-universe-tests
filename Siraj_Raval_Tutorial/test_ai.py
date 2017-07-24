#This is following Siraj Raval's tutorial on OpenAI's Universe
#https://www.youtube.com/watch?v=XI-I9i_GzIw&t=1975s

#Bot will deteremine a two things
#Step 1 Should I turn?
#Step 2 Where do I turn?

import gym
import universe
import random

#Reinforcement learning step
def determine_turn(turn, observation_n, j, total_sum, prev_total_sum, reward_n):
    #for every 15 iterations, sum the total observations, then take the average
    #if lower than 0, change the direction
    #if we go 15+ iterations and get a reward each step, we're doing something correctly
    #then we will turn
    if(j >= 15):
        if(total_sum/j) == 0:
            turn = True
        else:
            turn = False
        #reset vars
        j = 0
        prev_total_sum = total_sum
        total_sum = 0
    else:
        turn = False

    if(observation_n != None):
        #incremenet counter and reward sum
        j += 1
        total_sum += reward_n

    return(turn, j, total_sum, prev_total_sum)

def main():
    #init environment, define environemnt to be CoasterRacer
    env = gym.make('flashgames.CoasterRacer-v0')
    env.configure(remotes = 1)
    observation_n = env.reset()
    #init variables
    #num of game iterations
    n = 0
    j = 0
    #sum of observations
    total_sum = 0
    prev_total_sum = 0
    turn = False

    #define turns, keyboard actions
    left = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', True), ('KeyEvent', 'ArrowRight', False)]
    right = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'ArrowRight', True)]
    forward = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'ArrowRight', False)]

    #main logic
    while True:
        #increment a counter for number of iterations
        n += 1
        #if at least one iteration is made, check if turn is needed
        if(n > 1):
            #if at least one iteration, check if turn is needed
            if(observation_n[0] != None):
                #store the reward in the previous score
                prev_score = reward_n[0]
                #should we tun?
                if(turn):
                    #pick a random event
                    #where we turn
                    event = random.choice([left, right])
                    #perform an action
                    action_n = [event for ob in observation_n]
                    #set turn to false
                    turn = False

        elif(~turn):
            #if no turn is needed, go straight
            action_n = [forward for ob in observation_n]

        #if there is an observation, the game has started, check if we need a turn
        if(observation_n[0] != None):
            turn, j, total_sum, prev_total_sum = determine_turn(turn, observation_n[0], j, total_sum, prev_total_sum, reward_n[0])

        #save new variables for each iteration
        observation_n, reward_n, done_n, info = env.step(action_n)

        env.render()

if __name__ == '__main__':
    main()
