import pandas as pd
import streamlit as st

# Ρύθμιση σελίδας
st.set_page_config(
    page_title="ΚΠΕ Ακρωτηρίου - Application & Priority Manager",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS για το πράσινοστυλ του ΚΠΕ
st.markdown(
    """
    <style>
    .main-header {
        background-color: #115e3b;
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin-bottom: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Κεφαλίδα εφαρμογής
st.markdown(
    """
    <div class="main-header">
        <h1>🌱 ΚΠΕ Akrotiriou - Application & Priority Manager</h1>
        <p>Κέντρο Περιβαλλοντικής Εκπαίδευσης Ακρωτηρίου • Υπουργείο Παιδείας, Αθλητισμού & Νεολαίας</p>
    </div>
""",
    unsafe_allow_html=True,
)

# Tabs / Καρτέλες συστήματος
tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📋 Αιτήσεις Σχολείων",
        "📅 Ημερολόγιος & Προγραμματισμός",
        "📊 Στατιστικά & Προγράμματα",
        "⚙️ Βαθμίδες & Priority Dashboard",
    ]
)

with tab1:
  st.subheader("Διαχείριση & Προβολή Αιτήσεων Σχολείων")

  # Φόρτωση δεδομένων από τα Excel που υπάρχουν στο GitHub
  selected_file = st.selectbox(
      "Επιλέξτε αρχείο δεδομένων:",
      ["Απαντήσεις (15).xlsx", "Απαντήσεις (16).xlsx", "Απαντήσεις (17).xlsx"],
  )

  try:
    df = pd.read_excel(selected_file)

    # Metrics Overview
    col1, col2, col3, col4 = st.columns(4)
    with col1:
      st.metric("ΣΥΝΟΛΟ ΑΙΤΗΣΕΩΝ", len(df))
    with col2:
      st.metric("ΕΚΚΡΕΜΕΙΣ", len(df))
    with col3:
      st.metric("ΟΡΙΣΜΕΝΕΣ", 0)
    with col4:
      st.metric("ΣΥΝΔΥΑΣΜΕΝΕΣ", 0)

    st.divider()

    # Αναζήτηση και φίλτρα
    search_query = st.text_input(
        "🔍 Αναζήτηση σχολείου, εκπαιδευτικού, προγράμματος"
    )

    if search_query:
      # Φιλτράρισμα βάσει αναζήτησης (αν υπάρχουν οι στήλες)
      filtered_df = df[
          df.astype(str)
          .apply(lambda x: x.str.contains(search_query, case=False))
          .any(axis=1)
      ]
    else:
      filtered_df = df

    st.dataframe(filtered_df, use_container_width=True)

  except Exception as e:
    st.error(
        f"Δεν ήταν δυνατή η φόρτωση του αρχείου {selected_file}. Σφάλμα: {e}"
    )

with tab2:
  st.subheader("Ημερολόγιος & Προγραμματισμός Επισκέψεων")
  st.info("Εδώ θα εμφανίζεται το ημερολόγιο προγραμματισμού των σχολείων.")

with tab3:
  st.subheader("Στατιστικά Στοιχεία & Αναφορές")
  st.write("Συγκεντρωτικά γραφήματα και δεδομένα προγραμμάτων ΚΠΕ.")

with tab4:
  st.subheader("Βαθμίδες & Priority Dashboard")
  st.write("Διαχείριση προτεραιοτήτων ανά σχολική βαθμίδα.")
