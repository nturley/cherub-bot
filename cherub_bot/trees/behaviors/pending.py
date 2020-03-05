import sc2
from sc2.constants import UnitTypeId
import py_trees
from py_trees.common import Status

class Pending(py_trees.behaviour.Behaviour):
    def __init__(self, name: str, bot: sc2.BotAI, properties: dict):
        super(Pending, self).__init__(name)
        self.bot = bot
        self.unit_type = getattr(UnitTypeId, properties['Type'])
        self.bb = properties['Blackboard']
    
    def update(self):
        self.bot.blackboard[self.bb] = self.bot.already_pending(self.unit_type)
        return Status.SUCCESS