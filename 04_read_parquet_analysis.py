import s3fs
import pandas as pd

storage_options={
    "key": "admin",
    "secret": "viktorfest03",
    "client_kwargs": {"endpoint_url": "http://localhost:9000"}
}

df_from_minio=pd.read_parquet("s3://healthcare-data/processed/morbidity.parquet",storage_options=storage_options)

result=(df_from_minio.groupby("disease_class")["rate_per_1000"]
         .mean()
         .sort_values(ascending=False)
         )
print("\nСредний процент заболеваемости")
print(result)

result=df_from_minio[df_from_minio["rate_per_1000"]>=50]
print("\nЗаболеваемость больше 50:")
print(result)

result=(
    df_from_minio
    .groupby("year")
    .agg(
        average_rate=("rate_per_1000","mean"),
        max_rate=("rate_per_1000", "max"),
        min_rate=("rate_per_1000","min"),
        total_cases_thousands=("cases_thousands","sum"),
    )
    .reset_index()
)
print("\n Агрегация: ")
print(result)

result.to_parquet("s3://healthcare-data/analytics/disease_statistics.parquet",
                  storage_options=storage_options,
                  index=False
                  )