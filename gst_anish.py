import streamlit as st

st.title("GST CALCULATOR")

original_amount = st.number_input("Enter the amount:", min_value=0.00, format="%.2f")

gst_rate=18
if st.button("CALCULATE"):
    if original_amount>0:
            gst_amount = (original_amount*18)/100
            total_price = original_amount + gst_amount
        
            #display the result
            st.write(f"GST Amount: Rs.{gst_amount:.2f}")
            st.write(f"Total Price after GST: Rs.{total_price:.2f}")
    else:
        print("Enter the amount greater than Rs.0.00 !..")