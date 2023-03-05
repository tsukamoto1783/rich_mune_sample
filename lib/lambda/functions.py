import urllib.request
import json
import boto3
import traceback

# ディレクトリ内のファイルimport
import const

# クエリパラメーターの取得
def check_query_param(param: dict, query_param_name: str):
    query_param_value = None

    # クエリパラメータのbool文字列をbool値に変換
    # 不正のパラメーターだった場合はNoneを返す
    try:
        if param[query_param_name].lower() == "true":
            query_param_value = True
        elif param[query_param_name].lower() == "false":
            query_param_value = False
        else:
            print(query_param_name)
            None
        return query_param_value
    except e:
        print(e)
        return query_param_value


# レスポンスjsonデータの成形
def creating_response_date(process_name: str, reslut: bool = True, status_code: int = 200):
    response_date = const.RESPONSE_DEFALUT_DATE
    if reslut:
        response_date["body"] = "Ruch Menu: " + process_name +" Success"
    else:
        response_date["body"] = "Ruch Menu: " + process_name +" error"

    if status_code != 200:
        response_date["statusCode"] = status_code

    return response_date


# リッチメニュ作成
def create_rich_menu():
    process_name = "create"
    create_reslut = None
    url = "https://api.line.me/v2/bot/richmenu"
    headers = {
        "Authorization": "Bearer " + const.ACCESS_TOKEN,
        "Content-Type": "application/json"
    }

    # API Call
    request = urllib.request.Request(url, headers=headers, data=const.RICH_MENU_DATA.encode("utf-8"), method="POST")

    try:
        with urllib.request.urlopen(request) as response:
            create_reslut = creating_response_date(process_name)
            create_reslut = dict(create_reslut, **json.loads(response.read().decode("utf-8")))
            return create_reslut

    except urllib.error.HTTPError as e:
        print(e.read())
        create_reslut = creating_response_date(process_name, False, e.code)
        return create_reslut


# リッチメニュに画像をアップロード
def upload_rich_menu_image(rich_menu_id: str, is_bool: bool):
    process_name = "upload"
    upload_reslut = None
    url = f"https://api-data.line.me/v2/bot/richmenu/{rich_menu_id}/content"
    headers = {
        "Authorization": "Bearer " + const.ACCESS_TOKEN,
        "Content-Type": "image/png"
    }
    # S3から画像データを取得
    image_data = get_img_from_s3(is_bool)
    if type(image_data) == dict:
        return image_data

    # API Call
    request = urllib.request.Request(url, headers=headers, data=image_data, method='POST')

    try:
        with urllib.request.urlopen(request) as response:
            upload_reslut = creating_response_date(process_name)
            return upload_reslut

    except urllib.error.HTTPError as e:
        print(e.read())
        upload_reslut = creating_response_date(process_name, False, e.code)
        return upload_reslut


# S3から画像データを取得
def get_img_from_s3(is_bool: bool):
    get_obj_response_date = None
    object_name = ''

    # 引数のbool値で取得する画像データを切り替え
    if is_bool:
        object_name = const.RICH_MENU_IMAGE1
    else:
        object_name = const.RICH_MENU_IMAGE2

    s3 = boto3.client('s3')

    # S3から画像データ取得
    try:
        obj = s3.get_object(Bucket=const.BUCKET_NAME, Key=object_name)
        body = obj['Body'].read()
        return body
    except:
        get_obj_response_date = const.RESPONSE_DEFALUT_DATE
        get_obj_response_date["body"] = "S3からの画像取得に失敗"
        get_obj_response_date["statusCode"] = 400
        return get_obj_response_date


# デフォルトのリッチメニュを設定
def set_default_rich_menu(rich_menu_id: str):
    set_reslut = None
    process_name = "set"
    url = f"https://api.line.me/v2/bot/user/all/richmenu/{rich_menu_id}"
    headers = {
        "Authorization": "Bearer " + const.ACCESS_TOKEN
    }

    # API Call
    request = urllib.request.Request(url, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(request) as response:
            set_reslut = creating_response_date(process_name)
            return set_reslut

    except urllib.error.HTTPError as e:
        print(e.read())
        set_reslut = creating_response_date(process_name, False, e.code)
        return set_reslut
