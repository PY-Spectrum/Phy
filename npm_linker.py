"""quadratic eqn calculator"""


def eqn(x_2,x,c):
   soln_1 = (-x+((x**2)-(4*x_2*c))**0.5)/(2*x_2)
   soln_2= (-x-((x**2)-(4*x_2*c))**0.5)/(2*x_2)
   soln_tuple = (soln_1,soln_2)

   return soln_tuple
