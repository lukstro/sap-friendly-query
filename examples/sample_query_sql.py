from pyspark.sql import SparkSession
from sap_friendly_query.query_engine import SapFriendlyQuery

spark = SparkSession.builder.appName("SAPSQLQuery").getOrCreate()
query = SapFriendlyQuery(spark)

sql = "SELECT purchase_order, company_code, created_on FROM ekko WHERE created_on >= '2024-01-01'"
df = query.query("ekko", sql)
df.show()
