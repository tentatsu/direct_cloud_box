# direct_cloud_box tool
DirectCloudBOXのAPIを利用するためのツールです。

## 使い方
direct_cloud_box/api.pyのインスタンス作成時に、
サービス、サービスキー、企業コード、ユーザID、パスワードを渡すことで
API利用を用意にします。

```python
from direct_cloud_box.api import directCloudBox
import os
from os.path import join, dirname
from dotenv import load_dotenv

user_api = directCloudBox(
    USER_SERVICE,
    USER_SERVICE_KEY,
    COMPANY_CODE,
    USER_ID,
    PASSWORD
    )
try:
    print(user_api.folderCreate("test", "1"))
    print(user_api.folderGet(""))
    print(user_api.folderGet("MyBOX"))
    print(user_api.folderGet("SharedBOX"))
finally:
    user_api.tokenExpire()
```

# VSCodeの設定
* ./.vscode/settings.jsonに追加
  * ※Python言語サーバーがPylanceのとき。
    * https://qiita.com/keisukesato-ac/items/6213925bb167c25cc37c
```
{
    "python.analysis.extraPaths": [
        "./direct_cloud_box/lib/python3.9/site-packages"
    ], 
}
```

## venv 作成

```
$ cd ~/
$ python3 -m venv direct_cloud_box
```

## Activate

```
cd direct_cloud_box
$ source bin/activate
```

## deactivate

```
(direct_cloud_box) $ deactivate
```


## pip install

```
(direct_cloud_box) $ pip3 install -r requirements.txt
```

## execute

```
(direct_cloud_box) $ 

