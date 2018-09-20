#! user/bin/python 

class JustCounter(object):
    __secretCount = 0
    mycount = 10

    def count(self):
        self.__secretCount += 1
        #self.__secretCount = self.__secretCount + 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter.__secretCount)
#print(counter.__secretCount)
#print(JustCounter.__secretCount)
print(JustCounter.mycount)
print(counter.mycount)

