# Добавим в файл новый тест для создания поста и проверки его наличия:

import pytest
import requests
from ddt import ddt, data, unpack

@ddt
class TestPosts:

    @data(
        ("Post Title 1"),
        ("Post Title 2"),
        ("Post Title 3")
    )
    @unpack
    def test_check_post_title(self, auth_token, config, post_title):
        headers = {
            "X-Auth-Token": auth_token
        }
        response = requests.get(f"{config['site_url']}/api/posts", headers=headers, params={"owner": "notMe"})
        response.raise_for_status()
        
        posts = response.json()
        post_titles = [post['title'] for post in posts]
        
        assert post_title in post_titles, f"Post with title '{post_title}' not found."
    
    def test_create_and_check_post(self, auth_token, config):
        headers = {
            "X-Auth-Token": auth_token,
            "Content-Type": "application/json"
        }
        post_data = {
            "title": "Test Post",
            "description": "This is a test post",
            "content": "Test post content"
        }

        # Create a new post
        create_response = requests.post(f"{config['site_url']}/api/posts", headers=headers, json=post_data)
        create_response.raise_for_status()

        # Check if the post exists
        check_response = requests.get(f"{config['site_url']}/api/posts", headers=headers, params={"owner": "me"})
        check_response.raise_for_status()
        
        posts = check_response.json()
        post_descriptions = [post['description'] for post in posts]
        
        assert post_data['description'] in post_descriptions, f"Post with description '{post_data['description']}' not found."
