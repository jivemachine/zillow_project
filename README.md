# Creating a Model 
## that can be used to predict property value using zillow data

### Hypothesis:
- $H_0$: Number of bathrooms and bedrooms in home, as well as square footage will not be leading factors in predicting property value
- $H_a$: Number of bathrooms, bedrooms and square footage will have a strong reciprocy for predicting property value.
- $H_a$: Using recursive feature elimination from SK.learn will proove a different variation of features that will predict features mentioned above but not discluding other possible features included in the dataset

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

### Deliverables

- Link for google presentation [HERE](https://docs.google.com/presentation/d/1Gt7IMrhgTrMt7yxNsx0tpbm9yQ2UV5YE6aisZ81BCXA/edit?usp=sharing).
- GitHub repository above

### To Reproduce My Results
- env.py file is required with log-in credentials to the database used
- My SQL query is in the zillow_wrangle.py file in the repository above
- random state used in the split my data function is 830

