from collections import OrderedDict

class InventoryAllocator:

	def __init__(self, orders, warehouses):
		self.orders = orders
		self.warehouses= warehouses
		
	def allocateInventory(self):
		shipments = []
		for order, amount in self.orders.items():
			for warehouse in self.warehouses:
				if amount == 0:
					break
				if order in warehouse['inventory']:
					if amount <= warehouse['inventory'].get(order):
						for shipment in shipments:
							if shipment.get(warehouse['name']):
								shipment[warehouse['name']].update({order: amount})
								break
						else:
							shipments.append({warehouse['name']: {order: amount}})
						amount -= warehouse['inventory'].get(order)
					else: 
						available = warehouse['inventory'].get(order)
						for shipment in shipments:
							if shipment.get(warehouse['name']):
								shipment[warehouse['name']].update({order: available})
								break
						else:
							shipments.append({warehouse['name']: {order: available}})
						amount -= available
			if amount > 0:
				return []
		return shipments

		


