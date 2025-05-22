from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from . import celerybeat

# setting the Django settings module.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
app = Celery("blog")

# Load task modules from all registered Django app configs.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Configure Celery Beat schedule
app.conf.beat_schedule = celerybeat.CELERY_BEAT_SCHEDULE

# Explicitly include all tasks
app.autodiscover_tasks(["posts"])

# Run tasks on worker startup
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Run generate_access_token immediately
    sender.send_task('posts.tasks.generate_access_token')

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")