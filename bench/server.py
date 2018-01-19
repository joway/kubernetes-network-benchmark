import time

from lemon.app import Lemon
from lemon.context import Context


async def handler(ctx: Context):
    server_recv = int(time.time() * 1000)
    # do something
    server_resp = int(time.time() * 1000)

    ctx.body = {
        'server_recv': server_recv,
        'server_resp': server_resp,
    }


app = Lemon()

app.use(handler)

app.listen(port=9999)
