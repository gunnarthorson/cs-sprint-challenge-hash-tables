#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    source_ticket = {i.source:i for i in tickets}

    route = []

    this_ticket = source_ticket["NONE"]
    while this_ticket.destination != "NONE":
        route.append(this_ticket.destination)
        this_ticket = source_ticket[this_ticket.destination]

    route.append(this_ticket.destination)
    return route
