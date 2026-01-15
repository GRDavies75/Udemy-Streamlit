# Standard libraries

# Thirdparty libraries
import streamlit as st

# local packages


# fx and code
def main():
    '''
    All your code goes here
    '''
    st.title("(Simple) Text examples")
    st.text("")
    st.text("Hello, World!")
    name = "Johnny"
    st.text(f"Here's {name}!!!")

    #Header
    st.header("This is a header")

    #subheader
    st.subheader("This is a subheader")

    #title
    st.title("This is a Title")

    #markdown
    st.markdown("## This is markdown")

    #displaying Text with Colored background / highlights
    st.info("This is usually used with giving information") # Blue background
    st.success("Succesful") # Green background
    st.warning("This is dangerous") # Yellow background
    st.error("This is an error") # Red background
    st.exception("This is an exception") # Also Red background # type: ignore


if __name__ == '__main__':
    main()
