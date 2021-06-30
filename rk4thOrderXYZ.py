# date: 6/29/2021

# functions that I am using; currently they are the Lorenz equations
def dxdt(t,x,y,z):
    sigma = 10

    return sigma*(y-x)

def dydt(t,x,y,z):
    rho = 28
    return rho*x-y-x*z

def dzdt(t,x,y,z):
    beta = 8/3
    return x*y - beta*z

# runge kutta 4th order function
#        -------
# t0,x0,y0,z0 -- initial conditions
# h -- step size
# tEnd -- how long the model should run to

def rungekutta(t0,tEnd, x0, y0, z0, h):
    n = int((tEnd-t0)/h)

    x = x0
    y = y0
    z = z0
    t = t0
    xList = []
    yList = []
    zList = []
    tList = []

    for i in range(1, n+1):
        k1 = dxdt(t, x, y, z)
        l1 = dydt(t, x, y, z)
        m1 = dzdt(t, x, y, z)

        k2 = dxdt(t+(h/2), x+h*(k1/2), y+h*(l1/2), z+h*(m1/2))
        l2 = dydt(t+(h/2), x+h*(k1/2), y+h*(l1/2), z+h*(m1/2))
        m2 = dzdt(t+(h/2), x+h*(k1/2), y+h*(l1/2), z+h*(m1/2))

        k3 = dxdt(t+(h/2), x+h*(k2/2), y+h*(l2/2), z+h*(m2/2))
        l3 = dydt(t+(h/2), x+h*(k2/2), y+h*(l2/2), z+h*(m2/2))
        m3 = dzdt(t+(h/2), x+h*(k2/2), y+h*(l2/2), z+h*(m2/2))

        k4 = dxdt(t+h, x+(h*k3), y+(h*l3), z+(h*m3))
        l4 = dydt(t+h, x+(h*k3), y+(h*l3), z+(h*m3))
        m4 = dzdt(t+h, x+(h*k3), y+(h*l3), z+(h*m3))

        xList.append(x)
        yList.append(y)
        zList.append(z)
        tList.append(t)

        x += h*(1/6)*(k1+(2*k2)+(2*k3)+k4)
        y += h*(1/6)*(l1+(2*l2)+(2*l3)+l4)
        z += h*(1/6)*(m1+(2*m2)+(2*m3)+m4)

        t += h

    return xList, yList, zList, tList, n

