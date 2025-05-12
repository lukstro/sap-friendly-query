# sap-friendly-query

## :bulb: About this project

While working with __SAP S/4HANA__ data in __Databricks__, I encountered a common challenge among colleagues: the difficulty of dealing with SAP's technical field names. Writing queries often meant diving into wonderfully obscure documentation just to find out what a field like AWREF actually meant. It's not exactly the most efficient way to work, and certainly not welcoming for new users.

To address this, I developed a lightweight solution that allows users to query __SAP S/4HANA__ tables stored in __Databricks Delta Lake__ using friendly, human-readable field names. This means users can write intuitive queries in either __SQL__ or __PySpark__ without needing to memorize technical __SAP__ terminology.

The tool automatically translates these friendly field names into their corresponding __SAP__ technical names before executing the query, improving accessibility, reducing friction, and making __SAP__ data analysis faster and more user-friendly.

## :open_file_folder: Project Structure

    sap-friendly-query/
    ├── sap_friendly_query/
    │   ├── __init__.py
    │   ├── config.py
    │   ├── mappings/
    │   │   ├── __init__.py
    │   │   └── table_mappings.py
    │   ├── query_engine.py
    ├── examples/
    │   └── sample_query_sql.py
    │   └── sample_query_pyspark.py
    ├── requirements.txt
    ├── README.md


## :wrench: Features

:heavy_check_mark: Write queries using human-readable field names. <br/>
:heavy_check_mark: Supports both __SQL__ and __PySpark__ syntax. <br/>
:heavy_check_mark: Automatically maps between friendly and technical __SAP__ column names. <br/>

## :computer: Usage

### Using __SQL__
```python
from pyspark.sql import SparkSession
from sap_friendly_query.query_engine import SAPQueryHelper

spark = SparkSession.builder.appName("SAPSQLQuery").getOrCreate()
query_helper = SAPQueryHelper(spark)

sql = "SELECT purchase_order, company_code, created_on FROM ekko WHERE created_on >= '2024-01-01'"
df = query_helper.query("ekko", sql)
df.show()
```

### Using __Pyspark__
```python
from pyspark.sql import SparkSession
from sap_friendly_query.query_engine import SAPQueryHelper

spark = SparkSession.builder.appName("SAPPySparkQuery").getOrCreate()
query_helper = SAPQueryHelper(spark)

raw_df = spark.table("sap_s4hana_delta.ekko")
friendly_df = raw_df.select("purchase_order", "company_code", "created_on")
df = query_helper.query("ekko", friendly_df)
df.show()
```
