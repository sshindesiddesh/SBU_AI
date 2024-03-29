# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        score = successorGameState.getScore()

        minfooddist = -float("inf")
        listfood = newFood.asList()

        # lower the food distance - better the score
        # higher the food distance - least the score
        # inversely proportional, hence reciprocate
        for food in listfood:
            fooddist = util.manhattanDistance(food, newPos)
            if(fooddist != 0):
                score = score + (1.0/fooddist)

        # further the ghost distance, better the score
        for ghost in newGhostStates:
            ghostdist=manhattanDistance(ghost.getPosition(),newPos)
            if(ghostdist > 1):
                score = score + (1.0/ghostdist)

        return score
        #return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    #max player
    def get_max(self, gameState, agent, d):
        if (d == self.depth or gameState.isWin() or gameState.isLose()) :
             return [self.evaluationFunction(gameState), Directions.STOP]

        #initially max = -infinity
        v = -float("inf")
        a_out = Directions.STOP

        #get legal moves/actions of the max player
        action = gameState.getLegalActions(agent)
        if not action:
             return [self.evaluationFunction(gameState), Directions.STOP]

        #for every move/action of the max player, get the min move of the successive min player
        for a in action:
             if (a == "Stop"):
                continue
             suc = gameState.generateSuccessor(agent, a)
             [vl, al] = self.get_min(suc, agent + 1, d)
             #max player chooses the highest min move of the min player
             if (vl > v) :
                 v = vl
                 a_out = a
        return [v, a_out]

    # min player
	# we have multiple min players(min players = number of ghosts)
    def get_min(self, gameState, agent, d):
        if (d == self.depth or gameState.isWin() or gameState.isLose()) :
             return [self.evaluationFunction(gameState), Directions.STOP]

        # initially min = infinity
        v = float("inf")
        a_out = Directions.STOP

        #get legal moves/actions of the min player
        action = gameState.getLegalActions(agent)
        if not action:
             return [self.evaluationFunction(gameState), Directions.STOP]

		#for every  move/action of the min player, 
		#get the min move of the successive min players, or,
		#get the max move of the successive max players
        for a in action:
            if (a == "Stop"):
                continue
            suc = gameState.generateSuccessor(agent, a)
            if (agent % (gameState.getNumAgents() - 1) == 0):
                [vl, al] = self.get_max(suc, 0, d + 1)
            else :
                [vl, al] = self.get_min(suc, agent + 1, d)

			#min player chooses the lowest move of the successive player
            if (vl < v) :
                v = vl
                al_out = a
        return [v, a_out]
        
    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        [v, a] = self.get_max(gameState, 0, 0)
        return a
        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    #max player
    def get_max(self, gameState, agent, d, alpha, beta):
        if (d == self.depth or gameState.isWin() or gameState.isLose()) :
             return [self.evaluationFunction(gameState), Directions.STOP]

        #initially max = -infinity
        v = -float("inf")
        a_out = Directions.STOP

		#get legal moves/actions of the max player
        action = gameState.getLegalActions(agent)
        if not action:
             return [self.evaluationFunction(gameState), Directions.STOP]

		#for every move/action of the max player, get the min move of the successive min player
        for a in action:
             if (a == "Stop"):
                continue
             suc = gameState.generateSuccessor(agent, a)
             [vl, al] = self.get_min(suc, agent + 1, d, alpha, beta)

			 #max player chooses the highest min move of the min player
             if (vl > v) :
                 v = vl
                 a_out = a
			 #if the current highest min move is already greater than beta threshold, prune it
             if (v > beta) :
                 return [v, a_out]
			 #update alpha threshold
             alpha = max(v, alpha)
        return [v, a_out]

    #min player
    def get_min(self, gameState, agent, d, alpha, beta):
        if (d == self.depth or gameState.isWin() or gameState.isLose()) :
             return [self.evaluationFunction(gameState), Directions.STOP]

        #initially min = infinity
        v = float("inf")
        a_out = Directions.STOP

		#get legal moves/actions of the min player
        action = gameState.getLegalActions(agent)
        if not action:
             return [self.evaluationFunction(gameState), Directions.STOP]

		#for every  move/action of the min player,
		#get the min move of the successive min players, or,
		#get the max move of the successive max players
        for a in action:
            if (a == "Stop"):
                continue
            suc = gameState.generateSuccessor(agent, a)
            if (agent % (gameState.getNumAgents() - 1) == 0):
                [vl, al] = self.get_max(suc, 0, d + 1, alpha, beta)
            else :
                [vl, al] = self.get_min(suc, agent + 1, d, alpha, beta)

			#min player chooses the lowest move of the successive player
            if (vl < v) :
                v = vl
                al_out = a
			#if the current lowest move is already lesser than the alpha threshold, prune it
            if (v < alpha):
                return [v, al_out]
			#update beta threshold
            beta = min(v, beta)
        return [v, a]

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        [v, a] = self.get_max(gameState, 0, 0, -float("inf"), float("inf"))
        return a
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

	#max player
    def get_max(self, gameState, agent, d):
        if (d == self.depth or gameState.isWin() or gameState.isLose()) :
             return [self.evaluationFunction(gameState), Directions.STOP]

        #initially max = -infinity
        v = -float("inf")
        a_out = Directions.STOP

        #get legal moves/actions of the max player
        action = gameState.getLegalActions(agent)
        if not action:
             return [self.evaluationFunction(gameState), Directions.STOP]

        #for every move/action of the max player, get the min move of the successive min player
        for a in action:
             if (a == "Stop"):
                continue
             suc = gameState.generateSuccessor(agent, a)
             [vl, al] = self.get_min(suc, agent + 1, d)
             #max player chooses the highest min move of the min player
             if (vl > v) :
                 v = vl
                 a_out = a
        return [v, a_out]

    # min player
    # we have multiple min players(min players = number of ghosts)
    def get_min(self, gameState, agent, d):
        if (d == self.depth or gameState.isWin() or gameState.isLose()) :
             return [self.evaluationFunction(gameState), Directions.STOP]

        # initially min = infinity
        v = float("inf")
        a_out = Directions.STOP

        #get legal moves/actions of the min player
        action = gameState.getLegalActions(agent)
        if not action:
             return [self.evaluationFunction(gameState), Directions.STOP]

        #for every  move/action of the min player, 
        #get the min move of the successive min players, or,
        #get the max move of the successive max players
        t = 0.0
        for a in action:
            if (a == "Stop"):
                continue
            suc = gameState.generateSuccessor(agent, a)
            if (agent % (gameState.getNumAgents() - 1) == 0):
                [vl, al] = self.get_max(suc, 0, d + 1)
            else :
                [vl, al] = self.get_min(suc, agent + 1, d)
            #chance nodes take the average(expectation) of the minimax values 
            t = t + (vl * 1.0)
        avg = t/len(action)
        return [avg, a_out]


    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        [v, a] = self.get_max(gameState, 0, 0)
        return a
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

