import unittest
from InventoryAllocator import InventoryAllocator

class TestInventoryAllocator(unittest.TestCase):

	def test_basic(self):
		orders = {'apple': 1}
		warehouses = [{'name': 'wh1', 'inventory': {'apple': 1}}]
		expected = [{'wh1': {'apple': 1 }}]
		inventoryAllocator = InventoryAllocator(orders, warehouses)
		self.assertEqual(inventoryAllocator.allocateInventory(), expected)

	def test_excess_inventory(self):
		orders = {'apple': 1}
		warehouses = [{'name': 'wh1', 'inventory': { 'apple': 2 } }]
		expected = [{'wh1': {'apple': 1}}]
		inventoryAllocator = InventoryAllocator(orders, warehouses)
		self.assertEqual(inventoryAllocator.allocateInventory(), expected)

	def test_empty_order_no_warehouses(self):
		orders = {}
		warehouses = []
		expected = []
		inventoryAllocator = InventoryAllocator(orders, warehouses)
		self.assertEqual(inventoryAllocator.allocateInventory(), expected)	

	def test_no_warehouses(self):
		orders = {'apple': 10}
		warehouses = []
		expected = []
		inventoryAllocator = InventoryAllocator(orders, warehouses)
		self.assertEqual(inventoryAllocator.allocateInventory(), expected)	

	def test_empty_order(self):
		orders = {}
		warehouses = [{'name': 'wh1', 'inventory': {'apple': 5 }}]
		expected = []
		inventoryAllocator = InventoryAllocator(orders, warehouses)
		self.assertEqual(inventoryAllocator.allocateInventory(), expected)	

	def test_zero_order(self):
		orders = {'apple': 0}
		warehouses = [{'name': 'wh1', 'inventory': {'apple': 1}}]
		expected = []
		inventoryAllocator = InventoryAllocator(orders, warehouses)
		self.assertEqual(inventoryAllocator.allocateInventory(), expected)

	def test_no_inventory(self):
		orders = {'apple': 1}
		warehouses = [{'name': 'wh1', 'inventory': {'apple': 0}}]
		expected = []
		inventoryAllocator = InventoryAllocator(orders, warehouses)
		self.assertEqual(inventoryAllocator.allocateInventory(), expected)

	def test_zero_order_no_inventory(self):
		orders = {'apple': 0}
		warehouses = [{'name': 'wh1', 'inventory': {'apple': 0}}]
		expected = []
		inventoryAllocator = InventoryAllocator(orders, warehouses)
		self.assertEqual(inventoryAllocator.allocateInventory(), expected)

	def test_no_item_in_warehouse(self):
		orders = {'apple': 1}
		warehouses = [{'name': 'wh1', 'inventory': {'orange': 10}}]
		expected = []
		inventoryAllocator = InventoryAllocator(orders, warehouses)
		self.assertEqual(inventoryAllocator.allocateInventory(), expected)

	def test_multiple_warehouses_split(self):
		orders = { 'apple': 10 }
		warehouses = [{'name': 'wh1', 'inventory': {'apple': 5}},
					  {'name': 'wh2', 'inventory': {'apple': 5}}]
		expected = [{'wh1': {'apple': 5 }}, {'wh2': {'apple': 5}}]
		inventoryAllocator = InventoryAllocator(orders, warehouses)
		self.assertEqual(inventoryAllocator.allocateInventory(), expected)

	def test_skip_empty_warehouses(self):
		orders = {'apple': 10}
		warehouses = [{'name': 'wh1', 'inventory': {'apple': 0}}, 
					  {'name': 'wh2', 'inventory': {'apple': 10}}]
		expected = [{'wh2': {'apple': 10}}]
		inventoryAllocator = InventoryAllocator(orders, warehouses)
		self.assertEqual(inventoryAllocator.allocateInventory(), expected)	

	def test_multiple_warehouses_by_cost(self):
		orders = {'apple': 10}
		warehouses = [{'name': 'wh1', 'inventory': {'apple': 3}}, 
					  {'name': 'wh2', 'inventory': {'apple': 1}},
					  {'name': 'wh3', 'inventory': {'apple': 7}}]
		expected = [{'wh1': {'apple': 3}},
					{'wh2': {'apple': 1}}, 
					{'wh3': {'apple': 6}}]
		inventoryAllocator = InventoryAllocator(orders, warehouses)
		self.assertEqual(inventoryAllocator.allocateInventory(), expected)

	def test_multiple_order(self):
		orders = {'apple': 10 , 'orange': 5}
		warehouses = [{'name': 'wh1', 'inventory': {'apple': 10, 'orange': 5}}]
		expected = [{'wh1': {'apple': 10, 'orange': 5}}]
		inventoryAllocator = InventoryAllocator(orders, warehouses)
		self.assertEqual(inventoryAllocator.allocateInventory(), expected)

	def test_multiple_order_with_zero_order(self):
		orders = {'apple': 10 , 'orange': 0}
		warehouses = [{'name': 'wh1', 'inventory': {'apple': 10, 'orange': 5}}]
		expected = [{'wh1': {'apple': 10 }}]
		inventoryAllocator = InventoryAllocator(orders, warehouses)
		self.assertEqual(inventoryAllocator.allocateInventory(), expected)

	def test_multiple_order_items_multiple_warehouses(self):
		orders = {'apple': 10 , 'orange': 5}
		warehouses = [{'name': 'wh1', 'inventory': {'apple': 10}}, 
					  {'name': 'wh2', 'inventory': {'orange': 5}}]
		expected = [{'wh1': {'apple': 10}}, {'wh2': {'orange': 5}}]
		inventoryAllocator = InventoryAllocator(orders, warehouses)
		self.assertEqual(inventoryAllocator.allocateInventory(), expected)		

	def test_multiple_order_skip_warehouses(self):
		orders = {'apple': 10 , 'orange': 5}
		warehouses = [{'name': 'wh1', 'inventory': {'banana': 10}}, 
					  {'name': 'wh2', 'inventory': {'apple': 10 , 'orange': 5}}]
		expected = [{'wh2': {'apple': 10 , 'orange': 5}}]
		inventoryAllocator = InventoryAllocator(orders, warehouses)
		self.assertEqual(inventoryAllocator.allocateInventory(), expected)	




if __name__ == '__main__':
	unittest.main()



	# def test_(self):
	# 	orders = {}
	# 	warehouses = []
	# 	expected = []
	# 	inventoryAllocator = InventoryAllocator(orders, warehouses)
	# 	self.assertEqual(inventoryAllocator.allocateInventory(), expected)	