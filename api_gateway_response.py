import json
import unittest


def build_ok_response(body):
    return _build_response(200, body)


def build_bad_request_response(*messages):
    return _build_error_response(400, messages)


def build_not_found_response(*messages):
    return _build_error_response(404, messages)


def _build_response(status_code, body):
    return {
        'statusCode': status_code,
        'headers': {},
        'body': json.dumps(body),
        'isBase64Encoded': False,
    }


def _build_error_response(status_code, messages):
    return _build_response(status_code, {'messages': messages})


class Test(unittest.TestCase):

    def test_build_ok_response(self):
        self.assertEqual({
            'statusCode': 200,
            'headers': {},
            'body': '{"key": "value"}',
            'isBase64Encoded': False,
        }, build_ok_response({'key': 'value'}))
        self.assertEqual({
            'statusCode': 200,
            'headers': {},
            'body': 'null',
            'isBase64Encoded': False,
        }, build_ok_response(None))

    def test_build_bad_request_response(self):
        self.assertEqual({
            'statusCode': 400,
            'headers': {},
            'body': '{"messages": ["message"]}',
            'isBase64Encoded': False,
        }, build_bad_request_response('message'))
