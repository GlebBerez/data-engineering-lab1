import boto3
s3=boto3.client("s3",
                endpoint_url="http://localhost:9000",
                aws_access_key_id="admin",
                aws_secret_access_key="viktorfest03"
                )

s3.upload_file(
    "morbidity.csv",
    "healthcare-data",
    "raw/morbidity.csv"
)

s3.upload_file(
    "morbidity.parquet",
    "healthcare-data",
    "processed/morbidity.parquet"
)