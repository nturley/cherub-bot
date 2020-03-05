import py_trees
import sc2
from sc2.constants import UnitTypeId
import cherub_bot
from cherub_bot.trees.sync import sync
from cherub_bot import lookups, bot
from cherub_bot.lookups import job_lookup, name_lookup
class Build(py_trees.behaviour.Behaviour):
    def __init__(self, name, bot: sc2.BotAI, properties: dict):
        super(Build, self).__init__(name)
        self.bot = bot
        self.unitType = getattr(UnitTypeId, properties['Type'])
    
    def build_refinery(self):
        ccs: Units = self.bot.townhalls
        for cc in ccs:
            vgs = self.bot.vespene_geyser.closer_than(20, cc)
            for vg in vgs:
                if self.bot.gas_buildings.filter(lambda unit: unit.distance_to(vg) < 1):
                    break
                builder = self.bot.select_build_worker(vg)
                return sync(self.bot.build(self.unitType, vg)), builder
    
    def update(self):
        ccs: Units = self.bot.townhalls
        if not ccs:
            return py_trees.common.Status.FAILURE
        if self.unitType == UnitTypeId.REFINERY:
            result, builder = self.build_refinery()
        else:
            cc: Unit = ccs.random
            builder = self.bot.select_build_worker(cc.position.towards(self.bot.game_info.map_center, 8))
            result = sync(self.bot.build(self.unitType, near=cc.position.towards(self.bot.game_info.map_center, 8), build_worker=builder))
        if result:
            lookups.job_lookup[builder.tag] = bot.Job.Build
            print(name_lookup[builder.tag], 'build', self.unitType.name)
        return py_trees.common.Status.SUCCESS if result else py_trees.common.Status.FAILURE
