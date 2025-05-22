from celery.schedules import crontab

# Celery Beat Schedule (defined in-code)
CELERY_BEAT_SCHEDULE = {
    "generate-access-token-for-server-use-every-5-minutes": {
        "task": "posts.tasks.generate_access_token",
        "schedule": crontab(minute="*/5"),
        "options": {
            "expires": 300,  # 300 - expires after 5 minutes
        },
    },
}
