import streamlit as st
pizzas = {
    "Margherita": {
        "small": 50,
        "medium": 70,
        "large": 90
    },
    "Pepperoni": {
        "small": 60,
        "medium": 80,
        "large": 100
    },
    "BBQ Chicken": {
        "small": 65,
        "medium": 85,
        "large": 110
    }
}
pizzatab,pastatab,softdrink=st.tabs(
    ["pizza","pasta","drinks"]
)
with pizzatab:
    col1,col2,col3=st.columns(3)
    with col1:
        chicken_size=st.segmented_control(
            "size:",["small", "medium", "large"]
        )