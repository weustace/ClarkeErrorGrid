import sys
sys.path.append("./..")

from ClarkeErrorGrid import clarke_error_grid
import matplotlib.pyplot as plt
import numpy as np
#synthesise some data with random errors

actual_concs = np.random.rand(100)*400
errors = (np.random.random(100)*0.5)+0.75 #need to centre at 1
pred_concs = actual_concs * errors
improved_pred_concs = actual_concs * ((np.random.random(100)*0.1)+0.9)
plot_obj, zones = clarke_error_grid(actual_concs,pred_concs,color="red",marker='.',label="Original prediction method")
plot_obj.scatter(actual_concs,improved_pred_concs,color='green',marker='x',label="New and improved method!")
plt.legend()
plt.show()