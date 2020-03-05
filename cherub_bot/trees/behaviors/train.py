import py_trees
import sc2
from sc2.constants import UnitTypeId
from py_trees.common import Status

class Train(py_trees.behaviour.Behaviour):
    def __init__(self, name, bot: sc2.BotAI, properties: dict):
        super(Train, self).__init__(name)
        self.bot = bot
        self.unitType = getattr(UnitTypeId, properties['Type'])
    
    def update(self):
        result = self.bot.train(self.unitType)
        return Status.SUCCESS if result == 1 else Status.FAILURE

