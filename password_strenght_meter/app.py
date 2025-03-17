import streamlit as st
import re

def check_password_strength(password):
    strength = 0
    remarks = "Weak"
    
    # Criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r"[A-Z]", password))
    lowercase_criteria = bool(re.search(r"[a-z]", password))
    digit_criteria = bool(re.search(r"\d", password))
    special_char_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    
    # Strength calculation
    strength += length_criteria
    strength += uppercase_criteria
    strength += lowercase_criteria
    strength += digit_criteria
    strength += special_char_criteria
    
    # Remarks based on strength
    if strength == 5:
        remarks = "Very Strong"
    elif strength == 4:
        remarks = "Strong"
    elif strength == 3:
        remarks = "Moderate"
    elif strength == 2:
        remarks = "Weak"
    else:
        remarks = "Very Weak"
    
    return strength, remarks

# Streamlit UI
st.title("🔐 Password Strength Meter")
password = st.text_input("Enter your password:", type="password")

if password:
    strength, remarks = check_password_strength(password)
    st.write(f"**Strength Score:** {strength}/5")
    st.write(f"**Password Strength:** {remarks}")
    
    # Progress bar
    st.progress(strength / 5)
