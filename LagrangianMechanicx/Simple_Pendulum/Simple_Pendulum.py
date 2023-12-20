import numpy as np
import sympy as smp
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import PillowWriter
from sympy.physics.mechanics import *

L=smp.symbols('L')
g=9.81
t,g,m=smp.symbols('t g m')
the=dynamicsymbols('theta')
x1=L*smp.sin(the)
y1=L*smp.cos(the)
the_d=smp.diff(the,t)
the_dd=smp.diff(the_d,t)
vx=smp.diff(x1,t)
vy=smp.diff(y1,t)
T=1/2*m*(vx**2+vy**2)
V=m*g*L*(1-smp.cos(the))
L=T-V
LE= smp.diff(smp.diff(L,the_d),t)-smp.diff(L,the)
soln=smp.solve(LE,the,simplify=False)[0]
soln_lambda=lambda t,c: soln.subs([(t,t),(the.diff(t),c)])

lhs=L.diff(the)
rhs=smp.diff(L.diff(the_d),t)

eq=rhs-lhs
eq=smp.solve(eq,the_dd)[0]
display(eq.simplify())

class Pendulum:
    
    def __init__(self, l, t, theta0, v0):
        
        self.l = l
        self.t = t
        self.conds = [theta0, v0]
        
    def solvepend(self):
        
        m,g,l,t = smp.symbols(('m', 'g','l','t'))
        the = smp.Function('theta')(t)
        dthe = the.diff(t)
        ddthe = dthe.diff(t)
        
        x,y = l*smp.sin(the), -l*smp.cos(the)
        
        T = smp.Rational(1,2) *m*(x.diff(t)**2+y.diff(t)**2)
        V = m*g*y
        L = T-V
        
        lhs = L.diff(the)
        rhs = smp.diff( L.diff(dthe), t)
        
        eq = rhs-lhs
        
        eq = smp.solve(eq, ddthe)[0]
        
        dthetadt_num = smp.lambdify(dthe, dthe)
        dudt_num = smp.lambdify((g,l,the), eq)
        
        x_num, y_num = smp.lambdify((l,the), x), smp.lambdify((l,the), y)
        
        del m,g,l,t
        
        g = 9.81
        l = self.l
        t = self.t
        conds = self.conds
        
        def dXdt(X,t,g,l):
            
            the_num, u_num = X
            dthedt_num = smp.lambdify(dthe, dthe)
            
            return [dthedt_num(u_num),
                   dudt_num(g,l,the_num)]
        
        sol = odeint(dXdt, t=t, y0 = conds, args= (g,l))
        angle = sol.T[0]
        velocity = sol.T[1]      
        
        return x_num(l,angle), y_num(l,angle)
t = np.linspace(0,10, 500)
pend = Pendulum(1,t,np.pi/4, 0)
x,y = pend.solvepend()
x0,y0 = x[0], y[0]

fig = plt.figure()
ax = fig.add_subplot(aspect='equal')

line, = ax.plot([0, x0], [0, y0], lw=3, c='green')
bob_radius = 0.08
circle = ax.add_patch(plt.Circle((x0,y0), bob_radius,
                      fc='r', zorder=3))

ax.set_xlim([-x.max()-0.5, x.max()+0.5])
ax.set_ylim([y.min()-0.5,0.5])

def animate(i):
    """Update the animation at frame i."""
    line.set_data([0, x[i]], [0, y[i]])
    circle.set_center((x[i], y[i]))

nsteps = len(x)
nframes = nsteps
dt = t[1]-t[0]
interval = dt * 1000
ani = animation.FuncAnimation(fig, animate, frames=nframes, repeat=True,
                              interval=interval)
from matplotlib import animation
from IPython.display import HTML

HTML(ani.to_html5_video())
            