import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.unit import Unit
from sc2.player import Bot, Computer
import cherub_bot
from cherub_bot.trees.tree import build_tree
from cherub_bot.lookups import job_lookup, name_lookup
import py_trees
from enum import Enum
import traceback
import sys

class Job(Enum):
    Minerals = 0
    Gas = 1
    Idle = 2
    Build = 3

class WorkerRushBot(sc2.BotAI):
    async def on_start(self):
        self.blackboard = {}
        self.tree = build_tree('tree.json', self)
        for worker in self.workers:
            job_lookup[worker.tag] = Job.Minerals
            

    async def on_step(self, iteration: int):
        try:
            tree_debug = py_trees.display.ascii_tree(self.tree.root, show_status=True)
            self.client.debug_text_simple(tree_debug)
            for unit in self.workers:
                unit_name = str(name_lookup.get(unit.tag,'Anon'))
                job_label = str(job_lookup.get(unit.tag,'None'))
                self.client.debug_text_world(unit_name, unit.position3d)
            self.tree.tick()
        except Exception as e:
            traceback.print_exc(file=sys.stdout)
            
def main():
    run_game(maps.get("AcropolisLE"), [
        Bot(Race.Terran, WorkerRushBot()),
        Computer(Race.Protoss, Difficulty.Medium)
    ], realtime=True)

