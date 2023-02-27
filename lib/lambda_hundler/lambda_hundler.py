import urllib.request
import json
import os
import boto3
import traceback

access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
rich_menu_data = """
{
    "size": {
        "width": 2500,
        "height": 1686
    },
    "selected": false,
    "name": "richmenu name",
    "chatBarText": "tap here",
    "areas": [
        {
            "bounds": {
                "x": 0,
                "y": 0,
                "width": 2500,
                "height": 1686
            },
            "action": {
                "type": "postback",
                "data": "action=buy&itemid=123"
            }
        }
    ]
}
"""

def lambda_handler(event, context):
    # リッチメニュ作成
    create_result = create_rich_menu()
    if create_result == None:
        return "Ruch Menu: creating error"

    # リッチメニュID取得
    rich_menu_id = create_result["richMenuId"]

    # リッチメニュに画像をアップロード
    upload_result = upload_rich_menu_image(rich_menu_id)
    if upload_result == None:
        return "Rich Menu: uploading error"
    print(upload_result)

    # デフォルトのリッチメニュを設定
    set_default_result = set_default_rich_menu(rich_menu_id)
    if set_default_result == None:
        return "Rich Menu: defalut setting error"
    else:
        print(set_default_result)
        return "Rich Menu: deploy success"

# リッチメニュ作成
def create_rich_menu():
    url = "https://api.line.me/v2/bot/richmenu"
    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }

    # URL Open
    request = urllib.request.Request(url, headers=headers, data=rich_menu_data.encode("utf-8"), method="POST")

    try:
        with urllib.request.urlopen(request) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())
        return None


# リッチメニュに画像をアップロード
def upload_rich_menu_image(rich_menu_id):
    url = f"https://api-data.line.me/v2/bot/richmenu/{rich_menu_id}/content"
    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "image/png"
    }
    # S3から画像データを取得
    image_data = get_img_from_s3()
    if image_data == None:
        return None

    # URL Open
    request = urllib.request.Request(url, headers=headers, data=image_data, method='POST')

    try:
        with urllib.request.urlopen(request) as response:
            return response.read().decode("utf-8")

    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())
        return None


# S3から画像データを取得
def get_img_from_s3():
    BUCKET_NAME = {s3のバケット名}
    OBJECT_NAME = {オブジェクト名(画像ファイル名)}
    s3 = boto3.client('s3')

    # S3から画像データ取得
    try:
        obj = s3.get_object(Bucket=BUCKET_NAME, Key=OBJECT_NAME)
        body = obj['Body'].read()
        return body
    except:
        traceback.print_exc()
        return None


# デフォルトのリッチメニュを設定
def set_default_rich_menu(rich_menu_id):
    url = f"https://api.line.me/v2/bot/user/all/richmenu/{rich_menu_id}"
    headers = {
        "Authorization": "Bearer " + access_token
    }

    # URL Open
    request = urllib.request.Request(url, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(request) as response:
            return json.loads(response.read().decode("utf-8"))

    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())
        return None
