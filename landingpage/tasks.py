from celery.decorators import task
from celery.utils.log import get_task_logger

from landingpage.emails import send_welcome_email

logger = get_task_logger(__name__)


@task(name="send_welcome_email_task")
def send_welcome_email_task(email, message):
    """sends an email when subscription form is filled successfully"""
    logger.info("Sent welcome email")
    return send_welcome_email(email, message)
