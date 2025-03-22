import pytest
import requests


my_url_for_create = 'https://jsonplaceholder.typicode.com/posts'
my_url_for_changes = 'https://jsonplaceholder.typicode.com/posts/95'
my_headers = {
    "Content-type": "application/json; charset=UTF-8"
}
my_payload = {
    "userId": 1,
    "title": "titleTest123",
    "body": "random text in body"
}

my_payload_change = {
    "userId": 1,
    "title": "titleTest123999",
    "body": "random text in body1234567"
}
my_payload_delete = {}