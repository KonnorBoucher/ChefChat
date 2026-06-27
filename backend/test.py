from services.generation import generate_answer

test_answer = generate_answer("how long do i bake cookies?", 

"""Chocolate Chip Cookies

Ingredients:
2 cups all-purpose flour
1 tsp baking soda
1 tsp salt
1 cup butter, softened
3/4 cup granulated sugar
3/4 cup brown sugar
2 large eggs
2 tsp vanilla extract
2 cups chocolate chips

Instructions:
Preheat oven to 375°F. Mix flour, baking soda and salt in a bowl. 
In a separate bowl beat butter and sugars until creamy. Add eggs and vanilla. 
Gradually mix in flour mixture. Stir in chocolate chips.
Drop rounded tablespoons onto ungreased baking sheets.
Bake for 9-11 minutes or until golden brown. Cool on baking sheet for 2 minutes."""
                )

# print(test_answer)

from services.embeddings import chunk_by_page

with open(r"C:\Users\hb536\OneDrive\Desktop\PersonalProjects\ChefChat\Good_Test_PDFs\trending-chocolate-recipe-collection-sunbutter.pdf", "rb") as f:
    chunks = chunk_by_page(f.read())

print(f"Found {len(chunks)} recipe pages")
"""
print("--- CHUNK 1 ---")
print(chunks[0][:500])
print("--- CHUNK 2 ---")
print(chunks[1][:500])
"""

for i in range(len(chunks)):
    print(f"Chunk {i + 1}")
    print("------------------------------")
    print(chunks[i][0:50])
    print()