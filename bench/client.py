import logging.config
import time

import requests

logging.config.fileConfig('../logging.ini')
logger = logging.getLogger('bench_client')

while True:
    # ms
    cli_sent = int(time.time() * 1000)
    ret = requests.get(url='http://127.0.0.1:9999', params={
        'cli_sent': cli_sent,
    })
    cli_recv = int(time.time() * 1000)

    data = ret.json()
    server_recv = int(data['server_recv'])
    server_resp = int(data['server_resp'])

    point = {
        'cli_sent': cli_sent,
        'server_recv': server_recv,
        'server_resp': server_resp,
        'cli_recv': cli_recv,
        'total_duration': cli_recv - cli_sent,
        'server_duration': server_resp - server_recv,
        'cli_to_server_duration': server_recv - cli_sent,
        'server_to_cli_duration': cli_recv - server_resp,
    }
    logger.info(point)
    time.sleep(0.5)
