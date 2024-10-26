from flask import Flask, render_template, request
import joblib
import pandas as pd
from pipeline import private_pipeline, public_pipeline
from dotenv import dotenv_values
from ondemand import ondemand_summary
from apify_client import ApifyClient

app = Flask(__name__)
apify_client = ApifyClient(dotenv_values(".env")["TOKEN"])
model_priv = joblib.load('./model_random_forest_private.pkl')
model_pub = joblib.load('./model_public_final.pkl')

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
    item = scrape([id])[0]
    model = model_pub
    df = pd.DataFrame([item])
    data = ["", 0, "", False]
    try:
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
            data[0] = "real"
            summary = ondemand_summary(id)
        else:
            data[0] = "fake"
        data[1] = max_res
        data[2] = summary
        if item["private"] and data[0] == "real" and max_res < 0.733:
            data[0] = "fake"
    except:
        data[0] = "non-existent"
        data[3] = True
    return render_template("SeUI.html", data=data)

if __name__ == "__main__":
    app.run(port=5000)
