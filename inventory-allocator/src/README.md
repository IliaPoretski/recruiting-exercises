# Inventory Allocator for Deliverr Challenge

## Files

###### `InventoryAllocator.py`
File containing `InventoryAllocator` class and implementation for inventory allocation based on order and warehouse inventory.

###### `InventoryAllocatorTest.py`
Unit tests to test `InventoryAllocator` class.

###### `InventoryAllocatorManualTest.py`
Runs test based on input given in `InventoryAllocatorManualInput.txt`.

###### `InventoryAllocatorManualInput.txt`
File to input your own test cases. String must be surronged by single or double quotes.
An example input is provided.
**File Format**
Line 1: number of test cases

Line 2: order
Line 3: warehouse inventory
Line 4: expected output

Repeat lines 2-4 based on number of test cases

## Running the tests
### To run the pre-made unit tests
1. Download repository
2. Open a command prompt and navigate to the `src` folder.
3. Run the following command: `python InventoryAllocatorTest.py`
### To run custom tests
1. Download repository
2. Edit `InventoryAllocatorManualInput.txt`, ensuring proper formatting
3. Open a command prompt and navigate to the `src` folder.
4. Run the following command: `python InventoryAllocatorManualTest.py`
