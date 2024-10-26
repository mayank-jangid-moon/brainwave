from flask import Flask, render_template, request
# import pickle
import joblib
import pandas as pd
from pipeline import private_pipeline, public_pipeline
from dotenv import dotenv_values
from ondemand import ondemand_summary
from apify_client import ApifyClient

app = Flask(__name__)
apify_client = ApifyClient(dotenv_values(".env")["TOKEN"])
# model_priv = pickle.load(open('./model_svm_private.pkl', 'rb'))
# model_pub = pickle.load(open('./model_svm_public.pkl', 'rb'))
model_priv = joblib.load('./model_svm_private.pkl')
model_pub = joblib.load('./model_svm_public.pkl')

def scrape(id):
    input = { "usernames": id }
    actor_call = apify_client.actor('apify/instagram-profile-scraper').call(run_input=input)
    dataset_client = apify_client.dataset(actor_call['defaultDatasetId']) or {}
    dataset_items = dataset_client.list_items()
    return dataset_items.items

@app.route("/")
def get_index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def post_index():
    id = request.form['ids']
    id = id.strip("\r\n")
    # return asyncio.run(scrape(ids))
    item = scrape([id])[0]
    model = model_pub
    # try:
    df = pd.DataFrame([item])
    if item["private"]:
        model = model_priv
        df = private_pipeline(df)
    else:
        df = public_pipeline(df)
    prediction = model.predict(df)[0]
    result = model.predict_proba(df).tolist()[0]
    max_res = max(result)
    summary = ""
    if prediction == 0:
        summary = ondemand_summary(id)
    return str([prediction, max_res, summary])
    # except:
    #     return "Non-existent id"

if __name__ == "__main__":
    app.run(port=5000)
