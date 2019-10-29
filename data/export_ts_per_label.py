from utilities import get_ucr_dataset
import numpy as np

dataset_name = 'ItalyPowerDemand'
X_train, y_train, X_test, y_test = get_ucr_dataset('./UCR', dataset_name)

for cl in np.unique(y_train):
    indices = np.where(y_train == cl)
    ts = X_train[indices]
    np.savetxt(f"{dataset_name}_{int(cl)}.csv", ts.transpose())
