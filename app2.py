import streamlit as st
import json
import os
from datetime import datetime
import random

# Cipher
CIPHER = {
    'a': 'u', 'b': '17', 'c': 'k', 'd': '9', 'e': 'x',
    'f': '23', 'g': 'q', 'h': '5', 'i': 'w', 'j': '14',
    'k': 'z', 'l': '8', 'm': 'p', 'n': '3', 'o': 'y',
    'p': '19', 'q': 'v', 'r': '7', 's': '2', 't': '11',
    'u': 'm', 'v': '16', 'w': 'f', 'x': '21', 'y': '4',
    'z': '13', ' ': '_'
}

def encrypt(text):
    return '-'.join(CIPHER.get(c.lower(), c) for c in text)

def decrypt(text):
    DECIPHER = {v: k for k, v in CIPHER.items()}
    return ''.join(DECIPHER.get(part, part) for part in text.split('-'))

# Quotes collection
QUOTES = [
    "The name's Bond. James Bond.",
    "शांति परमो धर्मः - Peace is the highest dharma",
    "Yoga is the journey of the self, through the self, to the self. - Bhagavad Gita",
    "Justice delayed is justice denied.",
    "The mind is everything. What you think you become. - Buddha",
    "In matters of truth and justice, there is no difference between large and small problems.",
    "Stillness is where creativity and solutions are found.",
    "The law is reason, free from passion. - Aristotle",
    "Clarity comes from stillness, not from constant motion.",
    "Intelligence is the ability to adapt to change."
]

