import sc2
from sc2.constants import UnitTypeId
import py_trees
from py_trees.common import Status
import cherub_bot
from cherub_bot.lookups import job_lookup, name_lookup
from cherub_bot import bot
from sc2.ids.ability_id import AbilityId
class ManageMiners(py_trees.behaviour.Behaviour):
    def __init__(self, name: str, bot: sc2.BotAI, properties: dict):
        super(ManageMiners, self).__init__(name)
        self.bot = bot
    
    def go_mine(self, miner):
        cc = self.bot.townhalls.closest_to(miner)
        mineral = self.bot.mineral_field.closest_to(cc)
        result = self.bot.do(miner.gather(mineral, True))

    def update(self):
        miners = filter(lambda worker: job_lookup[worker.tag]==bot.Job.Minerals, self.bot.workers)
        for miner in miners:
            if not miner.is_collecting:
                print(name_lookup[miner.tag], 'is not collecting. Go get minerals')
                self.go_mine(miner)
            if miner.is_carrying_vespene and miner.is_returning:
                print(name_lookup[miner.tag], 'is collecting gas. Go get minerals')
                self.go_mine(miner)
        return Status.SUCCESS