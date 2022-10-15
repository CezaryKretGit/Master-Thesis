from collections.abc import Callable
from sklearn.model_selection import GridSearchCV
import numpy as np
import pandas as pd

SCV_DATA_PATH = 'TO DO'


def example_prepare_data() -> (pd.DataFrame, pd.DataFrame):
    return pd.DataFrame(), pd.DataFrame()


def _ignore_cols(data: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    return data.drop(columns=columns, inplace=False, errors='ignore')


def experiment(train_data, cluster_model, regression_model, regression_vals):
    train_feats, train_labels = _ignore_cols(train_data, ['labels', 'cluster']), train_data['labels']

    # clustering
    cluster_model.fit(train_feats)
    train_data['cluster'] = cluster_model.predict(train_feats)
    print(train_data['cluster'])

    # regression learning not clustered
    grid_search = GridSearchCV(estimator=regression_model, param_grid=regression_vals, scoring='r2',
                                    cv=6, refit=True, return_train_score=True)
    only_regression_results = grid_search.fit(train_feats, train_labels)

    # regression learning clustered data
    train_enriched_feats = _ignore_cols(train_data, ['labels'])

    grid_search = GridSearchCV(estimator=regression_model, param_grid=regression_vals, scoring='r2',
                                    cv=6, refit=True, return_train_score=True)
    with_clustering_results = grid_search.fit(train_enriched_feats, train_labels)

    return only_regression_results, with_clustering_results


class Pipeline:

    def __init__(self, data_transform_function: Callable[[], (pd.DataFrame, pd.DataFrame)],
                 regression_models: list, cluster_models: list):
        self.prepare_data = data_transform_function
        self.regression_models_with_params = regression_models
        self.cluster_models = cluster_models

    def full_training(self):
        train_data, test_data = self.prepare_data()
        results = []
        for cluster_model in self.cluster_models:
            for regression_model, params in self.regression_models_with_params:
                results.append(experiment(train_data, cluster_model, regression_model, params))

        return results


if __name__ == '__main__':
    print(np.__version__)
    print(pd.__version__)
    exit()
