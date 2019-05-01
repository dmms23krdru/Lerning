#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
#import smtplib
from smtplib import SMTP_SSL as SMTP
import sys
from configparser import ConfigParser
 
 
def send_email(subject, body_text, to_emails, cc_emails, bcc_emails):
    """
    Send an email
    """
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "email.ini")
    
    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        print("Config not found! Exiting!")
        sys.exit(1)
 
    host = cfg.get("smtp", "server")
    from_addr = cfg.get("smtp", "from_addr")
    loggin = cfg.get("smtp", "login")
    passw = cfg.get("smtp", "pass")
    
    BODY = "\r\n".join((
        "From: %s" % from_addr,
        "To: %s" % ', '.join(to_emails),
        "CC: %s" % ', '.join(cc_emails),
        "BCC: %s" % ', '.join(bcc_emails),
        "Subject: %s" % subject ,
        "",
        body_text
    ))
    
    emails = to_emails
    if cc_emails:
        emails = emails + cc_emails
        if bcc_emails:
            emails = emails + bcc_emails
    

    server = SMTP(host, 465)
    server.set_debuglevel(True)
    server.login(loggin, passw)
    server.sendmail(from_addr, emails, BODY)
    server.quit()
 
 
if __name__ == "__main__":
    emails = ["dim@23krd.ru"]
    cc_emails = []
    bcc_emails = []
    subject = "Test email from Python"
    body_text = "Python rules them all!"
    send_email(subject, body_text, emails, cc_emails, bcc_emails)