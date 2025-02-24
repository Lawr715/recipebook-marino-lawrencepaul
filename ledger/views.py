from django.shortcuts import render

recipes = [
    {
        "name": "Chicken Adobo",
        "ingredients": [
            {"name": "Chicken", "quantity": "1kg"},
            {"name": "Garlic", "quantity": "5 cloves"},
            {"name": "Soy Sauce", "quantity": "1/2 cup"},
            {"name": "Vinegar", "quantity": "1/2 cup"},
            {"name": "Water", "quantity": "1 cup"},
            {"name": "Sugar", "quantity": "1 tablespoon"},
            {"name": "Bay Leaves", "quantity": "2 leaves"},
            {"name": "Peppercorns", "quantity": "1 teaspoon"},
        ],
        "link": "/recipe/1/"
    },
    {
        "name": "Chao Fan Rice",
        "ingredients": [
            {"name": "Cooked Rice", "quantity": "2 cups"},
            {"name": "Eggs", "quantity": "2 pcs"},
            {"name": "Garlic", "quantity": "3 cloves"},
            {"name": "Soy Sauce", "quantity": "2 tablespoons"},
            {"name": "Carrots", "quantity": "1/2 cup, diced"},
            {"name": "Green Onions", "quantity": "1/4 cup, chopped"},
            {"name": "Oil", "quantity": "2 tablespoons"},
        ],
        "link": "/recipe/2/"
    }
]

# View for listing recipes
def recipe_list(request):
    return render(request, "ledger/recipe_list.html", {"recipes": recipes})

# View for displaying a single recipe
def recipe_detail(request, recipe_id):
    try:
        recipe = recipes[int(recipe_id) - 1]  # Adjust index since URLs start from 1
    except IndexError:
        return render(request, "ledger/not_found.html", status=404)  # Handle missing recipes
    return render(request, "ledger/recipe_detail.html", {"recipe": recipe})