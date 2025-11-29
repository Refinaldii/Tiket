from datetime import datetime, timedelta
import uuid

TICKETS = []
COMMENTS = {}

def create_ticket(data):
    ticket_id = str(uuid.uuid4())[:8]
    data["id"] = ticket_id
    data["created_at"] = datetime.utcnow()
    data["due_at"] = datetime.utcnow() + timedelta(hours=24)
    data["status"] = "New"
    TICKETS.append(data)
    COMMENTS[ticket_id] = []
    return ticket_id

def list_tickets():
    return TICKETS

def get_ticket(ticket_id):
    for t in TICKETS:
        if t["id"] == ticket_id:
            return t
    return None

def add_comment(ticket_id, author, text):
    COMMENTS.setdefault(ticket_id, [])
    COMMENTS[ticket_id].append({
        "at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        "author": author,
        "text": text
    })

