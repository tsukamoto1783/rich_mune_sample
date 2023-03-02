import os

QUERY_PARAM_NAME = {クエリパラメータに指定するKey名}

RESPONSE_DEFALUT_DATE = {
    "isBase64Encoded": False,
    "statusCode": 200,
    "body": ""
}

ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

RICH_MENU_DATA = """
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
