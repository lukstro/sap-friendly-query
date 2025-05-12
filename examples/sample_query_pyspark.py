from pyspark.sql import SparkSession
from sap_friendly_query.query_engine import SapFriendlyQuery

spark = SparkSession.builder.appName("SAPPySparkQuery").getOrCreate()
query = SapFriendlyQuery(spark)

raw_df = spark.table("sap_s4hana_delta.ekko")
friendly_df = raw_df.select("purchase_order", "company_code", "created_on")
df = query.query("ekko", friendly_df)
df.show()
