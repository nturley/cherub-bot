import sc2
import py_trees

from cherub_bot.trees.behaviors.train import Train
from cherub_bot.trees.behaviors.build import Build
from cherub_bot.trees.behaviors.supply_left import SupplyLeft
from cherub_bot.trees.behaviors.supply_used import SupplyUsed
from cherub_bot.trees.behaviors.pending import Pending
from cherub_bot.trees.behaviors.compare import Compare
from cherub_bot.trees.behaviors.init_jobs import InitJobs
from cherub_bot.trees.behaviors.manage_miners import ManageMiners
from cherub_bot.trees.decorators import generate_decorator
import json
import os

dirname = os.path.dirname(__file__)

def build_tree(tree_name, bot):
    tree_path = os.path.join(dirname, 'tree_json', tree_name)
    with open(tree_path) as f:
        tree_data = json.load(f)
    return py_trees.trees.BehaviourTree(root=generate_tree(tree_data, bot))

# wrap builtin Nodes so that the constructors all match
def Selector(name, bot: sc2.BotAI, properties: dict):
    return py_trees.composites.Selector()

def Sequence(name, bot: sc2.BotAI, properties: dict):
    return py_trees.composites.Sequence()

def Parallel(name, bot, properties):
    return py_trees.composites.Parallel()

all_nodes = {
    'Train':Train,
    'Build':Build,
    'Selector':Selector,
    'Sequence':Sequence,
    'Supply Left':SupplyLeft,
    'Supply Used': SupplyUsed,
    'Pending': Pending,
    'Compare': Compare,
    'Parallel': Parallel,
    'Init Jobs': InitJobs,
    'Manage Miners': ManageMiners
}

def generate_tree(tree_data: dict, bot: sc2.BotAI):
    node = None
    properties = {}
    for prop in tree_data.get('properties', []):
        properties[prop['name']] = prop['value']
    if tree_data['type'] in all_nodes:
        node = all_nodes[tree_data['type']](tree_data['type'], bot, properties)
    else:
        print(tree_data['type'], 'not found')
    if node:
        for child_data in tree_data.get('childNodes',[]):
            child = generate_tree(child_data, bot)
            if child:
                for decorator in child_data.get('decorators', [])[::-1]:
                    dec = generate_decorator(decorator, bot, child)
                    if dec:
                        child = dec
                node.add_child(child)
    return node
