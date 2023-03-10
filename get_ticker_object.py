
class Ticker:
    def __init__(self,tick,name,exchange):
        self.tick = tick
        self.name = name
        self.exchange = exchange

    def  __str__(self):
        return f'{self.tick}:{self.exchange}-{self.name}'

    def __repr__(self):
        return f'{self.tick}:{self.exchange}-{self.name}'

ticker_list = []
fobj = open('us_symbols.csv','r')
# read first line
fobj.readline()
# create ticker objects
for line in fobj:
    line = line.strip('\n').split(',')
    ticker_list.append(Ticker(line[0],line[1],line[2]))
fobj.close()
