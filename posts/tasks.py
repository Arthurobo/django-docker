from celery import shared_task
import time


@shared_task
def add(post_id):
    print("Starting task!")
    print(f"Adding {post_id}")
    return post_id


@shared_task
def generate_access_token():
    print("Generating access token!")
    return "Access token generated!"