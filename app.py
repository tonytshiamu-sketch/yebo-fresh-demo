"""
Yebo Fresh Redesign - Modern AI-Powered Grocery Platform
Streamlit Cloud Deployment Ready
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set page config MUST BE FIRST
st.set_page_config(
    page_title="Yebo Fresh | Fresh Groceries Delivered",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .main { padding: 0 !important; }
    :root {
        --primary: #2E8B57;
        --primary-light: #4CAF7A;
        --secondary: #FF6B35;
        --accent: #FFD166;
    }
    
    .modern-card {
        background: white;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid rgba(0,0,0,0.05);
        margin: 10px 0;
    }
    
    .product-card {
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #eaeaea;
        transition: transform 0.3s ease;
        height: 100%;
    }
    
    .product-card:hover {
        transform: translateY(-5px);
    }
    
    @media (max-width: 768px) {
        .product-card { margin-bottom: 16px; }
        .modern-card { padding: 16px; }
    }
</style>
""", unsafe_allow_html=True)

# Mock Data
def load_products():
    return pd.DataFrame([
        {'id': 1, 'name': 'Fresh Chicken Breast (1kg)', 'price': 89.99, 'category': 'Meat', 'image': '🍗', 'rating': 4.7},
        {'id': 2, 'name': 'Mixed Vegetables Pack', 'price': 45.50, 'category': 'Produce', 'image': '🥦', 'rating': 4.5},
        {'id': 3, 'name': 'Maize Meal Super (5kg)', 'price': 67.99, 'category': 'Pantry', 'image': '🌽', 'rating': 4.8},
        {'id': 4, 'name': 'Fresh Milk (2L)', 'price': 32.99, 'category': 'Dairy', 'image': '🥛', 'rating': 4.6},
        {'id': 5, 'name': 'Brown Bread Loaf', 'price': 18.99, 'category': 'Bakery', 'image': '🍞', 'rating': 4.4},
        {'id': 6, 'name': 'Cooking Oil (2L)', 'price': 54.99, 'category': 'Pantry', 'image': '🫒', 'rating': 4.3},
    ])

# Navigation
def create_nav():
    col1, col2, col3, col4, col5, col6 = st.columns([2, 1, 1, 1, 1, 1])
    with col1:
        st.markdown("## 🛒 YEBO FRESH")
        st.caption("Fresh Groceries Delivered")
    with col2: st.markdown("**🏠 Home**")
    with col3: st.markdown("**🛍️ Shop**")
    with col4: st.markdown("**🎯 Deals**")
    with col5: st.markdown("**📞 Contact**")
    with col6: 
        st.markdown("**🛒 Cart (3)**")
    st.markdown("---")

# Hero Section
def create_hero():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("# Fresh Groceries,")
        st.markdown("# <span style='color:#2E8B57'>Delivered to Your Door</span>", unsafe_allow_html=True)
        st.markdown("Serving townships across South Africa with fresh, affordable groceries.")
        col_a, col_b = st.columns(2)
        with col_a: st.button("🚀 Start Shopping", use_container_width=True)
        with col_b: st.button("📍 Check Delivery", use_container_width=True, type="secondary")
    
    with col2:
        st.markdown("""
        <div class='modern-card'>
            <h3>🕒 Live Delivery</h3>
            <h1 style='color:#2E8B57'>2.3 hours</h1>
            <p>Average delivery time</p>
            <p>✅ 15,000+ customers</p>
            <p>✅ 98% on-time</p>
        </div>
        """, unsafe_allow_html=True)

# Products
def show_products():
    st.markdown("## 🛍️ Popular Products")
    products = load_products()
    
    # Filters
    cols = st.columns(4)
    with cols[0]: category = st.selectbox("Category", ["All", "Meat", "Produce", "Dairy", "Pantry", "Bakery"])
    with cols[1]: sort = st.selectbox("Sort by", ["Popular", "Price: Low", "Price: High", "Rating"])
    
    # Product grid
    st.markdown("<br>", unsafe_allow_html=True)
    product_cols = st.columns(3)
    
    for idx, product in products.iterrows():
        with product_cols[idx % 3]:
            st.markdown(f"""
            <div class='product-card'>
                <div style='
                    background: #f5f5f5;
                    height: 150px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 60px;
                '>
                    {product['image']}
                </div>
                <div style='padding: 15px;'>
                    <h4>{product['name']}</h4>
                    <p style='color: #FF6B35; font-weight: bold;'>R {product['price']:.2f}</p>
                    <p>{"⭐" * int(product['rating'])} ({product['rating']})</p>
                    <button style='
                        width: 100%;
                        background: #2E8B57;
                        color: white;
                        border: none;
                        padding: 10px;
                        border-radius: 8px;
                        cursor: pointer;
                    '>Add to Cart</button>
                </div>
            </div>
            """, unsafe_allow_html=True)

# AI Features
def show_ai_features():
    st.markdown("## 🤖 AI-Powered Features")
    
    tab1, tab2 = st.tabs(["Smart Shopping List", "Delivery Predictor"])
    
    with tab1:
        st.markdown("### Generate Shopping List")
        occasion = st.selectbox("Select occasion", ["Family Week", "Braai Weekend", "Budget Month"])
        budget = st.slider("Budget (ZAR)", 200, 1000, 500)
        
        if st.button("Generate List", type="primary"):
            st.success(f"Generated {occasion} shopping list for R{budget}!")
            st.markdown("""
            - Chicken Breast (2kg)
            - Mixed Vegetables
            - Maize Meal (5kg)
            - Cooking Oil
            - Brown Bread
            - Milk (4L)
            """)
    
    with tab2:
        st.markdown("### Predict Delivery Time")
        location = st.text_input("Your Location", "Soweto")
        if location and st.button("Predict"):
            st.info(f"Estimated delivery to {location}: 2-3 hours")

# Testimonials
def show_testimonials():
    st.markdown("## 💬 Customer Reviews")
    cols = st.columns(3)
    reviews = [
        {"name": "Thandiwe M.", "text": "Life-changing service! Saves me hours every week.", "stars": 5},
        {"name": "James K.", "text": "Fresh produce delivered to my door. Quality is excellent.", "stars": 5},
        {"name": "Nomsa P.", "text": "Affordable prices and reliable delivery.", "stars": 4},
    ]
    
    for idx, review in enumerate(reviews):
        with cols[idx]:
            st.markdown(f"""
            <div class='modern-card'>
                <h4>{review['name']}</h4>
                <p>{"⭐" * review['stars']}</p>
                <p><i>"{review['text']}"</i></p>
                <p style='color:#2E8B57;font-size:0.9em'>✅ Verified Purchase</p>
            </div>
            """, unsafe_allow_html=True)

# Main App
def main():
    create_nav()
    create_hero()
    show_ai_features()
    show_products()
    show_testimonials()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align:center;color:#666;padding:20px'>
        <p>📍 Serving: Soweto, Alexandra, Khayelitsha, Gugulethu, Mamelodi</p>
        <p>© 2024 Yebo Fresh | Fresh Groceries Delivered</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
