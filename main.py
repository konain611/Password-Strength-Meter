import streamlit as st
import re
import random
import string

# Page Configuration
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .stApp {
            background-color: #ffffff;
        }
        h3 {
            text-align: center;
            font-size: 320px;
            color: #d32f2f;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #555;
            margin-bottom: 20px;
        }
        .stTextInput, .stButton {
            width: 100%;
        }
        .password-box {
            background: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0px 4px 12px rgba(211, 47, 47, 0.2);
        }
        .stButton > button {
            background-color: #d32f2f !important;
            color: white !important;
            border: none;
            border-radius: 8px;
            padding: 10px 15px;
            font-size: 16px;
            transition: 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #b71c1c !important;
        }
        .feedback {
            font-size: 16px;
            font-weight: bold;
            color: #d32f2f;
            margin-top: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

def check_password_strength(password):
    score = 0
    feedback = []
    common_passwords = ["password123", "Password", "password", "12345678", "Password123", "qwerty", "abc123", "letmein", "welcome"]

    if password in common_passwords:
        st.warning("🙁 &nbsp; This password is too common and easily guessable.")
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
        st.markdown(f'<p class="feedback">{msg}</p>', unsafe_allow_html=True)

# UI Layout
st.markdown('<h3 class="title">🔐 Password Strength Checker & Generator</h3>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Ensure your password is strong and secure.</p>', unsafe_allow_html=True)

password = st.text_input("Enter your password:", type="password")

if st.button("Check Strength"):
    check_password_strength(password)

if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.text_input("Suggested Strong Password:", strong_password)
