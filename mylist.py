class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        pass

    def __str__(self):
        return str(self.data)


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.temp = None
        pass

    def __iter__(self):
        self.temp = self.head
        return self

    def __next__(self):
        if self.temp is None:
            raise StopIteration
        ret = self.temp
        self.temp = self.temp.next
        return ret

    def append(self, data):
        if self.tail is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        pass

    def length(self):
        count = 0
        temp = self.head
        while(temp is not None):
            count += 1
            temp = temp.next
        return count
        pass

    def __getitem__(self, key):
        temp = self.head
        for i in range(0, key):
            temp = temp.next
            if temp is None:
                raise Exception("List index out of bounds")
        return temp.data

    def __setitem__(self, key, value):
        temp = self.head
        for i in range(0, key):
            temp = temp.next
            if temp is None:
                raise Exception("List index out of bounds")
        temp.data = value

    def pop_back(self):
        temp = self.head
        if self.head is None:
            return
        else:
            while(temp.next is not self.tail):
                temp = temp.next
            self.tail = temp
            del self.tail.next
            self.tail.next = None
        pass

    def pop_front(self):
        temp = self.head
        self.head = self.head.next
        del temp
        pass

    def remove(self, data):
        temp = self.head

        if temp.data == data:
            self.pop_front()
            return

        if self.tail.data == data:
            self.pop_back()
            return

        while(temp.next is not self.tail):
            if temp.next.data == data:
                connect = temp.next.next
                del temp.next
                temp.next = connect
                return
            temp = temp.next


if __name__ == "__main__":
    mylist = LinkedList()
    mylist.append(5342)
    mylist.append(23)
    mylist.remove(23)
    print(mylist.length())
    print(mylist[0])
    mylist[0] = 2452
    print(mylist[0])
    for i in mylist:
        print(i)
