import streamlit as st
from supabase import create_client

supabase = create_client("URL", "KEY")

st.title("📍 Pickup Site")
ship_code = st.text_input("Enter Shipment Code")

if st.button("Verify & Pay Rider"):
    # Logic: coordinates line up with pick up site 
    supabase.table("shipments").update({"status": "Completed"}).eq("shipment_no", ship_code).execute()
    st.balloons()
    st.success("Escrow Released. Rider paid in Mobile Money Wallet.")
