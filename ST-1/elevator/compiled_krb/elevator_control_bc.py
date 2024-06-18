# elevator_control_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1
from compiled_krb import elevator_control_plans

def open_to_enter_action(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('floors', 'floor', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "elevator_control.open_to_enter_action: got unexpected plan from when clause 1"
            with engine.prove('floors', 'floor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "elevator_control.open_to_enter_action: got unexpected plan from when clause 2"
                if context.lookup_data('Door') == 0:
                  if context.lookup_data('CurrentFloor') == context.lookup_data('WhereWaiting')            :
                    if context.lookup_data('PassengersInside') == 0:
                      if context.lookup_data('PassengersWaiting') == 1:
                        rule.rule_base.num_bc_rule_successes += 1
                        yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def open_to_leave_action(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('floors', 'floor', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "elevator_control.open_to_leave_action: got unexpected plan from when clause 1"
            with engine.prove('floors', 'floor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "elevator_control.open_to_leave_action: got unexpected plan from when clause 2"
                if context.lookup_data('Door') == 0:
                  if context.lookup_data('CurrentFloor') == context.lookup_data('WhereTo')            :
                    if context.lookup_data('PassengersInside') == 1:
                      rule.rule_base.num_bc_rule_successes += 1
                      yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def wait_to_enter_action(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('floors', 'floor', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "elevator_control.wait_to_enter_action: got unexpected plan from when clause 1"
            with engine.prove('floors', 'floor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "elevator_control.wait_to_enter_action: got unexpected plan from when clause 2"
                if context.lookup_data('Door') == 1:
                  if context.lookup_data('CurrentFloor') == context.lookup_data('WhereWaiting')            :
                    if context.lookup_data('PassengersInside') == 0:
                      if context.lookup_data('PassengersWaiting') == 1:
                        rule.rule_base.num_bc_rule_successes += 1
                        yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def wait_to_leave_action(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('floors', 'floor', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "elevator_control.wait_to_leave_action: got unexpected plan from when clause 1"
            with engine.prove('floors', 'floor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "elevator_control.wait_to_leave_action: got unexpected plan from when clause 2"
                if context.lookup_data('Door') == 1:
                  if context.lookup_data('CurrentFloor') == context.lookup_data('WhereTo')            :
                    if context.lookup_data('PassengersInside') == 1:
                      rule.rule_base.num_bc_rule_successes += 1
                      yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def wait_nobody_action(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('floors', 'floor', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "elevator_control.wait_nobody_action: got unexpected plan from when clause 1"
            with engine.prove('floors', 'floor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "elevator_control.wait_nobody_action: got unexpected plan from when clause 2"
                if context.lookup_data('Door') == 0           :
                  if context.lookup_data('PassengersInside') == 0:
                    if context.lookup_data('PassengersWaiting') == 0:
                      rule.rule_base.num_bc_rule_successes += 1
                      yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def up_waiting_action(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('floors', 'floor', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "elevator_control.up_waiting_action: got unexpected plan from when clause 1"
            with engine.prove('floors', 'floor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "elevator_control.up_waiting_action: got unexpected plan from when clause 2"
                if context.lookup_data('Door') == 0:
                  if context.lookup_data('PassengersInside') == 0:
                    if context.lookup_data('PassengersWaiting') == 1:
                      if context.lookup_data('WhereWaiting') > context.lookup_data('CurrentFloor'):
                        rule.rule_base.num_bc_rule_successes += 1
                        yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def up_action(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('floors', 'floor', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "elevator_control.up_action: got unexpected plan from when clause 1"
            with engine.prove('floors', 'floor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "elevator_control.up_action: got unexpected plan from when clause 2"
                if context.lookup_data('Door') == 0:
                  if context.lookup_data('PassengersInside') == 1:
                    if context.lookup_data('WhereTo') > context.lookup_data('CurrentFloor'):
                      rule.rule_base.num_bc_rule_successes += 1
                      yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def down_waiting_action(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('floors', 'floor', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "elevator_control.down_waiting_action: got unexpected plan from when clause 1"
            with engine.prove('floors', 'floor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "elevator_control.down_waiting_action: got unexpected plan from when clause 2"
                if context.lookup_data('Door') == 0:
                  if context.lookup_data('PassengersInside') == 0:
                    if context.lookup_data('PassengersWaiting') == 1:
                      if context.lookup_data('WhereWaiting') < context.lookup_data('CurrentFloor'):
                        rule.rule_base.num_bc_rule_successes += 1
                        yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def down_action(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('floors', 'floor', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "elevator_control.down_action: got unexpected plan from when clause 1"
            with engine.prove('floors', 'floor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "elevator_control.down_action: got unexpected plan from when clause 2"
                if context.lookup_data('Door') == 0:
                  if context.lookup_data('PassengersInside') == 1:
                    if context.lookup_data('WhereTo') < context.lookup_data('CurrentFloor'):
                      rule.rule_base.num_bc_rule_successes += 1
                      yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def close_to_destiny_action(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('floors', 'floor', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "elevator_control.close_to_destiny_action: got unexpected plan from when clause 1"
            with engine.prove('floors', 'floor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "elevator_control.close_to_destiny_action: got unexpected plan from when clause 2"
                if context.lookup_data('Door') == 1:
                  if context.lookup_data('PassengersInside') == 1:
                    if context.lookup_data('WhereTo') != context.lookup_data('CurrentFloor'):
                      rule.rule_base.num_bc_rule_successes += 1
                      yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def close_action(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('floors', 'floor', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "elevator_control.close_action: got unexpected plan from when clause 1"
            with engine.prove('floors', 'floor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "elevator_control.close_action: got unexpected plan from when clause 2"
                if context.lookup_data('Door') == 1:
                  if context.lookup_data('PassengersInside') == 0:
                    if context.lookup_data('PassengersWaiting') == 1:
                      if context.lookup_data('WhereTo') != context.lookup_data('CurrentFloor'):
                        rule.rule_base.num_bc_rule_successes += 1
                        yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def close_nobody_action(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('floors', 'floor', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "elevator_control.close_nobody_action: got unexpected plan from when clause 1"
            with engine.prove('floors', 'floor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "elevator_control.close_nobody_action: got unexpected plan from when clause 2"
                if context.lookup_data('Door') == 1:
                  if context.lookup_data('PassengersInside') == 0:
                    if context.lookup_data('PassengersWaiting') == 0:
                      rule.rule_base.num_bc_rule_successes += 1
                      yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('elevator_control')
  
  bc_rule.bc_rule('open_to_enter_action', This_rule_base, 'actions',
                  open_to_enter_action, elevator_control_plans.open_to_enter_action,
                  (contexts.variable('CurrentFloor'),
                   contexts.variable('PassengersInside'),
                   contexts.variable('PassengersWaiting'),
                   contexts.variable('WhereTo'),
                   contexts.variable('WhereWaiting'),
                   contexts.variable('Door'),
                   pattern.pattern_literal('open'),),
                  (),
                  (contexts.variable('CurrentFloor'),
                   contexts.variable('WhereWaiting'),))
  
  bc_rule.bc_rule('open_to_leave_action', This_rule_base, 'actions',
                  open_to_leave_action, elevator_control_plans.open_to_leave_action,
                  (contexts.variable('CurrentFloor'),
                   contexts.variable('PassengersInside'),
                   contexts.variable('PassengersWaiting'),
                   contexts.variable('WhereTo'),
                   contexts.variable('WhereWaiting'),
                   contexts.variable('Door'),
                   pattern.pattern_literal('open'),),
                  (),
                  (contexts.variable('CurrentFloor'),
                   contexts.variable('WhereTo'),))
  
  bc_rule.bc_rule('wait_to_enter_action', This_rule_base, 'actions',
                  wait_to_enter_action, elevator_control_plans.wait_to_enter_action,
                  (contexts.variable('CurrentFloor'),
                   contexts.variable('PassengersInside'),
                   contexts.variable('PassengersWaiting'),
                   contexts.variable('WhereTo'),
                   contexts.variable('WhereWaiting'),
                   contexts.variable('Door'),
                   pattern.pattern_literal('wait'),),
                  (),
                  (contexts.variable('CurrentFloor'),
                   contexts.variable('WhereWaiting'),))
  
  bc_rule.bc_rule('wait_to_leave_action', This_rule_base, 'actions',
                  wait_to_leave_action, elevator_control_plans.wait_to_leave_action,
                  (contexts.variable('CurrentFloor'),
                   contexts.variable('PassengersInside'),
                   contexts.variable('PassengersWaiting'),
                   contexts.variable('WhereTo'),
                   contexts.variable('WhereWaiting'),
                   contexts.variable('Door'),
                   pattern.pattern_literal('wait'),),
                  (),
                  (contexts.variable('CurrentFloor'),
                   contexts.variable('WhereTo'),))
  
  bc_rule.bc_rule('wait_nobody_action', This_rule_base, 'actions',
                  wait_nobody_action, elevator_control_plans.wait_nobody_action,
                  (contexts.variable('CurrentFloor'),
                   contexts.variable('PassengersInside'),
                   contexts.variable('PassengersWaiting'),
                   contexts.variable('WhereTo'),
                   contexts.variable('WhereWaiting'),
                   contexts.variable('Door'),
                   pattern.pattern_literal('wait'),),
                  (),
                  (contexts.variable('CurrentFloor'),
                   contexts.variable('WhereTo'),))
  
  bc_rule.bc_rule('up_waiting_action', This_rule_base, 'actions',
                  up_waiting_action, elevator_control_plans.up_waiting_action,
                  (contexts.variable('CurrentFloor'),
                   contexts.variable('PassengersInside'),
                   contexts.variable('PassengersWaiting'),
                   contexts.variable('WhereTo'),
                   contexts.variable('WhereWaiting'),
                   contexts.variable('Door'),
                   pattern.pattern_literal('up'),),
                  (),
                  (contexts.variable('CurrentFloor'),
                   contexts.variable('WhereWaiting'),))
  
  bc_rule.bc_rule('up_action', This_rule_base, 'actions',
                  up_action, elevator_control_plans.up_action,
                  (contexts.variable('CurrentFloor'),
                   contexts.variable('PassengersInside'),
                   contexts.variable('PassengersWaiting'),
                   contexts.variable('WhereTo'),
                   contexts.variable('WhereWaiting'),
                   contexts.variable('Door'),
                   pattern.pattern_literal('up'),),
                  (),
                  (contexts.variable('CurrentFloor'),
                   contexts.variable('WhereTo'),))
  
  bc_rule.bc_rule('down_waiting_action', This_rule_base, 'actions',
                  down_waiting_action, elevator_control_plans.down_waiting_action,
                  (contexts.variable('CurrentFloor'),
                   contexts.variable('PassengersInside'),
                   contexts.variable('PassengersWaiting'),
                   contexts.variable('WhereTo'),
                   contexts.variable('WhereWaiting'),
                   contexts.variable('Door'),
                   pattern.pattern_literal('down'),),
                  (),
                  (contexts.variable('CurrentFloor'),
                   contexts.variable('WhereWaiting'),))
  
  bc_rule.bc_rule('down_action', This_rule_base, 'actions',
                  down_action, elevator_control_plans.down_action,
                  (contexts.variable('CurrentFloor'),
                   contexts.variable('PassengersInside'),
                   contexts.variable('PassengersWaiting'),
                   contexts.variable('WhereTo'),
                   contexts.variable('WhereWaiting'),
                   contexts.variable('Door'),
                   pattern.pattern_literal('down'),),
                  (),
                  (contexts.variable('CurrentFloor'),
                   contexts.variable('WhereTo'),))
  
  bc_rule.bc_rule('close_to_destiny_action', This_rule_base, 'actions',
                  close_to_destiny_action, elevator_control_plans.close_to_destiny_action,
                  (contexts.variable('CurrentFloor'),
                   contexts.variable('PassengersInside'),
                   contexts.variable('PassengersWaiting'),
                   contexts.variable('WhereTo'),
                   contexts.variable('WhereWaiting'),
                   contexts.variable('Door'),
                   pattern.pattern_literal('close'),),
                  (),
                  (contexts.variable('CurrentFloor'),
                   contexts.variable('WhereTo'),))
  
  bc_rule.bc_rule('close_action', This_rule_base, 'actions',
                  close_action, elevator_control_plans.close_action,
                  (contexts.variable('CurrentFloor'),
                   contexts.variable('PassengersInside'),
                   contexts.variable('PassengersWaiting'),
                   contexts.variable('WhereTo'),
                   contexts.variable('WhereWaiting'),
                   contexts.variable('Door'),
                   pattern.pattern_literal('close'),),
                  (),
                  (contexts.variable('CurrentFloor'),
                   contexts.variable('WhereTo'),))
  
  bc_rule.bc_rule('close_nobody_action', This_rule_base, 'actions',
                  close_nobody_action, elevator_control_plans.close_nobody_action,
                  (contexts.variable('CurrentFloor'),
                   contexts.variable('PassengersInside'),
                   contexts.variable('PassengersWaiting'),
                   contexts.variable('WhereTo'),
                   contexts.variable('WhereWaiting'),
                   contexts.variable('Door'),
                   pattern.pattern_literal('close'),),
                  (),
                  (contexts.variable('CurrentFloor'),
                   contexts.variable('WhereTo'),))


Krb_filename = '../elevator_control.krb'
Krb_lineno_map = (
    ((15, 19), (5, 5)),
    ((21, 26), (7, 7)),
    ((27, 32), (8, 8)),
    ((33, 33), (9, 9)),
    ((34, 34), (10, 10)),
    ((35, 35), (11, 11)),
    ((36, 36), (12, 12)),
    ((49, 53), (18, 18)),
    ((55, 60), (20, 20)),
    ((61, 66), (21, 21)),
    ((67, 67), (22, 22)),
    ((68, 68), (23, 23)),
    ((69, 69), (24, 24)),
    ((82, 86), (30, 30)),
    ((88, 93), (32, 32)),
    ((94, 99), (33, 33)),
    ((100, 100), (34, 34)),
    ((101, 101), (35, 35)),
    ((102, 102), (36, 36)),
    ((103, 103), (37, 37)),
    ((116, 120), (43, 43)),
    ((122, 127), (45, 45)),
    ((128, 133), (46, 46)),
    ((134, 134), (47, 47)),
    ((135, 135), (48, 48)),
    ((136, 136), (49, 49)),
    ((149, 153), (55, 55)),
    ((155, 160), (57, 57)),
    ((161, 166), (58, 58)),
    ((167, 167), (59, 59)),
    ((168, 168), (60, 60)),
    ((169, 169), (61, 61)),
    ((182, 186), (68, 68)),
    ((188, 193), (70, 70)),
    ((194, 199), (71, 71)),
    ((200, 200), (72, 72)),
    ((201, 201), (73, 73)),
    ((202, 202), (74, 74)),
    ((203, 203), (75, 75)),
    ((216, 220), (81, 81)),
    ((222, 227), (83, 83)),
    ((228, 233), (84, 84)),
    ((234, 234), (85, 85)),
    ((235, 235), (86, 86)),
    ((236, 236), (87, 87)),
    ((249, 253), (93, 93)),
    ((255, 260), (95, 95)),
    ((261, 266), (96, 96)),
    ((267, 267), (97, 97)),
    ((268, 268), (98, 98)),
    ((269, 269), (99, 99)),
    ((270, 270), (100, 100)),
    ((283, 287), (106, 106)),
    ((289, 294), (108, 108)),
    ((295, 300), (109, 109)),
    ((301, 301), (110, 110)),
    ((302, 302), (111, 111)),
    ((303, 303), (112, 112)),
    ((316, 320), (118, 118)),
    ((322, 327), (120, 120)),
    ((328, 333), (121, 121)),
    ((334, 334), (122, 122)),
    ((335, 335), (123, 123)),
    ((336, 336), (124, 124)),
    ((349, 353), (130, 130)),
    ((355, 360), (132, 132)),
    ((361, 366), (133, 133)),
    ((367, 367), (134, 134)),
    ((368, 368), (135, 135)),
    ((369, 369), (136, 136)),
    ((370, 370), (137, 137)),
    ((383, 387), (143, 143)),
    ((389, 394), (145, 145)),
    ((395, 400), (146, 146)),
    ((401, 401), (147, 147)),
    ((402, 402), (148, 148)),
    ((403, 403), (149, 149)),
)
