from utilities import get_ucr_dataset
import numpy as np
import pandas as pd
import argparse

def main(args):

    dataset_name = args.dataset
    X_train, y_train, X_test, y_test = get_ucr_dataset('./UCR', dataset_name)

    for cl in np.unique(y_train):
        indices = np.where(y_train == cl)
        ts = X_train[indices]
        pd.DataFrame(ts.transpose()).to_csv(f"{dataset_name}_{int(cl)}.csv", index_label='ind')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dataset', type=str, help="Name of data set")

    args = parser.parse_args()
    main(args)
