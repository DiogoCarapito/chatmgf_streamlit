import openai
import pinecone
from dotenv import load_dotenv

from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

load_dotenv()  # Load variables from .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_API_ENV = os.getenv("PINECONE_API_ENV")
print('api loaded')


# openai api initialization
openai.api_key = OPENAI_API_KEY
embed_model = "text-embedding-ada-002"

print('OpenAI initialized')

# pinecone api initialization
index_name = 'choosing-wisely-test'

# initialize connection to pinecone
pinecone.init(
    api_key="PINECONE_API_KEY",  # app.pinecone.io (console)
    environment="PINECONE_API_ENV"  # next to API key in console
)
print('Pinecone initialized')


query = "posso fazer citologia a uma senhora de 75 anos?"

res = openai.Embedding.create(
    input=[query],
    engine=embed_model
)

# retrieve from Pinecone
xq = res['data'][0]['embedding']

# get relevant contexts (including the questions)
res = index.query(xq, top_k=3, include_metadata=True)


# system message to 'prime' the model
primer = f"""You are Q&A bot. A highly intelligent system that answers
user questions based on the information provided by the user above
each question. If the information can not be found in the information
provided by the user you truthfully say "I don't know".
"""

res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": primer},
        {"role": "user", "content": augmented_query}
    ]
)

llm = OpenAI(temperature=0.1)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good product for {product}?",
)
llm_chain = LLMChain(llm=llm, prompt_template=prompt)