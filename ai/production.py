working_memory = {'light': 'off', 'switch': 'up'}

rules = [
    {'condition': lambda wm: wm['light'] == 'off' and wm['switch'] == 'up',
     'action': lambda wm: wm.update({'light': 'on', 'switch': 'down'})},
]

# Simple rule engine
def apply_rules(wm, rules):
    for rule in rules:
        if rule['condition'](wm):
            rule['action'](wm)
            print("Rule applied!")
            return True
    return False

# Run the production system
while apply_rules(working_memory, rules):
    pass

print("Final state:", working_memory)
