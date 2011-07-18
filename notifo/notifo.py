from trac.core import *
from trac.ticket.api import ITicketChangeListener
from notifosvc import *
import string

class NotifoPlugin(Component):
    implements(ITicketChangeListener)

    def __init__(self):
        self.nuser = self.config['notifo'].get('username')
        self.nkey = self.config['notifo'].get('key')

    def ticket_created(self, ticket):
        """Called when a ticket is created."""
        msg = "Ticket: %d [%s %s] Created by %s: %s " % (
                ticket.id, ticket['priority'], ticket['type'], 
                ticket['reporter'], ticket['summary'])
        svc = NotifoSvc(self.nuser,self.nkey)
        response = svc.sendNotification({
            'to':self.nuser,
            'msg':msg
            })

    def ticket_changed(self, ticket, comment, author, old_values):
        """Called when a ticket is modified."""
        msg = "Ticket: %d [%s %s] %s by %s: %s " % (
                ticket.id, ticket['priority'], ticket['type'], 
                string.capwords(ticket['status']), author, comment)
        svc = NotifoSvc(self.nuser,self.nkey)
        response = svc.sendNotification({
            'to':self.nuser,
            'msg':msg
            })

    def ticket_deleted(self, ticket):
        """Called when a ticket is deleted."""
        msg = "Ticket: %d [%s %s] Deleted %s: %s " % (
                ticket.id, ticket['priority'], ticket['type'], 
                ticket['owner'], ticket['summary'])
        svc = NotifoSvc(self.nuser,self.nkey)
        response = svc.sendNotification({
            'to':self.nuser,
            'msg':msg
            })
