import sklearn
from sklearn.tree import DecisionTreeRegressor
from sklearn.cluster import KMeans
from sklearn.datasets import load_diabetes
import pandas as pd
from thesis import Pipeline
from thesis.models import KMeansBuilder, prepare_DicisionTreeRegressor


def prepare_testing_data():
    X, y = load_diabetes(return_X_y=True)
    X = pd.DataFrame(data=X, columns=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    X['labels'] = y
    return X.iloc[:300], X.iloc[300:]


def test_basic_pipeline():
    pipeline = Pipeline(prepare_testing_data,
                        [(DecisionTreeRegressor(), {'max_depth': [3, 6, 9]}),
                         (DecisionTreeRegressor(), {'max_depth': [5, 8]})],
                        [KMeansBuilder(), ])
    results_df = pipeline.results_as_df(pipeline.full_training())
    print(results_df.iloc[0])


def test_pipeline_with_basic_model_creator():
    pipeline = Pipeline(prepare_testing_data,
                        [prepare_DicisionTreeRegressor(), prepare_DicisionTreeRegressor()],
                        [KMeansBuilder(), ])
    results_df = pipeline.results_as_df(pipeline.full_training())
    print(results_df.iloc[0])



if __name__ == '__main__':
    test_basic_pipeline()
