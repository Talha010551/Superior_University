from product import Product
from avl_tree import AVLTree
from trie import Trie
from stack import Stack

avl = AVLTree()
root = None
trie = Trie()
recent_stack = Stack()

# Sample products
products = [
    Product(101, "iPhone 15", 80000, 4.8, 10),
    Product(102, "Samsung Galaxy S23", 75000, 4.6, 8),
    Product(103, "OnePlus 12", 60000, 4.5, 12),
    Product(104, "Redmi Note 13", 20000, 4.3, 20)
]

# Insert into structures
for p in products:
    root = avl.insert(root, p)
    trie.insert(p.name)

# Menu
while True:
    print("\nMobile Shop Inventory Optimizer")
    print("1. View All Products (Price Order)")
    print("2. Search Product Name")
    print("3. Autocomplete Product Name")
    print("4. Add to Recently Viewed")
    print("5. View Recently Viewed")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\n--- All Products ---")
        avl.pre_order(root)

    elif choice == "2":
        keyword = input("Enter product name to search: ").lower()
        matches = trie.autocomplete(keyword)
        print("Matches found:" if matches else "No matches.")
        for m in matches:
            print(f"- {m}")

    elif choice == "3":
        prefix = input("Start typing: ")
        suggestions = trie.autocomplete(prefix)
        print("Suggestions:")
        for s in suggestions:
            print(f"- {s}")

    elif choice == "4":
        name = input("Enter product name to mark as viewed: ")
        found = False
        for p in products:
            if p.name.lower() == name.lower():
                recent_stack.push(p)
                print("Added to recently viewed.")
                found = True
        if not found:
            print("Product not found.")

    elif choice == "5":
        recent_stack.view()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
