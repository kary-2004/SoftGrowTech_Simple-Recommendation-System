import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Recommendation System", page_icon="🎯", layout="centered")

st.title("🎬🛍️ Smart Recommendation System")
st.write("Search and filter items easily, then get recommendations!")

# Expanded dataset
data = pd.DataFrame({
    "name": [
        "Titanic","The Notebook","La La Land","Pride & Prejudice",
        "Avengers","Iron Man","Batman","Spider-Man",
        "The Conjuring","Insidious","Annabelle","The Nun",
        "Interstellar","Gravity","Inception","The Martian",
        "iPhone","Samsung Galaxy","OnePlus Phone","Google Pixel",
        "MacBook","Dell Laptop","HP Laptop","Lenovo Laptop",
        "iPad","Samsung Tablet",
        "Nike Shoes","Adidas Shoes","Puma Shoes","Reebok Shoes",
        "Levi's Jeans","Zara Jacket","H&M T-Shirt","Gucci Bag",
        "Rolex Watch","Casio Watch","Fossil Watch",
        "RayBan Sunglasses","Oakley Sunglasses",
        "Sofa Set","Dining Table","Bed Mattress","Office Chair",
        "Wall Clock","Table Lamp"
    ],
       "category": [
    *(["Movie"]*16),
    *(["Product"]*29)
],

    "type": [
        "Romance","Romance","Romance","Romance",
        "Action","Action","Action","Action",
        "Horror","Horror","Horror","Horror",
        "Sci-Fi","Sci-Fi","Sci-Fi","Sci-Fi",
        "Electronics","Electronics","Electronics","Electronics",
        "Electronics","Electronics","Electronics","Electronics",
        "Electronics","Electronics",
        "Fashion","Fashion","Fashion","Fashion",
        "Fashion","Fashion","Fashion","Fashion",
        "Accessories","Accessories","Accessories",
        "Accessories","Accessories",
        "Home","Home","Home","Home",
        "Home","Home"
    ]
})

# Sidebar filters
st.sidebar.header("🔍 Filter Options")
category_filter = st.sidebar.selectbox("Select Category:", ["All"] + sorted(data["category"].unique().tolist()))
type_filter = st.sidebar.selectbox("Select Type:", ["All"] + sorted(data["type"].unique().tolist()))

# Apply filters
filtered_data = data.copy()
if category_filter != "All":
    filtered_data = filtered_data[filtered_data["category"] == category_filter]
if type_filter != "All":
    filtered_data = filtered_data[filtered_data["type"] == type_filter]

# Searchable dropdown (Streamlit selectbox supports typing search)
selected_item = st.selectbox("🔎 Search & select item:", filtered_data["name"].tolist())

# Recommendation function
def recommend_items(selected_item):
    row = data[data["name"] == selected_item]
    if row.empty:
        return None, None

    item_type = row.iloc[0]["type"]

    recs = data[(data["type"] == item_type) & (data["name"] != selected_item)]
    return recs["name"].tolist(), item_type

# Button
if st.button("Recommend"):
    results, item_type = recommend_items(selected_item)

    if results is None:
        st.error("Item not found ❌")
    else:
        st.success(f"Recommendations based on: {item_type}")

        if len(results) == 0:
            st.info("No recommendations found.")
        else:
            st.subheader("Recommended Items:")
            for item in results:
                st.write(f"👉 {item}")

# Show filtered dataset
with st.expander("📂 View Filtered Dataset"):
    st.dataframe(filtered_data)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit & Pandas")