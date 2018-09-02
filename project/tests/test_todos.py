# standard library imports ...
from unittest.mock import patch

# Third-party imports...
from nose.tools import assert_is_not_none

# Local imports...
from project.services import get_todos

def test_getting_todos():
    mock_get_patcher = patch('project.services.requests.get')

    # start patching 'requests.get'
    mock_get = mock_get_patcher.start()

    # configure the mock to return a response with an OK status code
    mock_get.return_value.ok = True

    # call the service, which will send the request to the server
    response = get_todos()

    # stop patching 'requests.get'
    mock_get_patcher.stop()
     # if the request is sent successfully, then I expect a response to be returned
    assert_is_not_none(response)
    # with patch('project.services.requests.get') as mock_get:
    #     # configure the mock to return a response with an ok status code
    #     mock_get.return_value.ok = True

        # call the service, which will send a request to the server
        # response = get_todos()

    # if the request is sent successfully, then we exect a response to be returned.
#     assert_is_not_none(response)
# #
# @patch('project.services.requests.get')
# def test_getting_todos(mock_get):
#     # configure the mock to return a response with an OK status code.
#     mock_get.return_value.ok = True
#
#     # call the service, which will send a request to the server
#     response = get_todos()
#
#     # if the reequest is sent successfully, then we expect a response to be returned
#     assert_is_not_none(response)
# #
# # def test_request_response():
# #     # Call the service, which will send a request to the server.
# #     response = get_todos()
# #
# #     # If the request is sent successfully, then I expect a response to be returned.
# #     assert_is_not_none(response)
