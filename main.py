"""
Code purpose: Illustrate a ML file structure

Written by Raquel Aoki
Date: September 2021

This is a new test

For an example using absl.flags, visit https://abseil.io/docs/python/guides/flags
"""
import os
import pandas as pd
import sys
import utils
import yaml

from data_preprocessing import make_dataset


def main(config_path):
    """ Main function of the project.
    It loads config settings, dataset, run all the methods, save output.
    Args:
        config_path: path for the config files.
    """
    print('Starting...')
    # Load the config file. All comments should end with a .
    with open(config_path) as f:
        config = yaml.safe_load(f)
    params = config["parameters"]

    # Load dataset.
    X_train, X_test, y_train, y_test = make_dataset(params)

    # Run methods.
    output = utils.run_methdos(X_train, X_test, y_train, y_test, params)

    # Save results.
    if params['save_output']:
        file_path = params['path_output'] + str(params['config']) + '.csv'
        output.to_csv(file_path)
    else:
        print(output)
    print('Done!')
    return


if __name__ == "__main__":
    main(config_path=sys.argv[1])
