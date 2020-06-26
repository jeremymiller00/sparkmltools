from pyspark.sql.session import SparkSession
import random
import numpy as np
import scipy as scs
import matplotlib.pyplot as plt

spark = SparkSession.builder.getOrCreate()

def make_df():
    data = []
    for i in range(100):
        row = []
        for i in range(10):
            row.append(random.random())
        data.append(row)

    cols = []
    for i in range(1, 10):
        cols.append('col' + str(i))

    df = spark.createDataFrame(data,cols)
    return df


def test_partial_dependence_plot():
    assert True == 1

def test_partial_dependence_plot():
    df = make_df()
    partial_dependence_plot(df, y_column='col10', model, feature_column, model_type='classification',
                            model_input_col='features', columns_to_exclude=(), n_samples=10):



# if __name__ == '__main__':
#     print("Executing tests...")
#     df = make_df()
#     df.show()