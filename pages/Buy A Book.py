import streamlit as st

# Create a function for the user to buy a book

# st.set_page_config(background_color='#FFFDD0')


def buy_book():
    st.subheader("Buy a Book")

    # Get user input for book title and author
    title = st.text_input("Book Title")
    author = st.text_input("Author")

    # Get user input for price
    price = st.number_input("Price (USD)")

    # Create a submit button
    if st.button("Submit"):
        st.success("Book Submitted for Sale!")


if __name__ == '__main__':
    buy_book()
