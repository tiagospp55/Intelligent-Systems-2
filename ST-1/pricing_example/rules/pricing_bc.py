# pricing_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def week_package(rule, arg_patterns, arg_context):
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
        with engine.prove('packages', 'package', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pricing.week_package: got unexpected plan from when clause 1"
            if context.lookup_data('delta').days >= 7:
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def day_package(rule, arg_patterns, arg_context):
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
        with engine.prove('packages', 'package', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pricing.day_package: got unexpected plan from when clause 1"
            if context.lookup_data('delta').days >= 1:
              if context.lookup_data('delta').days < 7:
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def day_package_for_week(rule, arg_patterns, arg_context):
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
        with engine.prove('packages', 'package', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pricing.day_package_for_week: got unexpected plan from when clause 1"
            if context.lookup_data('delta').days >= 7:
              notany34_worked = True
              with engine.prove('packages', 'package', context,
                                (rule.pattern(1),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "pricing.day_package_for_week: got unexpected plan from when clause 3"
                  notany34_worked = False
                  if not notany34_worked: break
              if notany34_worked:
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('pricing')
  
  bc_rule.bc_rule('week_package', This_rule_base, 'packages',
                  week_package, None,
                  (pattern.pattern_literal('weekly'),
                   contexts.variable('delta'),),
                  (),
                  (pattern.pattern_literal('weekly'),))
  
  bc_rule.bc_rule('day_package', This_rule_base, 'packages',
                  day_package, None,
                  (pattern.pattern_literal('daily'),
                   contexts.variable('delta'),),
                  (),
                  (pattern.pattern_literal('daily'),))
  
  bc_rule.bc_rule('day_package_for_week', This_rule_base, 'packages',
                  day_package_for_week, None,
                  (pattern.pattern_literal('daily'),
                   contexts.variable('delta'),),
                  (),
                  (pattern.pattern_literal('daily'),
                   pattern.pattern_literal('weekly'),))


Krb_filename = '../pricing.krb'
Krb_lineno_map = (
    ((14, 18), (6, 6)),
    ((20, 25), (8, 8)),
    ((26, 26), (9, 9)),
    ((39, 43), (18, 18)),
    ((45, 50), (20, 20)),
    ((51, 51), (21, 21)),
    ((52, 52), (22, 22)),
    ((65, 69), (30, 30)),
    ((71, 76), (32, 32)),
    ((77, 77), (33, 33)),
    ((79, 84), (35, 35)),
)