# Page config
st.set_page_config(
    page_title="App",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with BLACK TABS
st.markdown("""
<style>
    .main-header {
        font-size: 42px;
        font-weight: 300;
        color: #2c3e50;
        text-align: center;
        padding: 40px 0 10px 0;
        letter-spacing: 2px;
    }
    .sub-header {
        font-size: 16px;
        color: #7f8c8d;
        text-align: center;
        padding-bottom: 30px;
        font-weight: 300;
    }
    .quote-box {
        background: #f8f9fa;
        padding: 20px;
        border-left: 4px solid #2c3e50;
        margin: 20px 0;
        font-style: italic;
        color: #555;
    }
    .metric-card {
        background: white;
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* BLACK TABS WITH WHITE TEXT - NO HOVER */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0px;
        background: #1a1a1a;
        padding: 15px 20px;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.3);
        justify-content: space-between;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #2c2c2c !important;
        border-radius: 8px;
        padding: 18px 60px;
        font-weight: 600;
        font-size: 19px;
        flex: 1;
        text-align: center;
        color: white !important;
        border: none !important;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #2c2c2c !important;
        color: white !important;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: #000000 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Password protection
def check_password():
    def password_entered():
        if st.session_state["password"] == "Venkatachalapathi6!":
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown("<h1 class='main-header'>Hey Vidhya Prakash, How are you doing?</h1>", unsafe_allow_html=True)
        st.markdown("<p class='sub-header'>This app belongs to VP!</p>", unsafe_allow_html=True)
        
        # Random quote
        quote = random.choice(QUOTES)
        st.markdown(f"<div class='quote-box'>{quote}</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.text_input("Access Code", type="password", on_change=password_entered, key="password", label_visibility="collapsed", placeholder="Enter access code")
        return False
    elif not st.session_state["password_correct"]:
        st.markdown("<h1 class='main-header'>SECURE VAULT</h1>", unsafe_allow_html=True)
        st.markdown("<p class='sub-header'>Protected Records System</p>", unsafe_allow_html=True)
        
        quote = random.choice(QUOTES)
        st.markdown(f"<div class='quote-box'>{quote}</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.text_input("Access Code", type="password", on_change=password_entered, key="password", label_visibility="collapsed", placeholder="Enter access code")
            st.error("Access Denied")
        return False
    else:
        return True

if not check_password():
    st.stop()

# Load data
DATA_FILE = 'ledger.json'
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as f:
        records = json.load(f)
else:
    records = []

# Welcome message after login
current_hour = datetime.now().hour
if current_hour < 12:
    greeting = "Good Morning"
elif current_hour < 17:
    greeting = "Good Afternoon"
else:
    greeting = "Good Evening"

st.markdown(f"""
<div style='background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%); padding: 30px; border-radius: 8px; margin-bottom: 30px;'>
    <h2 style='color: white; margin: 0; font-weight: 300; letter-spacing: 1px;'>{greeting}, Vidhya Prakash</h2>
    <p style='color: #bdc3c7; margin-top: 8px; margin-bottom: 0;'>{datetime.now().strftime("%A, %B %d, %Y")}</p>
</div>
""", unsafe_allow_html=True)

# Random daily quote
daily_quote = random.choice(QUOTES)
st.markdown(f"""
<div style='background: #ecf0f1; padding: 15px 20px; border-left: 3px solid #2c3e50; margin-bottom: 30px; border-radius: 4px;'>
    <p style='margin: 0; color: #555; font-style: italic;'>{daily_quote}</p>
</div>
""", unsafe_allow_html=True)

# Tabs with even spacing
tab1, tab2, tab3, tab4 = st.tabs(["Create", "Update", "View", "Delete"])

# TAB 1: Create Entry
with tab1:
    st.markdown("### Create New Record")
    
    col1, col2 = st.columns(2)
    
    with col1:
        place = st.text_input("Location *", key="create_place", help="Required")
        name = st.text_input("Name *", key="create_name", help="Required")
        month = st.text_input("Month", key="create_month")
        initial_date = st.text_input("Initial Date", key="create_date")
        year = st.text_input("Year", key="create_year")
    
    with col2:
        interest = st.text_input("Interest", key="create_interest")
        paid = st.text_input("Paid", key="create_paid")
        balance = st.text_input("Balance", key="create_balance")
        bank = st.text_input("Bank", key="create_bank")
        payment_date = st.text_input("Payment Date (DD/MM/YYYY)", key="create_payment")
    
    if st.button("Save Record", type="primary", use_container_width=True):
        if place and name:
            record = {
                'place': encrypt(place),
                'name': encrypt(name),
                'month': encrypt(month) if month else '',
                'initial_date': initial_date,
                'year': year,
                'interest': interest,
                'paid': paid,
                'balance': balance,
                'bank': encrypt(bank) if bank else '',
                'payment_date': payment_date
            }
            records.append(record)
            
            with open(DATA_FILE, 'w') as f:
                json.dump(records, f, indent=2)
            
            st.success("Record saved successfully")
        else:
            st.error("Location and Name are required")

# TAB 2: Update Entry
with tab2:
    st.markdown("### Update Existing Record")
    
    if not records:
        st.info("No records available. Create a record first.")
    else:
        col1, col2 = st.columns(2)
        with col1:
            search_name = st.text_input("Search by Name *", key="search_name")
        with col2:
            search_place = st.text_input("Search by Location *", key="search_place")
        
        if st.button("Find Record", use_container_width=True):
            found_idx = None
            for idx, r in enumerate(records):
                if decrypt(r['name']).lower() == search_name.lower() and decrypt(r['place']).lower() == search_place.lower():
                    found_idx = idx
                    break
            
            if found_idx is not None:
                st.session_state['update_idx'] = found_idx
                st.success(f"Record found: {search_name} at {search_place}")
            else:
                st.error("No matching record found")
                st.session_state['update_idx'] = None
        
        if 'update_idx' in st.session_state and st.session_state['update_idx'] is not None:
            idx = st.session_state['update_idx']
            r = records[idx]
            
            st.markdown("---")
            st.caption(f"Updating: {decrypt(r['name'])} - {decrypt(r['place'])}")
            
            col1, col2 = st.columns(2)
            
            with col1:
                new_place = st.text_input("Location", value=decrypt(r['place']), key="update_place")
                new_name = st.text_input("Name", value=decrypt(r['name']), key="update_name")
                new_month = st.text_input("Month", value=decrypt(r['month']) if r['month'] else '', key="update_month")
                new_initial_date = st.text_input("Initial Date", value=r['initial_date'], key="update_date")
                new_year = st.text_input("Year", value=r['year'], key="update_year")
            
            with col2:
                new_interest = st.text_input("Interest", value=r['interest'], key="update_interest")
                new_paid = st.text_input("Paid", value=r['paid'], key="update_paid")
                new_balance = st.text_input("Balance", value=r['balance'], key="update_balance")
                new_bank = st.text_input("Bank", value=decrypt(r['bank']) if r['bank'] else '', key="update_bank")
                new_payment_date = st.text_input("Payment Date", value=r['payment_date'], key="update_payment")
            
            if st.button("Update Record", type="primary", use_container_width=True):
                if new_place and new_name:
                    records[idx] = {
                        'place': encrypt(new_place),
                        'name': encrypt(new_name),
                        'month': encrypt(new_month) if new_month else '',
                        'initial_date': new_initial_date,
                        'year': new_year,
                        'interest': new_interest,
                        'paid': new_paid,
                        'balance': new_balance,
                        'bank': encrypt(new_bank) if new_bank else '',
                        'payment_date': new_payment_date
                    }
                    
                    with open(DATA_FILE, 'w') as f:
                        json.dump(records, f, indent=2)
                    
                    st.success("Record updated successfully")
                    del st.session_state['update_idx']
                    st.rerun()
                else:
                    st.error("Location and Name are required")

# TAB 3: View Ledger
with tab3:
    # Header with inline total records
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("### Records Overview")
    with col2:
        if records:
            st.markdown(f"""
            <div style='text-align: right; padding-top: 8px;'>
                <span style='color: #6c757d; font-size: 18px; font-weight: 500;'>Total: </span>
                <span style='color: #2c3e50; font-size: 36px; font-weight: 700;'>{len(records)}</span>
            </div>
            """, unsafe_allow_html=True)
    
    if records:
        st.markdown("---")
        st.markdown("### Export Options")
        
        col1, col2, col3, col4 = st.columns(4)
        
        # 1. Encrypted text
        with col1:
            line_width = 140
            encrypted_text = "ENCRYPTED RECORDS\n" + "="*line_width + "\n\n"
            encrypted_text += f"{'LOC':<18} | {'NAME':<18} | {'MTH':<10} | {'DT':<4} | {'YR':<4} | {'INT':<7} | {'PD':<7} | {'BAL':<7} | {'BANK':<18} | {'PMT':<11}\n"
            encrypted_text += "="*line_width + "\n"
            
            for r in records:
                encrypted_text += f"{r['place']:<18} | {r['name']:<18} | {r['month']:<10} | {r['initial_date']:<4} | {r['year']:<4} | {r['interest']:<7} | {r['paid']:<7} | {r['balance']:<7} | {r['bank']:<18} | {r['payment_date']:<11}\n"
                encrypted_text += "-"*line_width + "\n"
            
            st.download_button(
                label="Encrypted Text",
                data=encrypted_text,
                file_name="records_encrypted.txt",
                mime="text/plain",
                use_container_width=True
            )
        
        # 2. Encrypted Word
        with col2:
            html_encrypted = """
            <html>
            <head>
                <style>
                    body { font-family: 'Segoe UI', Tahoma, sans-serif; margin: 40px; }
                    h1 { text-align: center; color: #2c3e50; font-weight: 300; letter-spacing: 2px; margin-bottom: 10px; }
                    .meta { text-align: center; color: #7f8c8d; margin-bottom: 40px; font-size: 14px; }
                    table { width: 100%; border-collapse: collapse; margin-top: 20px; table-layout: fixed; }
                    th, td { border: 1px solid #ADD8E6; padding: 10px 6px; text-align: left; font-size: 10px; word-wrap: break-word; }
                    th { background-color: #34495e; color: white; font-weight: 500; white-space: nowrap; }
                    tr:nth-child(even) { background-color: #f8f9fa; }
                    tr:hover { background-color: #e9ecef; }
                    .col-location, .col-name, .col-bank { width: 14%; }
                    .col-month { width: 9%; }
                    .col-date, .col-year { width: 5%; }
                    .col-interest, .col-paid, .col-balance { width: 7%; }
                    .col-payment { width: 9%; }
                </style>
            </head>
            <body>
                <h1>ENCRYPTED RECORDS</h1>
                <p class='meta'>Generated: """ + datetime.now().strftime("%B %d, %Y at %I:%M %p") + """</p>
                <table>
                    <tr>
                        <th class='col-location'>Location</th>
                        <th class='col-name'>Name</th>
                        <th class='col-month'>Month</th>
                        <th class='col-date'>Date</th>
                        <th class='col-year'>Year</th>
                        <th class='col-interest'>Interest</th>
                        <th class='col-paid'>Paid</th>
                        <th class='col-balance'>Balance</th>
                        <th class='col-bank'>Bank</th>
                        <th class='col-payment'>Payment</th>
                    </tr>
            """
            
            for r in records:
                html_encrypted += f"""
                    <tr>
                        <td class='col-location'>{r['place']}</td>
                        <td class='col-name'>{r['name']}</td>
                        <td class='col-month'>{r['month']}</td>
                        <td class='col-date'>{r['initial_date']}</td>
                        <td class='col-year'>{r['year']}</td>
                        <td class='col-interest'>{r['interest']}</td>
                        <td class='col-paid'>{r['paid']}</td>
                        <td class='col-balance'>{r['balance']}</td>
                        <td class='col-bank'>{r['bank']}</td>
                        <td class='col-payment'>{r['payment_date']}</td>
                    </tr>
                """
            
            html_encrypted += """
                </table>
            </body>
            </html>
            """
            
            st.download_button(
                label="Encrypted Word",
                data=html_encrypted,
                file_name="records_encrypted.doc",
                mime="application/msword",
                use_container_width=True
            )
        
        # 3. Decrypted text
        with col3:
            line_width = 140
            decrypted_text = "DECRYPTED RECORDS\n" + "="*line_width + "\n\n"
            decrypted_text += f"{'LOC':<18} | {'NAME':<18} | {'MTH':<10} | {'DT':<4} | {'YR':<4} | {'INT':<7} | {'PD':<7} | {'BAL':<7} | {'BANK':<18} | {'PMT':<11}\n"
            decrypted_text += "="*line_width + "\n"
            
            for r in records:
                decrypted_text += f"{decrypt(r['place']):<18} | {decrypt(r['name']):<18} | {decrypt(r['month']) if r['month'] else '':<10} | {r['initial_date']:<4} | {r['year']:<4} | {r['interest']:<7} | {r['paid']:<7} | {r['balance']:<7} | {decrypt(r['bank']) if r['bank'] else '':<18} | {r['payment_date']:<11}\n"
                decrypted_text += "-"*line_width + "\n"
            
            st.download_button(
                label="Decrypted Text",
                data=decrypted_text,
                file_name="records_decrypted.txt",
                mime="text/plain",
                use_container_width=True
            )
        
        # 4. Decrypted Word
        with col4:
            html_decrypted = """
            <html>
            <head>
                <style>
                    body { font-family: 'Segoe UI', Tahoma, sans-serif; margin: 40px; }
                    h1 { text-align: center; color: #27ae60; font-weight: 300; letter-spacing: 2px; margin-bottom: 10px; }
                    .meta { text-align: center; color: #7f8c8d; margin-bottom: 40px; font-size: 14px; }
                    table { width: 100%; border-collapse: collapse; margin-top: 20px; table-layout: fixed; }
                    th, td { border: 1px solid #ADD8E6; padding: 10px 6px; text-align: left; word-wrap: break-word; }
                    th { background-color: #27ae60; color: white; font-weight: 500; white-space: nowrap; }
                    tr:nth-child(even) { background-color: #f8f9fa; }
                    tr:hover { background-color: #e9ecef; }
                    .col-location, .col-name, .col-bank { width: 14%; }
                    .col-month { width: 9%; }
                    .col-date, .col-year { width: 5%; }
                    .col-interest, .col-paid, .col-balance { width: 7%; }
                    .col-payment { width: 9%; }
                </style>
            </head>
            <body>
                <h1>DECRYPTED RECORDS</h1>
                <p class='meta'>Generated: """ + datetime.now().strftime("%B %d, %Y at %I:%M %p") + """</p>
                <table>
                    <tr>
                        <th class='col-location'>Location</th>
                        <th class='col-name'>Name</th>
                        <th class='col-month'>Month</th>
                        <th class='col-date'>Date</th>
                        <th class='col-year'>Year</th>
                        <th class='col-interest'>Interest</th>
                        <th class='col-paid'>Paid</th>
                        <th class='col-balance'>Balance</th>
                        <th class='col-bank'>Bank</th>
                        <th class='col-payment'>Payment</th>
                    </tr>
            """
            
            for r in records:
                html_decrypted += f"""
                    <tr>
                        <td class='col-location'>{decrypt(r['place'])}</td>
                        <td class='col-name'>{decrypt(r['name'])}</td>
                        <td class='col-month'>{decrypt(r['month']) if r['month'] else ''}</td>
                        <td class='col-date'>{r['initial_date']}</td>
                        <td class='col-year'>{r['year']}</td>
                        <td class='col-interest'>{r['interest']}</td>
                        <td class='col-paid'>{r['paid']}</td>
                        <td class='col-balance'>{r['balance']}</td>
                        <td class='col-bank'>{decrypt(r['bank']) if r['bank'] else ''}</td>
                        <td class='col-payment'>{r['payment_date']}</td>
                    </tr>
                """
            
            html_decrypted += """
                </table>
            </body>
            </html>
            """
            
            st.download_button(
                label="Decrypted Word",
                data=html_decrypted,
                file_name="records_decrypted.doc",
                mime="application/msword",
                use_container_width=True
            )
    else:
        st.info("No records available")

# TAB 4: Delete Entry
with tab4:
    st.markdown("### Delete Record")
    
    if records:
        st.warning("Warning: This action cannot be undone")
        
        delete_options = [f"Record {i+1}: {decrypt(r['name'])} - {decrypt(r['place'])}" for i, r in enumerate(records)]
        selected = st.selectbox("Select record to delete", delete_options)
        
        if st.button("Delete Record", type="secondary", use_container_width=True):
            idx = int(selected.split("Record ")[1].split(":")[0]) - 1
            deleted = records.pop(idx)
            
            with open(DATA_FILE, 'w') as f:
                json.dump(records, f, indent=2)
            
            st.success(f"Deleted: {decrypt(deleted['name'])}")
            st.rerun()
    else:
        st.info("No records to delete")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #95a5a6; padding: 15px;'>
    <p style='font-size: 13px; margin: 0;'>Secure Records System • Protected by encryption</p>
</div>
""", unsafe_allow_html=True)




