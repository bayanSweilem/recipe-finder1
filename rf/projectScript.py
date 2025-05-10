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

# 
# find recipes tab
def find_func():
    search_query = st.text_input("Search recipes", placeholder="Type recipe name...").strip().lower()
    
    for name, data in st.session_state.recipes.items():
        if search_query in name.lower():  # search according to recipe name
            with st.container():
                st.markdown("### %s" % name)
                if data.get('Image'):# if the image exist display it & design it using Html
                    st.markdown("""
                    <img src="%s" style="width:300px; height:200px; object-fit:cover; border-radius:15px; margin-bottom:10px;">
                    """ % data['Image'], unsafe_allow_html=True)
                st.write("**Cuisine:** %s" % data['Cuisine'])
                st.write("**Ingredients:** %s" % ', '.join(data['Ingredients'])) #Compose all ingredients list items into one comma-separated list.omma-separated text.
                st.write("**Prep Time:** %d mins" % data['Prep Time'])
                st.write("**Difficulty:** %s" % data['Difficulty'])
                st.write("**Rating:** %s" % data.get('Rating', 'Not rated'))
                st.markdown("---")


#add recipe tab
def add_func():
    st.subheader("Add New Recipe")

    name = st.text_input("Recipe Name")
    if name in st.session_state.recipes: #check if the user added the recipe before
      st.write("recipe already exsists")
    cuisine = st.text_input("Cuisine")
    ingredients_input = st.text_area("Ingredients (comma separated)")
    prep_time = st.number_input("Preparation Time (in minutes)",value=25)
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
    rating = st.slider("Rating (out of 5)", 0.0, 5.0, 3.0, 0.1)
    image_url = st.text_input("Recipe Image URL")

    if st.button("Add Recipe"):
        ingredients = [ingredient.strip() for ingredient in ingredients_input.split(',') if ingredient.strip()]# Remove spaces from the ingredients list and divide them by commas.(list comprehension)
        #Keep only ingredients that are not empty
        image_url_clean = image_url.strip() if image_url.strip() else None
        #check if the user entered
        if not name:
            st.warning("Recipe name is required!")
        elif not cuisine:
            st.warning("Cuisine is required!")
        elif not ingredients:
            st.warning("Ingredients are required!")
        else:
            st.session_state.recipes[name] = {
                'Cuisine': cuisine,
                'Ingredients': ingredients,
                'Prep Time': prep_time,
                'Difficulty': difficulty,
                'Rating': rating,
                'Image': image_url_clean
            }
            st.success("Recipe '%s' added successfully!" % name)# display message for the user (the recipe added) 
            st.session_state.current_tab = "find" #return back to find tab 
            st.rerun()


# filter Recipes tab
def filter_func():
    st.subheader("Filter Recipes")
    col1, col2, col3 = st.columns(3) #Create columns for filtering the recipes

    with col1:
        difficulty_filter = st.selectbox("Difficulty", ["Any", "Easy", "Medium", "Hard"])
    with col2:
        max_time = st.slider("Max Prep Time (mins)", 0, 120, 60)
    with col3:
        min_rating = st.slider("Min Rating", 0.0, 5.0, 3.0, 0.1)

    filtered = {} #empty dict to store filtered recipes
    for name, data in st.session_state.recipes.items(): #loop through each recipe in the dictionary
        if difficulty_filter != "Any" and data['Difficulty'] != difficulty_filter:#Skip the recipe if its difficulty doesn't match the filter
            continue
        if data['Prep Time'] > max_time: #If the recipe's prep time exceeds the maximum amount of time specified, skip it.
            continue
        if (data.get('Rating') or 0) < min_rating:
            continue
        filtered[name] = data #add the recipe to the filtered dictionary if all requirements are satisfied.

    if filtered:
        st.write("Found %d recipes:" % len(filtered)) #Show the quantity of recipes that were located
        for name, data in filtered.items():#iterate through every recipe that has been filtered.
            with st.container():
                st.markdown("### %s" % name)
                if data.get('Image'):
                    st.markdown("""
                        <img src="%s" style="width:300px; height:200px; object-fit:cover; border-radius:15px; margin-bottom:10px;">
                        """ % data['Image'], unsafe_allow_html=True)
                st.write("**Cuisine:** %s" % data['Cuisine'])
                st.write("**Ingredients:** %s" % ', '.join(data['Ingredients']))#ingredients as a list separated by commas
                st.write("**Prep Time:** %d mins" % data['Prep Time'])
                st.write("**Difficulty:** %s" % data['Difficulty'])
                st.write("**Rating:** %s" % data.get('Rating', 'Not rated'))
                st.markdown("---")
    else:
        st.warning("No recipes match these filters.")


#recommendations tab
def rec_func():
    st.header("Recipe Recommendations")
    preferred_cuisine = st.text_input("Enter your preferred cuisine (e.g., Italian, Indian):")

    if preferred_cuisine:#Process it if the user has selected a cuisine.  Create a list at the beginning to hold recipe names that match.
        matching_recipes = []
        for recipe_name, recipe_data in st.session_state.recipes.items():#loop through cuisines
            if recipe_data["Cuisine"].lower() == preferred_cuisine.lower():
                matching_recipes.append(recipe_name) #add the matching recipe to the list

        if matching_recipes:
            st.write("Based on your love for %s, try these recipes:" % preferred_cuisine)
            for name in matching_recipes:#loop through the matching recipes
                data = st.session_state.recipes[name]
                with st.container():
                    st.markdown("### %s" % name)
                    if data.get('Image'):
                        st.markdown("""
                        <img src="%s" style="width:300px; height:200px; object-fit:cover; border-radius:15px; margin-bottom:10px;">
                        """ % data['Image'], unsafe_allow_html=True)
                    st.write("**Cuisine:** %s" % data['Cuisine'])
                    st.write("**Ingredients:** %s" % ', '.join(data['Ingredients']))
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
