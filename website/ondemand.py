import requests

# Replace with your actual API key and external user ID
api_key = 'irWX8sdehvccExO1cVM2gLANSDPrNJSG'
external_user_id = 'apify_api_5668AcSZ1RpnmmN5XXhzIDD1Couzga33a4ER'

# Create Chat Session
create_session_url = 'https://api.on-demand.io/chat/v1/sessions'
create_session_headers = {
    'apikey': api_key
}
create_session_body = {
    "pluginIds": [],
    "externalUserId": external_user_id
}

def ondemand_summary(id):
    response = requests.post(create_session_url, headers=create_session_headers, json=create_session_body)
    response_data = response.json()

    session_id = response_data['data']['id']

    submit_query_url = f'https://api.on-demand.io/chat/v1/sessions/{session_id}/query'
    submit_query_headers = {
        'apikey': api_key
    }
    submit_query_body = {
        "endpointId": "predefined-openai-gpt4o",
        "query": id,
        "pluginIds": ["plugin-1729893241"],
        "responseMode": "sync"
    }

    query_response = requests.post(submit_query_url, headers=submit_query_headers, json=submit_query_body)
    query_response_data = query_response.json()
    try:
        return query_response_data["data"]["answer"]
    except:
        return ""

