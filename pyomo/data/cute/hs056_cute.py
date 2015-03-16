#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________
#
#   Taken from cute suite. Formulated in pyomo by Logan Barnes.

from pyomo.core import *
model = ConcreteModel()
model.N = RangeSet(1,7)
model.x = Var(model.N,bounds=(0,None))

model.x[1] = 1
model.x[2] = 1
model.x[3] = 1
model.x[4] = asin(sqrt(1/4.2))
model.x[5] = asin(sqrt(1/4.2))
model.x[6] = asin(sqrt(1/4.2))
model.x[7] = asin(sqrt(5/7.2))

model.obj = Objective(expr=-model.x[1]*model.x[2]*model.x[3])

model.constr1 = Constraint(expr=model.x[1] - 4.2*sin(model.x[4])**2 == 0)
model.constr2 = Constraint(expr=model.x[2] - 4.2*sin(model.x[5])**2 == 0)
model.constr3 = Constraint(expr=model.x[3] - 4.2*sin(model.x[6])**2 == 0)
model.constr4 = Constraint(expr=model.x[1] + 2*model.x[2] + 2*model.x[3] - 7.2*sin(model.x[7])**2 == 0)

