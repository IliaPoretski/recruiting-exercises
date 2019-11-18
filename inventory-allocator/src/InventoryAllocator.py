from copy import deepcopy


class InventoryAllocator:
    """
    Class used to allocate inventory based on order, and warehouse inventory.

    Attributes
    ----------
    warehouses: list
        A list of warehouses. each warehouse has a name and inventory.

    Methods
    -------
    allocateInventory(order_input: dict) -> list
        Returns the allocated inventory
        based on all warehouse inventory and order_input.

    """
    def __init__(self, warehouses: list):
        self.warehouses = warehouses

    def allocateInventory(self, order_input: dict) -> list:
        # Create copy of order_input to not make changes to argument.
        order = deepcopy(order_input)
        allocations = []
        for warehouse in self.warehouses:
            # Stops iterating warehouses if all inventory allocated
            if all(units <= 0 for units in order.values()):
                break
            for item, units, in order.items():
                # If item is in warehouse with enough inventory and unallocated
                if (item in warehouse['inventory'] and
                        warehouse['inventory'].get(item) > 0 and
                        units > 0):
                    units_allocated = min(units,
                                          warehouse['inventory'].get(item))
                    # Add to allocation if warehouse exists in allocations
                    for allocation in allocations:
                        if allocation.get(warehouse['name']):
                            allocation[warehouse['name']].\
                                update({item: units_allocated})
                            break
                    # Else add warehouse to allocation
                    else:
                        allocations.append({warehouse['name']:
                                           {item: units_allocated}})
                    # Update amount of units still required in order
                    order[item] = units - units_allocated
        # If order is not fulfilled return empty list
        if not all(units <= 0 for units in order.values()):
            return []
        else:
            return allocations
