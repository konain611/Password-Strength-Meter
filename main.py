import streamlit as st
import re
import random
import string

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

def check_password_strength(password):
    score = 0
    feedback = []
    common_passwords = ["password", "123456", "password123", "qwerty", "abc123", "letmein", "welcome"]
    
    if password in common_passwords:
        st.error("❌ This password is too common and easily guessable.")
        return
    
    length_weight = 2 if len(password) >= 12 else 1 if len(password) >= 8 else 0
    score += length_weight
    if length_weight == 0:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    case_weight = 2 if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password) else 0
    score += case_weight
    if case_weight == 0:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    digit_weight = 2 if re.search(r"\d", password) else 0
    score += digit_weight
    if digit_weight == 0:
        feedback.append("❌ Add at least one number (0-9).")
    
    special_weight = 2 if re.search(r"[!@#$%^&*]", password) else 0
    score += special_weight
    if special_weight == 0:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    if score >= 7:
        st.success("✅ Strong Password!")
    elif score >= 5:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions below.")
    
    for msg in feedback:
        st.write(msg)

st.title("Password Strength Checker & Generator")
password = st.text_input("Enter your password:", type="password")
if st.button("Check Strength"):
    check_password_strength(password)
if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.text_input("Suggested Strong Password:", strong_password)