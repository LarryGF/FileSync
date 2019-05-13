from fastapi import Cookie, FastAPI
# from authentication import authenticate
# from link_account import link_account_facebook
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get('/authenticate')
async def log_in(user: str, password: str):
    result = await authenticate(user, password)
    return result


@app.get('/link_account')
async def link_fb_account(user: str, password: str):
    result = await link_account_facebook(user, password)
    return result
