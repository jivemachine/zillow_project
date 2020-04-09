import pandas as pd
import numpy as np

from env import host, user, password

# function to get the url

def get_db_url(db_name):
    return f"mysql+pymysql://{user}:{password}@{host}/{db_name}"

# function that passes my query and my url to return df

def get_data_from_sql():
    query = '''
    SELECT * 
    FROM properties_2017
    LEFT JOIN predictions_2017 USING(parcelid)
    WHERE propertylandusetypeid NOT IN (246, 247, 248, 46, 47, 265, 267, 290, 291)
    AND transactiondate BETWEEN "2017-05-01" AND "2017-06-31"''
    AND bathroomcnt >= 1
    AND bedroomcnt >= 1
    '''
    df = pd.read_sql(query, get_db_url('zillow'))
    return df

# function that rules them all by acquiring and prepping my df for exploration or modeling

def wrangle_zillow():
    df = get_data_from_sql()
    df = df.drop(columns=['fireplaceflag','yardbuildingsqft26','yardbuildingsqft17','typeconstructiontypeid','threequarterbathnbr','storytypeid','pooltypeid7','pooltypeid2','pooltypeid10','poolsizesum','poolcnt','heatingorsystemtypeid','hashottuborspa','fireplacecnt','finishedsquarefeet6','finishedsquarefeet50','finishedsquarefeet15','finishedsquarefeet13','finishedfloor1squarefeet','calculatedbathnbr','buildingqualitytypeid', 'airconditioningtypeid', 'buildingclasstypeid', 'basementsqft', 'decktypeid', 'architecturalstyletypeid'])
    df = df.drop(columns=['lotsizesquarefeet','censustractandblock','fullbathcnt','finishedsquarefeet12','propertycountylandusecode','propertylandusetypeid','parcelid', 'garagecarcnt', 'garagetotalsqft', 'latitude', 'longitude', 'unitcnt', 'numberofstories', 'taxdelinquencyflag','taxdelinquencyyear' ])
    df = df.drop(columns=["propertyzoningdesc", 'regionidcity', 'regionidneighborhood', 'yearbuilt', 'regionidzip'])
    df.dropna(axis=0, inplace=True)
    return df