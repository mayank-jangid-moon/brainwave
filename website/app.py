from flask import Flask, render_template, request
import asyncio
from dotenv import dotenv_values
from apify_client import ApifyClientAsync

app = Flask(__name__)
apify_client = ApifyClientAsync(dotenv_values(".env")["TOKEN"])

async def run_apify_task(client):
    result = await client.call()
    return result or {}

async def scrape(id):
    input = { "usernames": id }
    actor_call = await apify_client.actor('apify/instagram-profile-scraper').call(run_input=input)
    dataset_client = apify_client.dataset(actor_call['defaultDatasetId']) or {}
    dataset_items = await dataset_client.list_items()
    return dataset_items.items

# def scrape(id):
#     input = { "usernames": id }
#     actor_call = apify_client.actor('apify/instagram-profile-scraper').call(run_input=input)
#     dataset_client = apify_client.dataset(actor_call['defaultDatasetId'])
#     dataset_items = dataset_client.list_items().items
#     print(dataset_items)

@app.route("/")
def get_index():
    # asyncio.run(scrape([]))
    return render_template("index.html")

@app.route("/", methods=["POST"])
def post_index():
    ids = request.form['ids'].split('\n')
    for i in range(len(ids)):
        ids[i] = ids[i].strip("\r\n")
    print(ids)
    return asyncio.run(scrape(ids))

if __name__ == "__main__":
    app.run(port=5000)
