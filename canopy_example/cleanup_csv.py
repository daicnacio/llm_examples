import pandas as pd
from bs4 import BeautifulSoup

def html_to_text(text):
    soup = BeautifulSoup(text)
    return soup.get_text()
def clean_csv(filepath):
    df=pd.read_csv(filepath)
    df_filtered=df[~df["Body (HTML)"].isnull()][["Handle","Body (HTML)","SEO Description","Variant Price"]]
    df_filtered["Body Filtered HTML"]=df_filtered["Body (HTML)"].apply(html_to_text)
    df_filtered.to_parquet("products_export_1.parquet")

