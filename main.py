import streamlit as st

print(st.__version__)
# st.beta_set_page_config(page_bg_color='#FFFDD0')

# Create a title and subtitle
st.title("Hand2Hand")
st.subheader("Buy and Sell Books with Other Students")

# Create a function to display top books


def top_books(category):
    st.subheader(f"Top Books in {category}")

    # Create a list of dictionaries representing books
    books = [{"title": "The Great Gatsby", "img": "gatsby.jpg"},
             {"title": "To Kill a Mockingbird", "img": "mockingbird.jpg"},
             {"title": "Pride and Prejudice", "img": "prideprejudice.jpg"}]

    for book in books:
        # Create a title for the book
        st.write(book["title"])

        # Create an image for the book
        st.image(book["img"], width=150)

        # Create a title and subtitle
        st.title("Book Trading Club")
        st.subheader("Top Books by Category")

        # Create a menu with options to choose a category
        st.sidebar.title("Menu")

        menu = ["Fiction", "Non-Fiction", "Classics"]
        category = st.sidebar.selectbox("Select a category", menu)

        if category == "Fiction":
            top_books("Fiction")
        elif category == "Non-Fiction":
            top_books("Non-Fiction")
        elif category == "Classics":
            top_books("Classics")


def dentistry():
    st.subheader("Dentistry")


def business():
    st.subheader("business")


def marketing():
    st.subheader("marketing")


def biochemistry():
    st.subheader("biochemistry")


def haematology():
    st.subheader("haematology")


def medication():
    st.subheader("medication")


def art():
    st.subheader("art")


def anatomy():
    st.subheader("anatomy")


def engineering():
    st.subheader("engineering")


def management():
    st.subheader("management")


def technology():
    st.subheader("technology")


# Create a menu with options to buy or sell a book
st.sidebar.title("Menu")

menu = ["Homepage", "Dentistry", "Business", "Marketing", "Biochemistry", "Haematology",
        "Medication", "Art", "Anatomy", "Engineering", "Management", "Technology"]
choice = st.sidebar.selectbox("Select an option", menu)

if choice == "Homepage":
    st.write("Welcome to the Book Trading Club")
elif choice == "Dentistry":
    dentistry()
elif choice == "Business":
    business()
elif choice == "Marketing":
    marketing()
elif choice == "Biochemistry":
    biochemistry()
elif choice == "Haematology":
    haematology()
elif choice == "Medication":
    medication()
elif choice == "Art":
    art()
elif choice == "Anatomy":
    anatomy()
elif choice == "Engineering":
    engineering()
elif choice == "Management":
    management()
elif choice == "Technology":
    technology()
