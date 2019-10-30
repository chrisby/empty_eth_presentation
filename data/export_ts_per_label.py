from utilities import get_ucr_dataset
import numpy as np
import pandas as pd

dataset_name = 'FacesUCR'
X_train, y_train, X_test, y_test = get_ucr_dataset('./UCR', dataset_name)

for cl in np.unique(y_train):
    indices = np.where(y_train == cl)
    ts = X_train[indices]
    pd.DataFrame(ts.transpose()).to_csv(f"{dataset_name}_{int(cl)}.csv", index_label='ind')
