# -*- coding: utf-8 -*-
import os
from datetime import timedelta
from dotenv import dotenv_values

class LocalConfig(object):
    IS_PROD_ENV = True

    ################################################
    # Validate if environment running
    # is local or is a Google Cloud Project
    ################################################
    if (
        "gunicorn" in os.getenv("SERVER_SOFTWARE", "")
        and os.getenv("GOOGLE_CLOUD_PROJECT") == "apolo11-prod"
    ):
        current_branch = "master"

    elif (
        "gunicorn" in os.getenv("SERVER_SOFTWARE", "")
        and os.getenv("GOOGLE_CLOUD_PROJECT") == "apolo11-dev"
    ):
        current_branch = "development"

    else:
        current_branch = "development"  # 'master'

    ################################################
    # Prod env variables
    # Only for main and master origin branch
    ################################################
    if (
        current_branch == "main"
        or current_branch == "master"
        or "hotfix" in current_branch
        or "release" in current_branch
    ):
        config = {
            **dotenv_values("app/config/common.env"),
        }
        IS_PROD_ENV = True

    ################################################
    # Dev env variables
    # any branch different to master or main origin
    ################################################
    else:  # current_branch == "development"
        config = {
            **dotenv_values("app/config/common.env"),
        }
        IS_PROD_ENV = False

    ###########################################################################
    # Auth
    ###########################################################################
    # JWT
    TOKEN_CONTENT = config["TOKEN_CONTENT"]
    PASSWORD_SYMBOLS_ALLOWED = config["PASSWORD_SYMBOLS_ALLOWED"]
    
    ############################################################################
    # MYSQL
    ############################################################################
    SQL_USERNAME=config["SQL_USERNAME"]
    SQL_PASSWORD=config["SQL_PASSWORD"]
    SQL_SERVER=config["SQL_SERVER"]
    SQL_DATABASE=config["SQL_DATABASE"]
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{SQL_USERNAME}:{SQL_PASSWORD}@{SQL_SERVER}/{SQL_DATABASE}?unix_socket=/cloudsql/apolo11-dev:us-central1:apolo11-developer-db&charset=utf8'

    #########################
    # web service log
    #########################
    WS_PRIVATE_KEY_MORFEO = config["WS_PRIVATE_KEY_MORFEO"]

    ############################################################################
    # Attachments
    ############################################################################
    ASSISTANCE_PROVIDER_BILL_ATTACHMENT_DIR = 'assistance_provider_bill_attachment'
    TYPE_FINDING_ATTACHMENT_DIR = 'assistance_finding'
    ASSISTANCE_WALLET_ASSETS_DIR = 'assistance_wallet_assets'
    ASSISTANCE_PRODUCT_ATTACHMENT_DIR = 'assistance_product_attachment'
    ASSISTANCE_PLAN_ATTACHMENT_DIR = 'assistance_plan_attachment'

    ############################################################################
    # Others
    ############################################################################
    GAE_APP_ID = config["GAE_APP_ID"]

    ############################################################################
    # Common configuration
    ############################################################################
    SYSTEM_URL = config["SYSTEM_URL"]

    VPS_APOLO_URL = config["VPS_APOLO_URL"]

    # web service timeout(secods)
    WEB_SERVICE_TIMEOUT = 300

    ############################################################################
    # GOOGLE CLOUD STORAGE
    ############################################################################
    BUCKET_NAME = config["BUCKET_NAME"]