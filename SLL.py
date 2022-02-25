class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head=self.head
        new_node.next = current_head
        self.head=new_node
        return self
    def add_to_back(self, val):
        if self.head == None:	# if the list is empty
            self.add_to_front(val)	# run the add_to_front method
            return self	# let's make sure the rest of this function doesn't happen if we add to the front
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node	# increment the runner to the next node in the list
        return self# return self to allow for chaining

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next 	# set the runner to its neighbor
        return self# once the loop is done, return self to allow for chaining

class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

my_list = SList()	# create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_front("Test").add_to_back("fun!").print_values()
# output should be:
# Linked lists
# are
# fun!

