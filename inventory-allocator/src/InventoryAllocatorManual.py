import unittest
import json
from InventoryAllocator import InventoryAllocator


def convert_quotes(input: str) -> str:
    # Replaces single quotes with double quotes for json parsing
    return input.replace("\'", "\"")


class TestInventoryAllocatorManual(unittest.TestCase):

    def test_from_file(self):
        with open('InventoryAllocatorManualInput.txt', 'r') as file:
            num_tests = int(file.readline())
            for x in range(num_tests):
                order = json.loads(convert_quotes(file.readline()))
                warehouses = json.loads(convert_quotes(file.readline()))
                expected = json.loads(convert_quotes(file.readline()))
                inventoryAllocator = InventoryAllocator(warehouses)
                self.assertEqual(inventoryAllocator.allocateInventory(order),
                                 expected)


if __name__ == '__main__':
    unittest.main()
