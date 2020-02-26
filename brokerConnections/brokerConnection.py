class BrokerConnection:
	name = "unspecified"

	def order(ticker, action, shares, exchange=None, curr="USD"):
		raise Exception("BrokerConnection must be overridden")