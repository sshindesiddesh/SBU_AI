# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
	"""
	Search the deepest nodes in the search tree first.

	Your search algorithm needs to return a list of actions that reaches the
	goal. Make sure to implement a graph search algorithm.

	To get started, you might want to try some of these simple commands to
	understand the search problem that is being passed in:

	print "Start:", problem.getStartState()
	print "Is the start a goal?", problem.isGoalState(problem.getStartState())
	print "Start's successors:", problem.getSuccessors(problem.getStartState())
	"""
	"*** YOUR CODE HERE ***"

	# Use Stack for the frontier
	from util import Stack
	st = Stack()

	# Maintain a list of already visited states
	visited = []

	# Get the start state
	state  = problem.getStartState()
	# Put it in visited array
	visited.append(state)
	# Get the list of successor states
	suc = problem.getSuccessors(state)

	# For every state in successors,
	# push to frontier if not visited
	for s in suc:
		if s[0] not in visited:
			l = list(s)
			l[1] = l[1].split()
			st.push(l)

	while (1) :

		# finish when the frontier is empty
		if st.isEmpty() :
			break;

		# visit state
		p = st.pop()
		visited.append(p[0])

		# end on reaching goal state
		if (problem.isGoalState(p[0])) :
			return p[1]
			break;

		# Get the list of successor states
		suc = problem.getSuccessors(p[0])

		#For every state in successors,
		# push to frontier if not visited or if not in frontier
		for s in suc:
			if s[0] not in visited : # if state is not visited yet
				if (s[0] not in [item for item in st.list if item[0] == s[0]]) : # if state is not in stack
					c = list(s)
					c[1] = c[1].split()
					c[1] = p[1] + c[1] # update actions for every state right from the start state 
					st.push(c)

	util.raiseNotDefined()

def breadthFirstSearch(problem):
	"""Search the shallowest nodes in the search tree first."""
	"*** YOUR CODE HERE ***"

	# Use Queue for the frontier
	from util import Queue
	qu = Queue()

	# Maintain a list of already visited states
	visited = []

	# Get the start state
	state  = problem.getStartState()
	# Put it in visited array
	visited.append(state)
	# Get the list of successor states
	suc = problem.getSuccessors(state)

	# For every state in successors,
	# push to frontier if not visited
	for s in suc:
		if s[0] not in visited:
			l = list(s)
			l[1] = l[1].split()
			qu.push(l)

	while (1) :

		# finish when the frontier is empty
		if qu.isEmpty() :
			break;

		# visit state
		p = qu.pop()
		visited.append(p[0])

		# end on reaching goal state
		if (problem.isGoalState(p[0])) :
			return p[1]
			break;

		# Get the list of successor states
		suc = problem.getSuccessors(p[0])

		#For every state in successors,
		# push to frontier if not visited or if not in frontier
		for s in suc:
			if s[0] not in visited : # if state is not visited yet
				if (s[0] not in [item for item in qu.list if item[0] == s[0]]) : # if state is not in stack
					c = list(s)
					c[1] = c[1].split()
					c[1] = p[1] + c[1] # update actions for every state right from the start state 
					qu.push(c)
	util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
