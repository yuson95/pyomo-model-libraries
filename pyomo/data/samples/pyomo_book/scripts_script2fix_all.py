import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/nonlinear/multimodal/')

# @all:
from pyomo.opt import SolverFactory
from multimodal import model

opt = SolverFactory("ipopt")
instance = model.create()

instance.y = 3.5
instance.x = 3.5
instance.y.fixed = True

results = opt.solve(instance)
instance.load(results)

xval = instance.x.value
print "First   x was", instance.x.value, \
        "and y was", instance.y.value

instance.x.fixed = True
instance.y.fixed = False

results = opt.solve(instance)
instance.load(results)

print "Next    x was", instance.x.value, \
        "and y was", instance.y.value

instance.x.fixed = False
instance.y.fixed = True

results = opt.solve(instance)
instance.load(results)

print "Finally x was", instance.x.value, \
        "and y was", instance.y.value
# @:all
