import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import *

if __name__ == '__main__':
    episode = input("Which episode should be used for the network? ")

    agent = Agent("PongDeterministic-v4")

    if episode == "final":
        agent.load_agent("pong_agent_episode_380.pth")
    elif episode == "first":
        agent.load_agent("pong_agent_episode_0.pth")
    else:
        exit(0)

    agent.play(1)
    agent.env.close()
