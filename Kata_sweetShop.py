import unittest

sweetShop = [
    {"id": 1, "name": "Dairymilk", "category": "Chocolate", "price": "20", "Quantity": 10},
    {"id": 2, "name": "ChocoBar", "category": "candy", "price": "50", "Quantity": 7},
    {"id": 3, "name": "ChocoCake", "category": "pastry", "price": "70", "Quantity": 13},
    {"id": 4, "name": "MangoBar", "category": "candy", "price": "15", "Quantity": 20},
    {"id": 5, "name": "MangoCake", "category": "pastry", "price": "50", "Quantity": 5},
    {"id": 6, "name": "KitKat", "category": "Chocolate", "price": "20", "Quantity": 2},
]

def addSweet():
    name = input("Please Enter name of sweet:")
    catr = input("Please Enter category of sweet:")
    price = input("Please Enter price of sweet:")
    qty = input("Please Quantity name of sweet:")
    sweetShop.append(
        {
            "id":len(sweetShop)+1,
            "name":name,
            "category":catr,
            "price":price,
            "Quantity":qty
        })
 
def deleteSweet():
    delete = int(input("Please Enter sweet ID:"))
    if delete > len(sweetShop):
        print("ID not found")
    else:
        print(sweetShop[delete-1])
        value = input("Confirm Delete:Y/N::")
        save = sweetShop[delete-1]
        sweetShop.remove(save)if value == "y" or "Y"else print("sweet not delete")

def searchSweet(enterSweet):
    searchSweet1 = str(enterSweet).lower()
    searchItem = []
                                               
    for sweet in sweetShop:
      if(searchSweet1 in sweet['name'].lower()  or searchSweet1 in sweet['category'].lower() or searchSweet1 == sweet['price']):
          searchItem.append(sweet)
    return searchItem


def purchaseSweet():
    purSweet = input("Please Enter Sweet Name:")
    print("wait...")
    sweets = searchSweet(purSweet)
    if sweets != []:
       if sweets[0]['Quantity'] > 0:
        sweets[0]['Quantity'] -= 1
        print(f"{sweets[0]['name']} purchased. Remaining quantity: {sweets[0]['Quantity']}")
       else:
            print(f"{purSweet} is out of stock")
    else:
        print("Sweet not found")

class TestSweetShop(unittest.TestCase):
    def test_addSweet(self):
        result = addsweet("TestSweet", "Test", "99", 9)
        self.assertEqual(result['name'], "TestSweet")
        self.assertEqual(result['Quantity'], 9)

    def test_searchExistingsweet(self):
        results = searchsweet("Dairymilk")
        self.assertTrue(any(s['name'] == "Dairymilk" for s in results))

    def test_searchNonExistentSweet(self):
        results = searchsweet("NonSweet")
        self.assertEqual(len(results), 0)

    def test_deleteExistingsweet(self):
        addsweet("DeleteSweet", "temp", "10", 1)
        sweet_id = sweetShop[-1]['id']
        self.assertTrue(deletesweet(sweet_id))

    def test_deleteNonexistentSweet(self):
        self.assertFalse(deletesweet(9999))

    def test_PurchaseAvailableSweet(self):
        addsweet("BuySweet", "candy", "10", 2)
        msg = purchasesweet("BuySweet")
        self.assertIn("purchased", msg)

    def test_purchaseOutofStock(self):
        addsweet("OutStock", "test", "1", 0)
        msg = purchasesweet("OutStock")
        self.assertIn("out of stock", msg)


if __name__ == '__main__':
    unittest.main()
