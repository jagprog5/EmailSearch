#!/usr/bin/env python3

from soupsieve import match
from utils import get_config, extract
from getpass import getpass
import imaplib, email
from tika import parser

if __name__ == "__main__":
    config = get_config()
    mail = imaplib.IMAP4_SSL(config["host"], config["port"])
    mail.login(config["email"], getpass("password: "))
    mail.select('"' + config["mailbox"] + '"')
    typ, data = mail.search(None, 'ALL')
    if typ != "OK":
        print("Error searching mailbox: " + typ)
        exit()
    mail_ids = data[0]
    id_list = mail_ids.split()
    patterns = config["patterns"]

    # Store all the matches
    matches = []

    for id in id_list:
        typ, data = mail.fetch(id, '(RFC822)')
        if typ != "OK":
            print("Error getting email: " + typ)
            exit()
        email_str = data[0][1].decode('utf-8')
        # look through the raw text of the entire email
        raw_matches = extract(patterns, email_str)
        for r in raw_matches:
            if r not in matches:
                matches.append(r)
        
        # apply secret sauce to decode attachments
        # and search through the raw text of those attachments
        email_message = email.message_from_string(email_str)
        for p in email_message.get_payload():
            # application includes pdfs, odt, docx, etc.
            if p.get_content_maintype() != "application":
                continue
            if p.get('Content-Disposition') is None:
                continue
            parsed = parser.from_buffer(p.get_payload(decode=True))
            data = parsed["content"]
            data_matches = extract(patterns, data)
            for d in data_matches:
                if d not in matches:
                    matches.append(d)
            
    for m in matches:
        print(m)
    