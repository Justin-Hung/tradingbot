from bots import RSIBot
from tools import avg
from brokerConnections import IBConnection

bot = RSIBot()

connection = IBConnection()

print(bot.name)

print(avg([5,6,10,24]))

# This should work but I can't test it becuse Interactive broker is an absolute nightmare
#print(connection.order(ticker="QQQ", action="BUY", shares=1))
print(connection.name)
