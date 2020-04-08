# Creating a Multi-Regression Model 
## predicting property value using zillow data
*************************************************************************
### Hypothesis:
- $H_0$: Number of bathrooms and bedrooms in home, as well as square footage will not be leading factors in predicting property value
- $H_a$: Number of bathrooms, bedrooms and square footage will have a strong reciprocy for predicting property value.
- $H_a$: Using recursive feature elimination from SK.learn will proove a different variation of features that will predict features mentioned above but not discluding other possible features included in the dataset
*************************************************************************
### Data Dictionary
*id* = primary-key / index
*bathroomcnt* = Number of restrooms on property, including half-baths and quarter-baths                     
*bedroomcnt* = Number of bedrooms in property                      
*calculatedfinishedsquarefeet* = Square footage of the property
*rawcensustractandblock* = census tracts and their unique block number *regionidcounty* = 
regionidzip                     20765 non-null float64
roomcnt                         20765 non-null float64
structuretaxvaluedollarcnt      20765 non-null float64
taxvaluedollarcnt               20765 non-null float64
assessmentyear                  20765 non-null float64
landtaxvaluedollarcnt           20765 non-null float64
taxamount                       20765 non-null float64
id                              20765 non-null int64
logerror                        20765 non-null float64
transactiondate                 20765 non-null object