import py_trees
import sc2
from py_trees.common import Status

class Compare(py_trees.behaviour.Behaviour):
    def __init__(self, name, bot: sc2.BotAI, properties: dict):
        super(Compare, self).__init__(name)
        self.bot = bot
        self.bb = properties['Blackboard']
        self.amount = properties['Constant']
        self.comparator = properties['Comparator']
    
    def update(self):
        value = self.bot.blackboard[self.bb]
        if self.comparator == '>' and value > self.amount:
            return Status.SUCCESS
        if self.comparator == '<' and value < self.amount:
            return Status.SUCCESS
        return Status.FAILURE