import unittest
from InventoryAllocator import InventoryAllocator


class TestInventoryAllocator(unittest.TestCase):

    def test_basic(self):
        order = {'apple': 1}
        warehouses = [{'name': 'wh1', 'inventory': {'apple': 1}}]
        expected = [{'wh1': {'apple': 1}}]
        inventoryAllocator = InventoryAllocator(warehouses)
        self.assertEqual(inventoryAllocator.allocateInventory(order), expected)

    def test_excess_inventory(self):
        order = {'apple': 1}
        warehouses = [{'name': 'wh1', 'inventory': {'apple': 2}}]
        expected = [{'wh1': {'apple': 1}}]
        inventoryAllocator = InventoryAllocator(warehouses)
        self.assertEqual(inventoryAllocator.allocateInventory(order), expected)

    def test_empty_order_no_warehouses(self):
        order = {}
        warehouses = []
        expected = []
        inventoryAllocator = InventoryAllocator(warehouses)
        self.assertEqual(inventoryAllocator.allocateInventory(order), expected)

    def test_no_warehouses(self):
        order = {'apple': 10}
        warehouses = []
        expected = []
        inventoryAllocator = InventoryAllocator(warehouses)
        self.assertEqual(inventoryAllocator.allocateInventory(order), expected)

    def test_empty_order(self):
        order = {}
        warehouses = [{'name': 'wh1', 'inventory': {'apple': 5}}]
        expected = []
        inventoryAllocator = InventoryAllocator(warehouses)
        self.assertEqual(inventoryAllocator.allocateInventory(order), expected)

    def test_zero_order(self):
        order = {'apple': 0}
        warehouses = [{'name': 'wh1', 'inventory': {'apple': 1}}]
        expected = []
        inventoryAllocator = InventoryAllocator(warehouses)
        self.assertEqual(inventoryAllocator.allocateInventory(order), expected)

    def test_no_inventory(self):
        order = {'apple': 1}
        warehouses = [{'name': 'wh1', 'inventory': {'apple': 0}}]
        expected = []
        inventoryAllocator = InventoryAllocator(warehouses)
        self.assertEqual(inventoryAllocator.allocateInventory(order), expected)

    def test_zero_order_no_inventory(self):
        order = {'apple': 0}
        warehouses = [{'name': 'wh1', 'inventory': {'apple': 0}}]
        expected = []
        inventoryAllocator = InventoryAllocator(warehouses)
        self.assertEqual(inventoryAllocator.allocateInventory(order), expected)

    def test_no_item_in_warehouse(self):
        order = {'apple': 1}
        warehouses = [{'name': 'wh1', 'inventory': {'orange': 10}}]
        expected = []
        inventoryAllocator = InventoryAllocator(warehouses)
        self.assertEqual(inventoryAllocator.allocateInventory(order), expected)

    def test_multiple_warehouses_split(self):
        order = {'apple': 10}
        warehouses = [{'name': 'wh1', 'inventory': {'apple': 5}},
                      {'name': 'wh2', 'inventory': {'apple': 5}}]
        expected = [{'wh1': {'apple': 5}}, {'wh2': {'apple': 5}}]
        inventoryAllocator = InventoryAllocator(warehouses)
        self.assertEqual(inventoryAllocator.allocateInventory(order), expected)

    def test_skip_empty_warehouses(self):
        order = {'apple': 10}
        warehouses = [{'name': 'wh1', 'inventory': {'apple': 0}},
                      {'name': 'wh2', 'inventory': {'apple': 10}}]
        expected = [{'wh2': {'apple': 10}}]
        inventoryAllocator = InventoryAllocator(warehouses)
        self.assertEqual(inventoryAllocator.allocateInventory(order), expected)

    def test_multiple_warehouses_by_cost(self):
        order = {'apple': 10}
        warehouses = [{'name': 'wh1', 'inventory': {'apple': 3}},
                      {'name': 'wh2', 'inventory': {'apple': 1}},
                      {'name': 'wh3', 'inventory': {'apple': 7}}]
        expected = [{'wh1': {'apple': 3}},
                    {'wh2': {'apple': 1}},
                    {'wh3': {'apple': 6}}]
        inventoryAllocator = InventoryAllocator(warehouses)
        self.assertEqual(inventoryAllocator.allocateInventory(order), expected)

    def test_multiple_order(self):
        order = {'apple': 10, 'orange': 5}
        warehouses = [{'name': 'wh1', 'inventory': {'apple': 10, 'orange': 5}}]
        expected = [{'wh1': {'apple': 10, 'orange': 5}}]
        inventoryAllocator = InventoryAllocator(warehouses)
        self.assertEqual(inventoryAllocator.allocateInventory(order), expected)

    def test_multiple_order_with_zero_order(self):
        order = {'apple': 10, 'orange': 0}
        warehouses = [{'name': 'wh1', 'inventory': {'apple': 10, 'orange': 5}}]
        expected = [{'wh1': {'apple': 10}}]
        inventoryAllocator = InventoryAllocator(warehouses)
        self.assertEqual(inventoryAllocator.allocateInventory(order), expected)

    def test_multiple_order_items_multiple_warehouses(self):
        order = {'apple': 10, 'orange': 5}
        warehouses = [{'name': 'wh1', 'inventory': {'apple': 10}},
                      {'name': 'wh2', 'inventory': {'orange': 5}}]
        expected = [{'wh1': {'apple': 10}}, {'wh2': {'orange': 5}}]
        inventoryAllocator = InventoryAllocator(warehouses)
        # inventoryAllocator.allocateInventory(order)
        self.assertEqual(inventoryAllocator.allocateInventory(order), expected)

    def test_reverse_multiple_order_items_multiple_warehouses(self):
        order = {'orange': 5, 'apple': 10}
        warehouses = [{'name': 'wh1', 'inventory': {'apple': 10}},
                      {'name': 'wh2', 'inventory': {'orange': 5}}]
        expected = [{'wh1': {'apple': 10}}, {'wh2': {'orange': 5}}]
        inventoryAllocator = InventoryAllocator(warehouses)
        self.assertEqual(inventoryAllocator.allocateInventory(order), expected)

    def test_multiple_order_multiple_warehouses_by_cost(self):
        order = {'apple': 10, 'orange': 7}
        warehouses = [{'name': 'wh1', 'inventory': {'apple': 3, 'orange': 4}},
                      {'name': 'wh2', 'inventory': {'apple': 1, 'orange': 0}},
                      {'name': 'wh3', 'inventory': {'apple': 7, 'orange': 6}}]
        expected = [{'wh1': {'apple': 3, 'orange': 4}},
                    {'wh2': {'apple': 1}},
                    {'wh3': {'apple': 6, 'orange': 3}}]
        inventoryAllocator = InventoryAllocator(warehouses)
        self.assertEqual(inventoryAllocator.allocateInventory(order), expected)

    def test_multiple_order_skip_warehouses(self):
        order = {'apple': 10, 'orange': 5}
        warehouses = [{'name': 'wh1', 'inventory': {'banana': 10}},
                      {'name': 'wh2', 'inventory': {'apple': 10, 'orange': 5}}]
        expected = [{'wh2': {'apple': 10, 'orange': 5}}]
        inventoryAllocator = InventoryAllocator(warehouses)
        self.assertEqual(inventoryAllocator.allocateInventory(order), expected)


if __name__ == '__main__':
    unittest.main()
