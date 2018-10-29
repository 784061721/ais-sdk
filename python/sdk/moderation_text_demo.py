# -*- coding:utf-8 -*-
from ais_sdk.gettoken import get_token
from ais_sdk.moderation_text import moderation_text
from ais_sdk.moderation_text import moderation_text_aksk
if __name__ == '__main__':
    #
    # access moderation text enhance,posy data by token
    #
    user_name = '******'
    password = '******'
    account_name = '******'  # the same as user_name in commonly use

    token = get_token(user_name, password, account_name)

    # call interface use the text
    result = moderation_text(token, '666666luo聊请+110亚砷酸钾六位qq，fuck666666666666666', 'content')
    print result

    #
    # access moderation text enhance,posy data by ak,sk
    #
    app_key = "*************"
    app_secret = "************"

    # call interface use the text
    result = moderation_text_aksk(app_key, app_secret, '666666luo聊请+110亚砷酸钾六位qq，fuck666666666666666', 'content')
    print result