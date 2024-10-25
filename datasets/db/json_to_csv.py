import os
import json
import csv

def json_to_flat_dict(json_file):
    with open(json_file, 'r') as jf:
        data = json.load(jf)
    
    # Flatten data
    flat_data = {
        "logging_page_id": data.get("logging_page_id"),
        "show_suggested_profiles": data.get("show_suggested_profiles"),
        "show_follow_dialog": data.get("show_follow_dialog"),
        "user_biography": data["graphql"]["user"].get("biography"),
        "user_blocked_by_viewer": data["graphql"]["user"].get("blocked_by_viewer"),
        "user_restricted_by_viewer": data["graphql"]["user"].get("restricted_by_viewer"),
        "user_country_block": data["graphql"]["user"].get("country_block"),
        "user_external_url": data["graphql"]["user"].get("external_url"),
        "user_followers": data["graphql"]["user"]["edge_followed_by"].get("count"),
        "user_fbid": data["graphql"]["user"].get("fbid"),
        "user_followed_by_viewer": data["graphql"]["user"].get("followed_by_viewer"),
        "user_following": data["graphql"]["user"]["edge_follow"].get("count"),
        "user_follows_viewer": data["graphql"]["user"].get("follows_viewer"),
        "user_full_name": data["graphql"]["user"].get("full_name"),
        "user_has_ar_effects": data["graphql"]["user"].get("has_ar_effects"),
        "user_has_clips": data["graphql"]["user"].get("has_clips"),
        "user_has_guides": data["graphql"]["user"].get("has_guides"),
        "user_has_channel": data["graphql"]["user"].get("has_channel"),
        "user_highlight_reel_count": data["graphql"]["user"].get("highlight_reel_count"),
        "user_is_private": data["graphql"]["user"].get("is_private"),
        "user_is_verified": data["graphql"]["user"].get("is_verified"),
        "user_profile_pic_url": data["graphql"]["user"].get("profile_pic_url"),
        "user_username": data["graphql"]["user"].get("username"),
        "user_media_count": data["graphql"]["user"]["edge_owner_to_timeline_media"].get("count"),
        "latest_media_id": data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"].get("id") if data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"] else None,
        "latest_media_shortcode": data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"].get("shortcode") if data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"] else None,
        "latest_media_height": data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["dimensions"].get("height") if data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"] else None,
        "latest_media_width": data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["dimensions"].get("width") if data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"] else None,
        "latest_media_display_url": data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"].get("display_url") if data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"] else None,
        "latest_media_comments": data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["edge_media_to_comment"].get("count") if data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"] else None,
        "latest_media_likes": data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["edge_liked_by"].get("count") if data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"] else None,
        "latest_media_timestamp": data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"].get("taken_at_timestamp") if data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"] else None,
    }
    return flat_data

# Output CSV file
output_csv = "compiled_output.csv"

# Gather all data and write to a single CSV file
with open(output_csv, mode='w', newline='') as cf:
    writer = None

    for i in range(701):
        json_file = f"{i}.json"
        if os.path.exists(json_file):
            flat_data = json_to_flat_dict(json_file)
            
            # Initialize CSV writer and write headers on the first write
            if writer is None:
                writer = csv.DictWriter(cf, fieldnames=flat_data.keys())
                writer.writeheader()
            
            writer.writerow(flat_data)
            print(f"Processed {json_file}")
        else:
            print(f"File {json_file} does not exist.")
