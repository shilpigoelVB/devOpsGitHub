from typing import Optional

from fastapi import FastAPI

import os

app = FastAPI()


@app.get("/")
def read_root():
    version = os.getenv('image_url', default = 'bmhcpjocbku8/python_fastapi_app:')
    return {"Message": "With ❤️ from OCI DevOps via GitHubLab Actions","Version":version}
