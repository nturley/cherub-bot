import py_trees
import sc2
from sc2.ids.ability_id import AbilityId
from py_trees.common import Status
from cherub_bot.trees.sync import sync
import cherub_bot.bot
import cherub_bot.lookups
from cherub_bot import bot
from cherub_bot.lookups import job_lookup, name_lookup
import names

class InitJobs(py_trees.behaviour.Behaviour):
    def __init__(self, name, bot: sc2.BotAI, properties: dict):
        super(InitJobs, self).__init__(name)
        self.bot = bot
    
    def is_really_idle(self, worker):
        return (worker not in self.bot.unit_tags_received_action
            and not worker.orders
            or len(worker.orders) == 1
            and worker.orders[0].ability.id in {AbilityId.MOVE, AbilityId.HARVEST_GATHER})
    
    def update(self):
        for unit in self.bot.units.not_structure:
            if unit.tag not in name_lookup:
                name_lookup[unit.tag] = names.get_first_name(gender='male')
            if unit.tag not in job_lookup:
                if unit.name == 'SCV':
                    job_lookup[unit.tag] = bot.Job.Minerals
                    print(name_lookup[unit.tag], 'minerals')
                else:
                    job_lookup[unit.tag] = bot.Job.Idle
            if self.is_really_idle(unit):
                if job_lookup[unit.tag] == bot.Job.Build:
                    print('looks like ', name_lookup[unit.tag], 'finished')
                    job_lookup[unit.tag] = bot.Job.Minerals
                    print(name_lookup[unit.tag], 'minerals')
        return Status.SUCCESS