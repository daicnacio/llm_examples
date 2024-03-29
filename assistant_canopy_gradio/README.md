# Chat Assistant using Canopy and Gradio
The following example is a chat assistant that uses the open source Retrieval Augmented Assistant (RAG) 
framework [canopy](https://github.com/pinecone-io/canopy) and [gradio](https://www.gradio.app/) for the UI.
Canopy is built on top of the [pinecone](https://www.pinecone.io/) vector database which is used to store the
information. In this case, the information is the product catalog for the online store https://contentia.cl.

## What do you need to make it work

1. Create a Pinecone account
2. Create an OpenAI account
3. Create a python environment and install the needed packages
   ```bash
   pip install notebook pandas python-dotenv canopy-sdk trulens-eval cohere ipywidgets pyarrow pinecone-client gradio
   ```
4. create a `.env` file with the secrets , that looks like this
   ```toml
   PINECONE_API_KEY=xxxx
   FILEPATH_PARQUET="/path/to/output.parquet"
   FILEPATH_CSV_PRODUCTS="/path/to/products.csv"
   FILEPATH_CSV_EXTRAS="/path/to/extras/"
   OPENAI_API_KEY=xxxx
   PORT1=8999
   BASE_URL="xxxx"
   CANOPY_DEBUG_INFO="true"
   ```
5. Get data for storing in the vector database
6. Run notebooks.

There are three steps, the first two are only done once.
## Clean Data
The first notebook is used to clean the data. The input data is a csv exported from shopify. The html is transformed
to text using `BeautifulSoup` and then the formatted data is stored as `parquet`.

## Load data to pinecone
The second notebook is used to "upsert" the data into the pinecone database. The data has the proper columns needed
by pinecone, i.e. "id", "text", "source".

## Launch gradio app
The third notebook is used to deploy a gradio app to interact with the assistant through a UI. If you use `share=True` you can deploy it on a public website that runs while you are running the notebook.


