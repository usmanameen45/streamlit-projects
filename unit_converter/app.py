import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import os


def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        "meter": 1,
        "kilometer": 0.001,
        "centimeter": 100,
        "millimeter": 1000,
        "inch": 39.3701,
        "foot": 3.28084,
        "yard": 1.09361,
        "mile": 0.000621371
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def weight_converter(value, from_unit, to_unit):
    conversion_factors = {
        "gram": 1,
        "kilogram": 0.001,
        "pound": 0.00220462,
        "ounce": 0.035274
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    return value

# Custom UI with Sidebar and Option Menu
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")
st.title("🔄 Unit Converter")

with st.sidebar:
    image_path = os.path.abspath("logo.png")
    image = Image.open(image_path)
    st.sidebar.image(image, width=150)
    conversion_type = option_menu("Select Conversion Type", ["Length", "Weight", "Temperature"],
                                  icons=["rulers", "balance-scale", "thermometer-half"], menu_icon="list", default_index=0)

st.markdown("---")

if conversion_type == "Length":
    units = ["meter", "kilometer", "centimeter", "millimeter", "inch", "foot", "yard", "mile"]
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
    if st.button("Convert", use_container_width=True):
        result = length_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")

elif conversion_type == "Weight":
    units = ["gram", "kilogram", "pound", "ounce"]
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
    if st.button("Convert", use_container_width=True):
        result = weight_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")

elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    value = st.number_input("Enter Value", format="%.2f")
    if st.button("Convert", use_container_width=True):
        result = temperature_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
