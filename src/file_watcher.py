from datetime import datetime
from src.api.whatsappAPI import whatsAppMsgAPI
from src.api.gsheetapi import *

# -----------------------Time---------------------------------------------#
t = datetime.now()
st = t.strftime('%H:%M:%S')
# ------------------------------------------------------------------------#



def file_handling(event):
    lines = 0
    f = open(event.src_path, 'r')
    for i in f:
        lines += 1
    return lines


def on_created(event):
    total_lines = file_handling(event)
    t = datetime.now()            # Time has been once again initiated to get updated time for message and sheets
    ct = t.strftime('%H:%M:%S')
    msg = f"{event.src_path} has been created! at {ct}"
    whatsAppMsgAPI(msg)
    worksheet.append_row([st, event.src_path, total_lines, ct, 'accepted'])


def on_deleted(event):
    t = datetime.now()
    ct = t.strftime('%H:%M:%S')
    msg = f"Someone deleted {event.src_path}! at {ct}"
    whatsAppMsgAPI(msg)


def on_modified(event):
    t = datetime.now()
    ct = t.strftime('%H:%M:%S')
    msg = f"{event.src_path} has been modified at {ct}"
    whatsAppMsgAPI(msg)


def on_moved(event):
    t = datetime.now()
    ct = t.strftime('%H:%M:%S')
    msg = f"someone moved {event.src_path} to {event.dest_path} at {ct}"
    whatsAppMsgAPI(msg)
