# ディレクトリ内のファイルimport
import const
import functions

def lambda_handler(event, context):
    param = event["queryStringParameters"]

    # クエリパラメーターの取得
    param_check_result = functions.check_query_param(param, const.QUERY_PARAM_NAME)
    if param_check_result == None:
        check_query_param_error = const.RESPONSE_DEFALUT_DATE
        check_query_param_error["body"] = "クエリパラメーターが不正です"
        check_query_param_error["statusCode"] = 400
        return check_query_param_error

    is_bool = param_check_result

    # リッチメニュ作成
    create_result = functions.create_rich_menu()
    print(create_result)
    if create_result["statusCode"] != 200:
        return create_result

    # リッチメニュID取得
    rich_menu_id = create_result["richMenuId"]

    # リッチメニュに画像をアップロード
    upload_result = functions.upload_rich_menu_image(rich_menu_id, is_bool)
    print(upload_result)
    if upload_result['statusCode'] != 200:
        return upload_result

    # デフォルトのリッチメニュを設定
    set_default_result = functions.set_default_rich_menu(rich_menu_id)
    print(set_default_result)
    if set_default_result['statusCode'] != 200:
        return set_default_result

    return functions.creating_response_date("deploy")
