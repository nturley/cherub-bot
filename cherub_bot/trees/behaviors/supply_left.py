import py_trees
import sc2
from py_trees.common import Status

class SupplyLeft(py_trees.behaviour.Behaviour):
    def __init__(self, name, bot: sc2.BotAI, properties: dict):
        super(SupplyLeft, self).__init__(name)
        self.bot = bot
        self.bb = properties['Blackboard']
    
    def update(self):
        self.bot.blackboard[self.bb] = self.bot.supply_left
        return Status.SUCCESS