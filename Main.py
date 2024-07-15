import streamlit as st
import time
import numpy as np
import pandas as pd

st.title('I like CS 😆')

_LOREM_IPSUM = """
    I like computer science. And I like studying backend.. Whould you ~ I'll study backend on this summer vacation. 😆
"""

def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)

    yield pd.DataFrame(
        np.random.randn(2, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )


if st.button("What I do?"):
    st.write_stream(stream_data)

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

st.write("This is my score.")

st.slider("This is a slider score", 0, 100, (0, 75))

st.divider()  # 👈 Draws a horizontal rule

st.write("This text is between the horizontal rules.")

st.divider()  # 👈 Another horizontal rule