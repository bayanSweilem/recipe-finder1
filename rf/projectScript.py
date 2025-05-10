import streamlit as st

# Creating buttons with css
st.markdown("""
<style>
    div.stButton > button {
        background-color: #ffffff;
        color: #120f21; /*text color*/
        font-size: 14px;
        font-weight: bold;
        padding: 10px 10px;
        border-radius: 12px;
        border: none;
        margin: 0;
        width: 100%;
        box-sizing: border-box;
    }
    /* Soft blue-gray background on hover */
    div.stButton > button:hover { 
        background-color: #eff3f8;
        color: #120f21;
    }
    /*style for active tabs*/
    div.stButton.tab-active > button {
        background-color: #ccd0cf !important;
        color: #253745 !important;
    }
</style>
""", unsafe_allow_html=True)

# import google font (for title) with Html
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# title & description designed with html
st.markdown("<h1 style='text-align: center; font-size: 70px; font-family: \"Libre Baskerville\", serif;'>Recipe Finder</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Find and share your favorite recipes with ratings, preparation time, and cuisine information.</p>", unsafe_allow_html=True)

# Ensure the recipe data exists by initializing it (create dict for  6 recipes)
if 'recipes' not in st.session_state:
    st.session_state.recipes = {
        'Spaghetti Carbonara': {
            'Cuisine': 'Italian',
            'Ingredients': ['Pasta', 'Eggs', 'Cheese', 'Bacon'],
            'Prep Time': 20,
            'Difficulty': 'Medium',
            'Rating': 4.5,
            'Image': "https://images.unsplash.com/photo-1612874742237-6526221588e3"
        },
        'Chicken Tikka Masala': {
            'Cuisine': 'Indian',
            'Ingredients': ['Chicken', 'Yogurt', 'Spices', 'Tomato Sauce'],
            'Prep Time': 45,
            'Difficulty': 'Hard',
            'Rating': 4.8,
            'Image': "https://images.unsplash.com/photo-1565557623262-b51c2513a641"
        },
        'Avocado Toast': {
            'Cuisine': 'American',
            'Ingredients': ['Bread', 'Avocado', 'Salt', 'Pepper'],
            'Prep Time': 5,
            'Difficulty': 'Easy',
            'Rating': 3.7,
            'Image': "https://www.siftandsimmer.com/wp-content/uploads/2023/03/IMG_1208.jpg"
        },
        'Sushi Rolls': {
            'Cuisine': 'Japanese',
            'Ingredients': ['Sushi Rice', 'Nori', 'Fish', 'Vegetables'],
            'Prep Time': 60,
            'Difficulty': 'Hard',
            'Rating': 4.6,
            'Image': "https://images.unsplash.com/photo-1579871494447-9811cf80d66c"
        },
        'Beef Tacos': {
            'Cuisine': 'Mexican',
            'Ingredients': ['Tortillas', 'Ground Beef', 'Cheese', 'Lettuce'],
            'Prep Time': 25,
            'Difficulty': 'Medium',
            'Rating': 4.3,
            'Image': "https://images.unsplash.com/photo-1565299585323-38d6b0865b47"
        },
        'Ratatouille': {
            'Cuisine': 'French',
            'Ingredients': ['Eggplant', 'Zucchini', 'Tomatoes', 'Herbs'],
            'Prep Time': 50,
            'Difficulty': 'Medium',
            'Rating': 4.4,
            'Image': "https://images.unsplash.com/photo-1572453800999-e8d2d1589b7c?q=80&w=1970&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        }
    }

# Track the current tab
if "current_tab" not in st.session_state:
    st.session_state.current_tab = "find"

# Tab dictionary
tabs = {
    "Find Recipes": "find",
    "Add Recipe": "add",
    "Filter Recipe": "filter",
    "Recommendations": "recommendations"
}

# Display tab 4 buttons
col1, col2, col3, col4 = st.columns(4)
for col, (label, key) in zip([col1, col2, col3, col4], tabs.items()):
    with col:
        if st.session_state.current_tab == key:
            st.markdown(f"""
            <div class="stButton tab-active">
                <button disabled>{label}</button>
            </div>
            """, unsafe_allow_html=True)
        else:
            if st.button(label):
                st.session_state.current_tab = key
                st.rerun()


# find recipes tab
def find_func():
    # get user search input and clean it
    search_query = st.text_input("Search recipes", placeholder="Type recipe name...").strip().lower()
    
    found = False  # to check if we found any matching recipe

    for name, data in st.session_state.recipes.items():
        if search_query in (name.lower() if name else ''):
            found = True
            with st.container():
                st.markdown("### %s" % name)
                
                # show image if it exists
                if data.get('Image'):
                    st.markdown("""
                    <img src="%s" style="width:300px; height:200px; object-fit:cover; border-radius:15px; margin-bottom:10px;">
                    """ % data['Image'], unsafe_allow_html=True)
                
                # get ingredients list, show it nicely
                ingredients = data.get('Ingredients', None) 
                if ingredients is None:
                    ingredients_display = ""
                else:
                    ingredients_display = ', '.join(ingredients)

                # show all recipe details
                st.write("**Cuisine:** %s" % data.get('Cuisine', None))
                st.write("**Ingredients:** %s" % ingredients_display)
                st.write("**Prep Time:** %s mins" % data.get('Prep Time', None))
                st.write("**Difficulty:** %s" % data.get('Difficulty', None))
                st.write("**Rating:** %s" % data.get('Rating', None))
                st.markdown("---")

    if not found:
        st.write("No recipes found.")




# add recipe tab
def add_func():
    st.subheader("Add New Recipe")

    # get all inputs from user
    name = st.text_input("Recipe Name")
    cuisine = st.text_input("Cuisine")
    ingredients_input = st.text_area("Ingredients (comma separated)")
    prep_time = st.number_input("Preparation Time (in minutes)", value=25)
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
    rating = st.slider("Rating (out of 5)", 0.0, 5.0, 3.0, 0.1)
    image_url = st.text_input("Recipe Image URL")

    if st.button("Add Recipe"):
        if not name:
            name = None

        if not cuisine:
            cuisine = None

        if not ingredients_input:
            ingredients = None
        else:
            ingredients = [ingredient.strip() for ingredient in ingredients_input.split(',') if ingredient.strip()]

        if not image_url.strip():
            image_url_clean = None
        else:
            image_url_clean = image_url.strip()

        # store the recipe in session state
        st.session_state.recipes[name] = {
            'Cuisine': cuisine,
            'Ingredients': ingredients,
            'Prep Time': prep_time,
            'Difficulty': difficulty,
            'Rating': rating,
            'Image': image_url_clean
        }

        # show success message and switch to find tab
        st.success("Recipe '%s' added successfully!" % name)
        st.session_state.current_tab = "find"
        st.rerun()






# filter Recipes tab
def filter_func():
    st.header("Filter Recipes")

    # Collect filter options from the user
    preferred_cuisine = st.text_input("Enter preferred cuisine (optional):").strip()
    max_prep_time = st.number_input("Enter maximum prep time (in minutes):", min_value=0, value=60)
    difficulty = st.selectbox("Select difficulty level:", ["Any", "Easy", "Medium", "Hard"])

    matching_recipes = []

    # Loop through all recipes and apply filters
    for recipe_name, recipe_data in st.session_state.recipes.items():
        # Apply filters
        matches_cuisine = (preferred_cuisine.lower() in recipe_data["Cuisine"].lower()) if preferred_cuisine else True
        matches_time = recipe_data["Prep Time"] <= max_prep_time
        matches_difficulty = (difficulty == "Any") or (recipe_data["Difficulty"] == difficulty)

        # If all conditions are met, add to matching recipes
        if matches_cuisine and matches_time and matches_difficulty:
            matching_recipes.append(recipe_name)

    # If there are matching recipes, display them
    if matching_recipes:
        st.write("Matching recipes based on your filters:")
        for name in matching_recipes:
            data = st.session_state.recipes[name]
            with st.container():
                st.markdown("### %s" % name)
                if data.get('Image'):
                    st.markdown("""
                    <img src="%s" style="width:300px; height:200px; object-fit:cover; border-radius:15px; margin-bottom:10px;">
                    """ % data['Image'], unsafe_allow_html=True)
                st.write("**Cuisine:** %s" % data['Cuisine'])
                st.write("**Ingredients:** %s" % ', '.join(data['Ingredients']) if data.get('Ingredients') else "None")
                st.write("**Prep Time:** %d mins" % data['Prep Time'])
                st.write("**Difficulty:** %s" % data['Difficulty'])
                st.write("**Rating:** %s" % data.get('Rating', 'Not rated'))
                st.markdown("---")
    else:
        st.warning("No recipes found that match your filters.")




#recommendations tab
def rec_func():
    st.header("Recipe Recommendations")
    preferred_cuisine = st.text_input("Enter your preferred cuisine (e.g., Italian, Indian):")

    if preferred_cuisine:  # Process it if the user has selected a cuisine.
        matching_recipes = []  # Create a list to store recipes that match.
        
        # Loop through recipes in session state
        for recipe_name, recipe_data in st.session_state.recipes.items():
            # Check if the cuisine matches
            if recipe_data["Cuisine"] and preferred_cuisine.lower() in recipe_data["Cuisine"].lower():
                matching_recipes.append(recipe_name)

        if matching_recipes:  # If matching recipes are found, display them.
            st.write("Based on your love for %s, try these recipes:" % preferred_cuisine)
            for name in matching_recipes:
                data = st.session_state.recipes[name]
                with st.container():
                    st.markdown("### %s" % name)
                    if data.get('Image'):
                        st.markdown("""
                        <img src="%s" style="width:300px; height:200px; object-fit:cover; border-radius:15px; margin-bottom:10px;">
                        """ % data['Image'], unsafe_allow_html=True)
                    st.write("**Cuisine:** %s" % data['Cuisine'])
                    st.write("**Ingredients:** %s" % ', '.join(data['Ingredients']) if data.get('Ingredients') else "None")
                    st.write("**Prep Time:** %d mins" % data['Prep Time'])
                    st.write("**Difficulty:** %s" % data['Difficulty'])
                    st.write("**Rating:** %s" % data.get('Rating', 'Not rated'))
                    st.markdown("---")
        else:
            st.warning("No matching recipes found for this cuisine.")


# call func. according to the button
if st.session_state.current_tab == "find":
    find_func()
elif st.session_state.current_tab == "add":
    add_func()
elif st.session_state.current_tab == "filter":
    filter_func()
elif st.session_state.current_tab == "recommendations":
    rec_func()
