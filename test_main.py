import logging

from flask import url_for

def test_app(client, config):
    res = client.get('/')
    logging.info(config)
    assert res.status_code == 200
