import numpy as np
from cvxopt import matrix, solvers

# This optimization problem is an answer to the following question:
# "How many kilometers squared of wheat and barley should a farmer plant in order to
# maximize revenue?". Each instance of the problem is parameterized by 9 values.
# These are treated as constants with respect to x_wheat and x_barley. Given a
# column vector x = np.array([[x_wheat],[x_barley]]), the objective function is
# given by f(x) = np.dot(S,x).
params = {
    'S_wheat': 3.0,
    'S_barley': 4.0,
    'L_area': 5.0,
    'L_fertilizer': 500.0,
    'L_pesticide': 300.0,
    'F_wheat': 100.0,
    'F_barley': 200.0,
    'P_wheat': 30.0,
    'P_barley': 30.0
}

# Coefficients of objective function. Each coefficient represents selling price
# of the crop in units of km^2.
S_wheat = params['S_wheat']
S_barley = params['S_barley']
S = np.array([S_wheat,S_barley])

# The farmer has limited amounts of land, fertilizer and pesticide.
# L_area has units of km^2 while L_fertilizer and L_pesticide have
# units of kg.
L_area = params['L_area']
L_fertilizer = params['L_fertilizer']
L_pesticide = params['L_pesticide']

# The cultivation of different crops might require different amount of
# fertilizer and pesticide. Every square kilometer of wheat requires
# F_wheat kilograms of fertilizer and P_wheat kilograms of pesticide.
# Every square kilometer of barley requires F_barley kilograms of fertilizer
# and P_barley kilograms of pesticide.
F_wheat = params['F_wheat']
F_barley = params['F_barley']
P_wheat = params['P_wheat']
P_barley = params['P_barley']

# Now that we have the parameters for the problem setup, we need to transform the
# constraints (as they appear in the wikipedia article) into a form that satisfies
# cvxopt's api. For each constraint we need to perform 3 sequential operations:
# 1. encode the constraints as numpy arrays
# 2. convert all greater than assertions to less than assertions
# 3. convert the result of 2 into slack form (e.g. convert inequalities to equalities)
# after steps 1, 2 and 3 all constraints can be represented as follows:
# given a column vector x = np.array([[x1],[x2]]), we can represent the
# nth constraint as np.dot(constraint_n_lhs, x) + s_n = constraint_n_rhs.
# in this example only the x1 >= 0 and x2 >= 0 assertions will be transformed
# by step 2. also note that step 3 is not very explicit in this formulation (wat?).

# constraint 1: limit on total area
# x1 + x2 <= L_area
# note that step 2 (above) does not apply because the assertion is already <=.
encode_1_lhs = np.array([1.,1.])
encode_1_rhs = np.array([L_area])
constraint_1_lhs = encode_1_lhs
constraint_1_rhs = encode_1_rhs

# constraint 2: limit on fertilizer
# F_wheat * x1 + F_barley * x2 <= L_fertilizer
encode_2_lhs = np.array([F_wheat, F_barley])
encode_2_rhs = np.array([L_fertilizer])
constraint_2_lhs = encode_2_lhs
constraint_2_rhs = encode_2_rhs

# constraint 3: limit on pesticide
# P_wheat * x1 + P_barley * x2 <= L_pesticide
encode_3_lhs = np.array([P_wheat, P_barley])
encode_3_rhs = np.array([L_pesticide])
constraint_3_lhs = encode_3_lhs
constraint_3_rhs = encode_3_rhs

# constraint 4: area of wheat planted cannot be negative
# note how we multiply both side by -1 to flip the inequality.
encode_4_lhs = np.array([1,0])
encode_4_rhs = np.array([0])
constraint_4_lhs = encode_4_lhs * -1.0
constraint_4_rhs = encode_4_rhs * -1.0

# constraint 5: area of barley planted cannot be negative
encode_5_lhs = np.array([0,1])
encode_5_rhs = np.array([0])
constraint_5_lhs = encode_5_lhs * -1.0
constraint_5_rhs = encode_5_rhs * -1.0

# bundle up all lhs
constraint_lhs = np.array([
  constraint_1_lhs,
  constraint_2_lhs,
  constraint_3_lhs,
  constraint_4_lhs,
  constraint_5_lhs
])

# bundle up all rhs
constraint_rhs = np.array([
  constraint_1_rhs,
  constraint_2_rhs,
  constraint_3_rhs,
  constraint_4_rhs,
  constraint_5_rhs
])

# notice the constraint on the slack variables (s_i >= 0) where i indexes
# the constraint. the collection of s_i's is a column vector.
# s = .. TODO: compute this

# setup the problem according to api spec
S_min = -1.0 * S
c = matrix(S_min.tolist())
G = matrix([constraint_lhs[:,0].tolist(),constraint_lhs[:,1].tolist()])
h = matrix(constraint_rhs.ravel().tolist())

sol = solvers.lp(c, G, h)
print(sol['x'])
