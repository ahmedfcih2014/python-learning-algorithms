from collections import deque

class Person:
    def __init__(self ,name ,job):
        self.name = name
        self.job = job

    def im_mango_seller(self):
        return self.job == 'Mango Seller'

def search(name):
    try :
        search_queue = deque(graph[name])
    except :
        print "Can`t init Queue"
        return False
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person.name in searched:
            if person.im_mango_seller():
                print 'visited : ' + ",".join(searched)
                print person.name + " is a mango seller!"
                return True
            else:
                try:
                    search_queue += graph[person.name]
                except:
                    print 'Can`t append to queue'
                try:
                    searched.append(person.name)
                except:
                    print "Can`t append search list"
    return False

# Define some persons
ahmed = Person('Ahmed Hesham' ,'Mango Buyer')
shouk = Person('Shouk Hesham' ,'Mango Buyer')
helal = Person('Helal Hesham' ,'Mango Buyer')
ali = Person('Ali Hesham' ,'Mango Buyer')
gehan = Person('Gehan Samer' ,'Mango Seller')
mohamed = Person('Mohamed Samer' ,'Mango Buyer')

# Build simple social network
graph = {}

graph[ahmed.name] = [helal ,shouk ,gehan ,ali]
graph[shouk.name] = [helal ,ahmed ,mohamed ,ali]
graph[helal.name] = [shouk ,ahmed ,ali]
graph[ali.name] = [helal ,ahmed ,shouk]
graph[gehan.name] = [ahmed ,mohamed]
graph[mohamed.name] = [gehan ,shouk]

search("Shouk Hesham")