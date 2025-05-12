from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col
from sap_friendly_query.mappings.table_mappings import TABLE_MAPPINGS
from sap_friendly_query.config import DEFAULT_DATABASE

class SapFriendlyQuery:
    def __init__(self, spark: SparkSession, database: str = DEFAULT_DATABASE):
        self.spark = spark
        self.database = database

    def _get_table_mapping(self, table: str) -> dict:
        mapping = TABLE_MAPPINGS.get(table.lower())
        if not mapping:
            raise ValueError(f"No mapping found for table '{table}'")
        return mapping
      
    def _reverse_mapping(self, mapping: dict) -> dict:
        return {v: k for k, v in mapping.items()}

    def _is_sql_query(self, query) -> bool:
        return isinstance(query, str) and query.strip().lower().startswith("select")

    def _translate_sql_query(self, query: str, table: str) -> str:
        mapping = self._get_table_mapping(table)
        for friendly, technical in mapping.items():
            query = query.replace(friendly, technical)
        return query

    def _translate_df_to_technical(self, df: DataFrame, table: str) -> DataFrame:
        mapping = self._get_table_mapping(table)
        return df.select([col(f).alias(mapping.get(f, f)) for f in df.columns])

    def _translate_df_to_friendly(self, df: DataFrame, table: str) -> DataFrame:
        mapping = self._get_table_mapping(table)
        reverse = self._reverse_mapping(mapping)
        return df.select([col(c).alias(reverse.get(c, c)) for c in df.columns])

    def query(self, table: str, query_input) -> DataFrame:
        if self._is_sql_query(query_input):
            translated_sql = self._translate_sql_query(query_input, table)
            df = self.spark.sql(translated_sql)
        elif isinstance(query_input, DataFrame):
            df = self._translate_df_to_technical(query_input, table)
        else:
            raise TypeError("Query must be a SQL string or a PySpark DataFrame")

        return self._translate_df_to_friendly(df, table)
