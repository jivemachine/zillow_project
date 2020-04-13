# Creating a Multi-Regression Model 
## predicting property value using zillow data
*************************************************************************
### Hypothesis:
- $H_0$: Number of bathrooms and bedrooms in home, as well as square footage will not be leading factors in predicting property value
- $H_a$: Number of bathrooms, bedrooms and square footage will have a strong reciprocy for predicting property value.
- $H_a$: Using recursive feature elimination from SK.learn will proove a different variation of features that will predict features mentioned above but not discluding other possible features included in the dataset
*************************************************************************
### Data Dictionary


| Unit-Title | Description |
|--- |---|
|id | primary-key / index|
| bathroomcnt |  Number of restrooms in unit (including half-baths and quarter-baths) |
| bedroomcnt | Number of bedrooms in unit |
| calculatedfinishedsquarefeet | Square footage of the property |
|roomcnt | Number of rooms in unit |
|structuretaxvaluedollarcnt | property value |
| taxamount | The amount the homeowner was taxed |
| transactiondate | The date of the last transaction |