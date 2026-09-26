import pandas as pd
import streamlit as st

# Ρύθμιση σελίδας (Wide layout)
st.set_page_config(
    page_title="ΚΠΕ Ακρωτηρίου - Application & Priority Manager",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS για να μοιάζει ακριβώς με το AI Studio (πράσινοheader & κάρτες)
st.markdown(
    """
    <style>
    .main-container {
        background-color: #115e3b;
        padding: 25px;
        border-radius: 12px;
        color: white;
        margin-bottom: 25px;
    }
    .metric-card {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        text-align: center;
        color: #333333;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Πάνω μέρος: Κεφαλίδα & Κουμπιά Ενέργειας
header_col1, header_col2 = st.columns([3, 2])

with header_col1:
  st.markdown(
      """
        <div style="background-color: #115e3b; padding: 20px; border-radius: 10px; color: white;">
            <h2>🌱 ΚΠΕ Ακρωτηρίου - Application & Priority Manager</h2>
            <p style="margin: 0; font-size: 14px;">Κέντρο Περιβαλλοντικής Εκπαίδευσης Ακρωτηρίου • Υπουργείο Παιδείας, Αθλητισμού & Νεολαίας</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

with header_col2:
  st.write("")  # Κενό για στοίχιση
  b1, b2, b3 = st.columns(3)
  with b1:
    if st.button("➕ Νέα Αίτηση"):
      st.info("Λειτουργία προσθήκης νέας αίτησης")
  with b2:
    if st.button("📥 Εισαγωγή"):
      st.info("Εισαγωγή αρχείου")
  with b3:
    if st.button("📤 Εξαγωγή"):
      st.info("Εξαγωγή δεδομένων")

# Tabs συστήματος ακριβώς όπως στο design
tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📋 Αιτήσεις Σχολείων",
        "📅 Ημερολόγιος & Προγραμματισμός",
        "📊 Στατιστικά & Προγράμματα",
        "⚙️ Βαθμίδες & Priority Dashboard",
    ]
)

with tab1:
  # Επιλογή αρχείου Excel
  selected_file = st.selectbox(
      "Επιλέξτε αρχείο δεδομένων:",
      ["Απαντήσεις (15).xlsx", "Απαντήσεις (16).xlsx", "Απαντήσεις (17).xlsx"],
  )

  try:
    df = pd.read_excel(selected_file)
    total_records = len(df)
  except:
    df = pd.DataFrame()
    total_records = 0

  # Στατιστικές κάρτες (Metrics) πάνω από τον πίνακα
  m1, m2, m3, m4, m5 = st.columns(5)
  with m1:
    st.metric(label="ΣΥΝΟΛΟ ΑΙΤΗΣΕΩΝ", value=total_records)
  with m2:
    st.metric(label="ΣΥΝΟΛΟ ΜΑΘΗΤΩΝ", value="2,447")
  with m3:
    st.metric(label="ΟΡΙΣΜΕΝΕΣ ΗΜΕΡΟΜΗΝΙΕΣ", value="0")
  with m4:
    st.metric(label="ΕΚΚΡΕΜΕΙΣ ΗΜΕΡΟΜΗΝΙΑ", value=total_records)
  with m5:
    st.metric(label="ΣΥΝΔΥΑΣΜΕΝΕΣ ΕΠΙΣΚΕΨΕΙΣ", value="0")

  st.divider()

  # Γραμμή Αναζήτησης
  search_query = st.text_input(
      "🔍 Αναζήτηση σχολείου, εκπαιδευτικού, προγράμματος", ""
  )

  # Φίλτρα σε σειρές (Κατάσταση, Πρόγραμμα, Επαρχία, Βαθμίδα)
  f1, f2, f3, f4, f5 = st.columns(5)
  with f1:
    st.selectbox("Κατάσταση:", ["Όλες οι καταστάσεις", "Υποβληθείσα", "Εγκριθείσα"])
  with f2:
    st.selectbox("Πρόγραμμα ΚΠΕ:", ["Όλα τα προγράμματα"])
  with f3:
    st.selectbox("Επαρχία:", ["Όλες οι επαρχίες", "Λεμεσός", "Λευκωσία"])
  with f4:
    st.selectbox("Βαθμίδα:", ["Όλες οι βαθμίδες", "Δημοτική", "Μέση"])
  with f5:
    st.selectbox("Προγραμματισμός:", ["Όλες οι αιτήσεις"])

  st.write("")

  # Φιλτράρισμα και εμφάνιση πίνακα
  if search_query and not df.empty:
    filtered_df = df[
        df.astype(str)
        .apply(lambda x: x.str.contains(search_query, case=False))
        .any(axis=1)
    ]
  else:
    filtered_df = df

  if not filtered_df.empty:
    st.dataframe(filtered_df, use_container_width=True)
  else:
    st.warning("Δεν βρέθηκαν δεδομένα ή το αρχείο είναι κενό.")

with tab2:
  st.subheader("📅 Ημερολόγιος & Προγραμματισμός")
  st.info("Διαχείριση ημερομηνιών και επισκέψεων σχολείων.")

with tab3:
  st.subheader("📊 Στατιστικά & Προγράμματα")
  st.write("Συγκεντρωτικές αναφορές και γραφήματα.")

with tab4:
  st.subheader("⚙️ Βαθμίδες & Priority Dashboard")
  st.write("Διαχείριση προτεραιοτήτων και μορίων ανά βαθμίδα.")
