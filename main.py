# @Project : token
# @Time : 2022/12/23 10:39
# @Author : Alan
# @File : main.py
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from oauth import LoginOauth
from setting import PROJECTS

app = FastAPI()


class ReqTokenData(BaseModel):
    project: str
    env: str
    username: str
    password: str
    is_cache: Optional[bool] = True


def Response(data=None, message="success", success=True):
    response = dict()
    response['message'] = message
    response['success'] = success
    response['data'] = data

    return response


@app.post("/api/token")
def oauth_token(data: ReqTokenData):
    data_dict = data.dict()
    if data_dict['project'] not in PROJECTS:
        return Response(message=f"项目不存在, 当前项目{PROJECTS}", success=False)
    oauth = LoginOauth(**data.dict())
    token = oauth.get_token()
    if token:
        return Response(data={'token': token})
    return Response(message="获取token失败", success=False)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=6666, reload=True)