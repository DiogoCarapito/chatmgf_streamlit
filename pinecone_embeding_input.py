import pandas as pd
import openai
import pinecone
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_API_ENV = os.getenv("PINECONE_API_ENV")


# read csv file
df = pd.read_csv('scripts/scrapped_data/Recomendações_choosing_wisely_30-03-2023.csv')

#print(df[0:4])
text_for_embedding = []
for index, row in df[0:4].iterrows():
    text_for_embedding.append(row['Recomendação'])

#print(text_for_embedding)

# openai api key
openai.api_key = OPENAI_API_KEY
embed_model = "text-embedding-ada-002"

# embeding texts
res = openai.Embedding.create(
    input=[
        "Sample document text goes here",
        "there will be several phrases in each batch"
    ], engine=embed_model
)

