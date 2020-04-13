# Creating a Multi-Regression Model 
## predicting property value using zillow data
*************************************************************************
### Hypothesis:
- $H_0$: Number of bathrooms and bedrooms in home, as well as square footage will not be leading factors in predicting property value
- $H_a$: Number of bathrooms, bedrooms and square footage will have a strong reciprocy for predicting property value.
- $H_a$: Using recursive feature elimination from SK.learn will proove a different variation of features that will predict features mentioned above but not discluding other possible features included in the dataset
*************************************************************************
### Data Dictionary
--- *id* = primary-key / index
--- *bathroomcnt* = Number of restrooms on property, including half-baths and quarter-baths                     
--- *bedroomcnt* = Number of bedrooms in property                      
--- *calculatedfinishedsquarefeet* = Square footage of the property
--- *roomcnt* = Number of rooms in home
--- *structuretaxvaluedollarcnt* = property value
--- *taxamount* =
--- *transactiondate* = The date the last transaction was made regarding the house.