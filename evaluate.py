import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score
from statsmodels.formula.api import ols

from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression 

import math




def residuals(actual, predicted):
    return predicted - actual

def sse(actual, predicted):
    return (residuals(actual, predicted) ** 2).sum()

def mse(actual, predicted):
    n = actual.shape[0]
    return sse(actual, predicted) / n

def rmse(actual, predicted):
    return math.sqrt(mse(actual, predicted))

def ess(actual, predicted):
    return ((predicted - actual.mean()) ** 2).sum()

def tss(actual):
    return ((actual - actual.mean()) ** 2).sum()

def r2_score(actual, predicted):
    return ess(actual, predicted) / tss(actual)
    

# a function that plots residuals
def plot_residuals(df, actual, predicted):
    '''
    user inputs a dataframe, then Data or column name in data for the predictor variable.
    then Data or column name in data for the response variable. And 
    function will produce a scatter plot
    with a baseline
    '''
    sns.residplot(x=actual, y=predicted, data=df)
    
    
    
    
# function that produces a dataframe with information regarding regression errors
#def regression_errors(actual, predicted):
#    '''
#    input df.y value and df.yhat value to produce a 
#    dataframe of regression errors and their values
#    '''
#    return pd.Series({
#        'sse': sse(actual, predicted),
#        'ess': ess(actual, predicted),
#        'tss': tss(actual),
#        'mse': mse(actual, predicted),
#        'rmse': rmse(actual, predicted),
#        'R^2': r2_score(actual, predicted)
#    })
#
#ss = pd.DataFrame(np.array(['SSE','ESS','TSS', 'MSE', 'RMSE']), columns=['metric'])
#    ss['model_values'] = np.array([SSE, ESS, TSS, MSE, RMSE])

def regression_errors(actual, predicted):
    SSE = sse(actual, predicted)
    ESS = ess(actual, predicted)
    TSS = tss(actual)
    MSE = mse(actual, predicted)
    RMSE = rmse(actual, predicted)
    R2 = r2_score(actual, predicted)
    ss = pd.DataFrame(np.array(['SSE','ESS','TSS', 'MSE', 'RMSE', "R^2"]), columns=['metric'])
    ss['model_values'] = np.array([SSE, ESS, TSS, MSE, RMSE, R2])
    return ss



# function that computes SSE, MSE and RMSE for a baseline model and 
# returns the information in a dataframe
def baseline_mean_errors(actual):
    '''
    input df.y value and df.baseline_yhat value to 
    produce a dataframe of baseline regression errors 
    and their values
    '''
    predicted = actual.mean()
    return {
        'sse': sse(actual, predicted),
        'mse': mse(actual, predicted),
        'rmse': rmse(actual, predicted),
    }



# function returns True if your model is more accurate than your baseline
def better_than_baseline(actual, predicted):
    '''
    input df.y, df.yaht, df.yhat_baseline, df
    calculates SSE_baseline and SSE for the model
    then id the model's SSE is smaller than the baseline
    returns true
    '''
    sse_baseline = sse(actual, actual.mean())
    sse_model = sse(actual, predicted)
    return sse_model < sse_baseline

# takes a OLS model as input and returns the amount of variance in your mode and the f p-value
def model_significance(ols_model):
    '''
    takes an ols model as input and returns the r^2
    and the p-value
    '''
    r2 = model.rsquared
    p_value = model.f_pvalue
    df_model_sig = pd.DataFrame(np.array(['r^2', 'f p-value']), columns=['metric'])
    df_model_sig['value'] = np.array([r2, p_value])
    return df_model_sig
    
    