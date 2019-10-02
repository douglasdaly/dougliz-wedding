# -*- coding: utf-8 -*-
"""
Email-related utilities.
"""
import logging
import os
import typing as tp

import emails
from emails.template import JinjaTemplate

from app.core import config


def send_email(
    email_to: str,
    subject_template: str = "",
    html_template: str = "",
    environment: tp.Mapping = {}
) -> None:
    """Sends an email with the given parameters.

    Parameters
    ----------
    email_to : str
        The email address to send the email to.
    subject_template : str, optional
        The subject line template string to use.
    html_template : str, optional
        The email body template string to use.
    environment : Mapping, optional
        The environment variables to use in rendering the message.

    """
    if not config.EMAILS_ENABLED:
        logging.warn("Emails are not enabled")
        return

    message = emails.Message(
        subject=JinjaTemplate(subject_template),
        html=JinjaTemplate(html_template),
        mail_from=(config.EMAILS_FROM_NAME, config.EMAILS_FROM_EMAIL)
    )
    smtp_options = dict(host=config.SMTP_HOST, port=config.SMTP_PORT)
    if config.SMTP_TLS:
        smtp_options["tls"] = True
    if config.SMTP_USER:
        smtp_options["user"] = config.SMTP_USER
    if config.SMTP_PASSWORD:
        smtp_options["password"] = config.SMTP_PASSWORD
    response = message.send(to=email_to, render=environment, smtp=smtp_options)
    logging.info(f"Email send result: {response}")
    return


def send_test_email(email_to: str) -> None:
    """Sends a test email to the given address.

    Parameters
    ----------
    email_to : str
        The email address to send the test email to.

    """
    subject = f"{config.PROJECT_NAME} - Test Email"
    template_path = os.path.abspath(os.path.join(
        config.EMAILS_TEMPLATE_DIR, "test_email.html"
    ))
    with open(template_path) as fin:
        template_str = fin.read()
    return send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        environment={
            "project_name": config.PROJECT_NAME,
            "email": email_to,
        }
    )


def send_password_reset_email(email_to: str, email: str, token: str) -> None:
    """Sends the password reset email.

    Parameters
    ----------
    email_to : str
        The email address to send the password reset email to.
    email : str
        The user's email address (used as a username).
    token : str
        The recovery token to send.

    """
    subject = f"{config.PROJECT_NAME} - Password Recovery for {email}"
    template_path = os.path.abspath(os.path.join(
        config.EMAILS_TEMPLATE_DIR, "password_reset.html"
    ))
    with open(template_path) as fin:
        template_str = fin.read()
    if hasattr(token, "decode"):
        use_token = token.decode()
    else:
        use_token = token
    link = f"{config.SERVER_HOST}/reset-password?token={use_token}"
    return send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        environment={
            "project_name": config.PROJECT_NAME,
            "username": email,
            "email": email_to,
            "valid_hours": config.EMAIL_RESET_TOKEN_EXPIRES_HOURS,
            "link": link,
        }
    )


def send_new_account_email(
    email_to: str,
    username: str,
    password: str
) -> None:
    """Sends a new account created email.

    Parameters
    ----------
    email_to : str
        The email address to send the email to.
    username : str
        The username to use for the newly created account.
    password : str
        The initial password to use for the newly created account.

    """
    subject = f"{config.PROJECT_NAME} - New account for {username}"
    template_path = os.path.abspath(os.path.join(
        config.EMAILS_TEMPLATE_DIR, "new_account.html"
    ))
    with open(template_path) as fin:
        template_str = fin.read()
    return send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        environment={
            "project_name": config.PROJECT_NAME,
            "username": username,
            "password": password,
            "email": email_to,
            "link": config.SERVER_HOST,
        }
    )
