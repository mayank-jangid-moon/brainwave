import csv

# JSON data
data = {
    "logging_page_id": "profilePage_44850258325",
    "show_suggested_profiles": False,
    "show_follow_dialog": False,
    "graphql": {
        "user": {
            "biography": "",
            "blocked_by_viewer": False,
            "restricted_by_viewer": False,
            "country_block": False,
            "external_url": None,
            "external_url_linkshimmed": None,
            "edge_followed_by": {"count": 1027},
            "fbid": "17841444709776282",
            "followed_by_viewer": False,
            "edge_follow": {"count": 1932},
            "follows_viewer": True,
            "full_name": "a.a.ghasami20",
            "has_ar_effects": False,
            "has_clips": False,
            "has_guides": False,
            "has_channel": False,
            "has_blocked_viewer": False,
            "highlight_reel_count": 1,
            "has_requested_viewer": False,
            "id": "44850258325",
            "is_business_account": False,
            "is_joined_recently": False,
            "business_category_name": None,
            "overall_category_name": None,
            "category_enum": None,
            "category_name": None,
            "is_private": False,
            "is_verified": False,
            "edge_mutual_followed_by": {"count": 0, "edges": []},
            "profile_pic_url": "https://scontent-ort2-1.cdninstagram.com/v/t51.2885-19/s150x150/132200586_1279222765810706_8483593670365738739_n.jpg?_nc_ht=scontent-ort2-1.cdninstagram.com&amp;_nc_ohc=F7SADorNqBYAX9SYGoi&amp;tp=1&amp;oh=8794759649b605e64b613510d3f2cc7f&amp;oe=60214E5B",
            "profile_pic_url_hd": "https://scontent-ort2-1.cdninstagram.com/v/t51.2885-19/s320x320/132200586_1279222765810706_8483593670365738739_n.jpg?_nc_ht=scontent-ort2-1.cdninstagram.com&amp;_nc_ohc=F7SADorNqBYAX9SYGoi&amp;tp=1&amp;oh=3f3f40135716fc7c82a0822e8394dbda&amp;oe=601EB74E",
            "requested_by_viewer": False,
            "should_show_category": False,
            "username": "a.a.ghasami20",
            "connected_fb_page": None,
            "edge_felix_video_timeline": {"count": 0, "page_info": {"has_next_page": False, "end_cursor": None}, "edges": []},
            "edge_owner_to_timeline_media": {
                "count": 1,
                "page_info": {"has_next_page": False, "end_cursor": None},
                "edges": [
                    {
                        "node": {
                            "id": "2470516445352912470",
                            "shortcode": "CJJCZ4hBWZW",
                            "dimensions": {"height": 1080, "width": 1080},
                            "display_url": "https://scontent-ort2-1.cdninstagram.com/v/t51.2885-15/e35/132642373_239194574302075_5599471643144512073_n.jpg?_nc_ht=scontent-ort2-1.cdninstagram.com&amp;_nc_cat=107&amp;_nc_ohc=zHW3-DG-CEQAX8ii5_R&amp;tp=1&amp;oh=de79dde294ac60c77ab70758ec6dd86c&amp;oe=60217EAC",
                            "is_video": False,
                            "edge_media_to_comment": {"count": 1},
                            "taken_at_timestamp": 1608728531,
                            "edge_liked_by": {"count": 122},
                        }
                    }
                ]
            },
        }
    },
}

# CSV filename
csv_filename = "/mnt/data/instagram_profile.csv"

# Flattened data for CSV
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
    "latest_media_id": data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"].get("id"),
    "latest_media_shortcode": data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"].get("shortcode"),
    "latest_media_height": data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["dimensions"].get("height"),
    "latest_media_width": data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["dimensions"].get("width"),
    "latest_media_display_url": data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"].get("display_url"),
    "latest_media_comments": data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["edge_media_to_comment"].get("count"),
    "latest_media_likes": data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["edge_liked_by"].get("count"),
    "latest_media_timestamp": data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"].get("taken_at_timestamp"),
}

# Writing data to CSV
with open(csv_filename, mode='w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=flat_data.keys())
    writer.writeheader()
    writer.writerow(flat_data)

csv_filename
