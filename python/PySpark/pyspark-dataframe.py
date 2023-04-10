
## Creating Spark Context
```
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]") \
                    .appName('e2esa') \
                    .getOrCreate()
print(spark.sparkContext)
print("appName: "+ spark.sparkContext.appName)
```

## Read a CSV
```
url = "https://github.com/e2eSolutionArchitect/datascience/blob/main/python/test-data.csv"
from pyspark import SparkFiles
spark.sparkContext.addFile(url)
```

```
df = spark.read.csv(SparkFiles.get("test-data.csv"), header=True, inferSchema= True)
df.show()
df.printSchema()
```

## Save as parquet file 
```
df.write.parquet('ssa.parquet')
```

## Read parquet file
```
import pandas as pd
pd.read_parquet('ssa.parquet', engine='pyarrow')
```
