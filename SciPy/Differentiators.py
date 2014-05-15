import numpy as np
def twoPtForwardDiff(x,y):
    """This function takes the data (x) and the function of the data (y) and takes the derivative using the two point forward difference method."""
    dydx = np.zeros(y.shape,float)
    dydx[0:-1] = np.diff(y)/np.diff(x)
    dydx[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2])
    return dydx

def twoPtCenteredDiff(x,y):
    """This function takes the data (x) and the function of the data (y) and takes the derivative using the two point centered difference method."""
    dydx = np.zeros(y.shape,float)
    dydx[1:-1] = (y[2:] - y[:-2]) / (x[2:] - x[:-2])
    dydx[0] = (y[1] - y[0]) / (x[1] - x[0])
    dydx[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2])
    return dydx

def fourPtCenteredDiff(x,y):
    """This function takes the data (x) and the function of the data (y) and takes the derivative using the four point centered difference method."""
    dydx = np.zeros(y.shape,float)
    dydx[2:-2] = ((y[0:-4] - 8*y[1:-3]) + (8*y[3:-1] - y[4:])) / (12*(x[1] - x[0]))
    dydx[0] = (y[1] - y[0]) / (x[1] - x[0])
    dydx[1] = (y[2] - y[1]) / (x[2] - x[1])
    dydx[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2])
    dydx[-2] = (y[-2] - y[-1]) / (x[-3] - x[-2])
    return dydx