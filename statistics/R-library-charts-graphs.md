
#### Density plot in R
```
require(tigerstats)

# With no particular column of dataset 'data'
densityplot(data, xlab="X axis label", main="Distribution of ...)

# plot on a particular column/attribute 'column1 of dataset 'data'
densityplot(~column1, data, xlab="X axis label", main="Distribution of ...)

densityplot(~income,data, xlab="Income", main="Distribution of Income")
```
