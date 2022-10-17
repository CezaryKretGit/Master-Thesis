from sklearn.tree import DecisionTreeRegressor
from sklearn.cluster import KMeans


def prepare_DicisionTreeRegressor():
    model = DecisionTreeRegressor()
    params = dict()
    params['max_depth'] = [3, 6, 9]
    return model, params


N_CLUSTERS_INDEX = 0
RANDOM_STATE_INDEX = 1


def kmeans_builder(params):
    return KMeans(n_clusters=params[N_CLUSTERS_INDEX], random_state=params[RANDOM_STATE_INDEX])


def kmeans_get_params():
    params = []
    # n_clusters
    params.insert(N_CLUSTERS_INDEX, [2, 3, 4, 5, 6, 8])
    # random_state
    params.insert(RANDOM_STATE_INDEX, [1, 10, 100, 1000])

    return params