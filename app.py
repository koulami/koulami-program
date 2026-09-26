import pandas as pd
import streamlit as st

# Ρύθμιση σελίδας (Wide layout)
st.set_page_config(
    page_title="KPE Akrotiriou - Application & Priority Manager",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS για το πράσινο design και τις κάρτες
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f8f9fa;
    }
    .top-header {
        background-color: #115e3b;
        padding: 15px 25px;
        border-radius: 10px;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .metric-card {
        background-color: white;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border: 1px solid #e2e8f0;
    }
    .priority-box {
        background-color: #0b3c24;
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin-top: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- ΠΑΝΩ ΜΕΡΟΣ: ΚΕΦΑΛΙΔΑ & ΚΟΥΜΠΙΑ ---
col_logo, col_btns = st.columns([2.5, 2])

with col_logo:
  st.markdown(
      """
        <div style="background-color: #115e3b; padding: 15px 20px; border-radius: 10px; color: white;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 24px;">🌱</span>
                <div>
                    <h2 style="margin: 0; font-size: 20px; font-weight: bold;">KPE Akrotiriou - Application & Priority Manager</h2>
                    <p style="margin: 3px 0 0 0; font-size: 12px; opacity: 0.9;">Κέντρο Περιβαλλοντικής Εκπαίδευσης Ακρωτηρίου • Υπουργείο Παιδείας, Αθλητισμού & Νεολαίας</p>
                </div>
            </div>
        </div>
    """,
      unsafe_allow_html=True,
  )

with col_btns:
  c1, c2, c3, c4, c5 = st.columns([1, 1.2, 1.2, 1.2, 0.8])
  with c1:
    st.markdown(
        "<div style='background-color: #115e3b; color: white; padding: 8px"
        " 12px; border-radius: 20px; text-align: center; font-size: 12px;'"
        ">2026-2027</div>",
        unsafe_allow_html=True,
    )
  with c2:
    if st.button("➕ Νέα Αίτηση", use_container_width=True):
      st.toast("Άνοιγμα φόρμας νέας αίτησης...")
  with c3:
    if st.button("📥 Εισαγωγή", use_container_width=True):
      st.toast("Εισαγωγή αρχείου...")
  with c4:
    if st.button("📤 Εξαγωγή", use_container_width=True):
      st.toast("Εξαγωγή CSV...")
  with c5:
    if st.button("⚙️", help="System Management"):
      pass

st.write("")

# --- TABS ΣΥΣΤΗΜΑΤΟΣ ---
tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📋 Αιτήσεις Σχολείων (65)",
        "📅 Ημερολόγιος & Προγραμματισμός",
        "📊 Στατιστικά & Προγράμματα",
        "⚙️ Βαθμίδες & Priority Dashboard",
    ]
)

with tab1:
  # --- ΚΑΡΤΕΣ ΣΤΑΤΙΣΤΙΚΩΝ ---
  m1, m2, m3, m4, m5 = st.columns(5)
  with m1:
    st.markdown(
        """<div class="metric-card">
            <span style="font-size: 11px; color: #64748b; font-weight: bold;">ΣΥΝΟΛΟ ΑΙΤΗΣΕΩΝ</span>
            <h3 style="margin: 5px 0 0 0; color: #0f172a;">65 <span style="font-size: 12px; font-weight: normal; color: #64748b;">σχολικά τμήματα</span></h3>
        </div>""",
        unsafe_allow_html=True,
    )
  with m2:
    st.markdown(
        """<div class="metric-card">
            <span style="font-size: 11px; color: #64748b; font-weight: bold;">ΣΥΝΟΛΟ ΜΑΘΗΤΩΝ</span>
            <h3 style="margin: 5px 0 0 0; color: #0f172a;">2,447 <span style="font-size: 12px; font-weight: normal; color: #64748b;">μαθητές/τρίες</span></h3>
        </div>""",
        unsafe_allow_html=True,
    )
  with m3:
    st.markdown(
        """<div class="metric-card">
            <span style="font-size: 11px; color: #64748b; font-weight: bold;">ΟΡΙΣΜΕΝΕΣ ΗΜΕΡΟΜΗΝΙΕΣ</span>
            <h3 style="margin: 5px 0 0 0; color: #0f172a;">0 <span style="font-size: 12px; font-weight: normal; color: #64748b;">(0 εγκεκριμένες)</span></h3>
        </div>""",
        unsafe_allow_html=True,
    )
  with m4:
    st.markdown(
        """<div class="metric-card">
            <span style="font-size: 11px; color: #64748b; font-weight: bold;">ΕΚΚΡΕΜΕΙΣ ΗΜΕΡΟΜΗΝΙΑ</span>
            <h3 style="margin: 5px 0 0 0; color: #0f172a;">65 <span style="font-size: 12px; font-weight: normal; color: #64748b;">προς κατανομή</span></h3>
        </div>""",
        unsafe_allow_html=True,
    )
  with m5:
    st.markdown(
        """<div class="metric-card">
            <span style="font-size: 11px; color: #64748b; font-weight: bold;">ΣΥΝΔΥΑΣΜΕΝΕΣ ΕΠΙΣΚΕΨΕΙΣ</span>
            <h3 style="margin: 5px 0 0 0; color: #0f172a;">0 <span style="font-size: 12px; font-weight: normal; color: #64748b;">αιτήματα κοινής μεταφοράς</span></h3>
        </div>""",
        unsafe_allow_html=True,
    )

  st.write("")

  # --- ΑΝΑΖΗΤΗΣΗ & ΦΙΛΤΡΑ ---
  search_query = st.text_input(
      "🔍",
      placeholder="Αναζήτηση σχολείου, εκπαιδευτικού, προγράμματος",
      label_visibility="collapsed",
  )

  f1, f2, f3, f4, f5 = st.columns(5)
  with f1:
    st.selectbox(
        "Κατάσταση",
        ["Όλες οι καταστάσεις", "Υποβληθείσα", "Εγκριθείσα"],
        label_visibility="collapsed",
    )
  with f2:
    st.selectbox(
        "Πρόγραμμα ΚΠΕ", ["Όλα τα προγράμματα"], label_visibility="collapsed"
    )
  with f3:
    st.selectbox(
        "Επαρχία",
        ["Όλες οι επαρχίες", "Λεμεσός", "Λευκωσία"],
        label_visibility="collapsed",
    )
  with f4:
    st.selectbox(
        "Βαθμίδα",
        ["Όλες οι βαθμίδες", "Δημοτική", "Μέση Εκπαίδευση", "Νηπιαγωγεία"],
        label_visibility="collapsed",
    )
  with f5:
    st.selectbox(
        "Προγραμματισμός", ["Όλες οι αιτήσεις"], label_visibility="collapsed"
    )

  # Γρήγορα Φίλτρα (Quick Filters)
  q1, q2, q3, q4, q5 = st.columns([1.2, 1.2, 1.5, 2.2, 3])
  with q1:
    st.button("🟢 Δημοτικά", use_container_width=True)
  with q2:
    st.button("🟡 Νηπιαγωγεία", use_container_width=True)
  with q3:
    st.button("🔵 Μέση Εκπαίδευση", use_container_width=True)
  with q4:
    st.button("🟣 Σχολεία με πολλαπλές αιτήσεις", use_container_width=True)

  st.divider()

  # --- ΦΟΡΤΩΣΗ ΚΑΙ ΠΡΟΒΟΛΗ ΔΕΔΟΜΕΝΩΝ ΑΠΟ EXCEL ---
  try:
    df = pd.read_excel("Απαντήσεις (15).xlsx")
  except:
    df = pd.DataFrame(
        {
            "Σειρά": ["#1", "#2", "#3", "#4"],
            "Κωδικός & Σχολείο": [
                "ΠΕΡΙΦΕΡΕΙΑΚΟ ΛΥΚΕΙΟ ΑΠΟΣΤΟΛΟΥ ΛΟΥΚΑ ΚΟΛΟΣΣΙΟΥ",
                "ΔΗΜΟΤΙΚΟ ΣΧΟΛΕΙΟ ΠΑΡΑΜΥΘΑΣ - ΣΠΙΤΑΛΙΟΥ",
                "ΔΗΜΟΤΙΚΟ ΣΧΟΛΕΙΟ ΠΟΤΑΜΟΥ ΓΕΡΜΑΣΟΓΕΙΑΣ Β΄",
                "ΔΗΜΟΤΙΚΟ ΣΧΟΛΕΙΟ ΣΟΥΝΙΟΥ ΖΑΝΑΚΙΑΣ",
            ],
            "Πρόγραμμα ΚΠΕ": [
                "ΟΙΚΟΣΥΣΤΗΜΑΤΑ: ΧΛΩΡΙΔΑ - ΠΑΝΙΔΑ",
                "ΝΕΡΟ - ΥΓΡΟΒΙΟΤΟΠΟΙ - ΘΑΛΑΣΣΑ",
                "ΝΕΡΟ - ΥΓΡΟΒΙΟΤΟΠΟΙ - ΘΑΛΑΣΣΑ",
                "ΝΕΡΟ - ΥΓΡΟΒΙΟΤΟΠΟΙ - ΘΑΛΑΣΣΑ",
            ],
            "Μαθητές": ["0 (Α24 - 25 παιδιά)", "27", "71", "27"],
            "Κατάσταση": ["Υποβληθείσα", "Υποβληθείσα", "Υποβληθείσα", "Υποβληθείσα"],
        }
    )

  st.dataframe(df, use_container_width=True)

  # --- ΕΝΙΑΙΟΣ ΠΙΝΑΚΑΣ ΠΡΟΤΕΡΑΙΟΤΗΤΑΣ & ΒΑΘΜΙΔΩΝ (ΚΑΤΩ ΜΕΡΟΣ) ---
  st.markdown(
      """
        <div class="priority-box">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <h4 style="margin: 0; color: white;">🛡️ Ενιαίος Πίνακας Προτεραιότητας & Βαθμίδων</h4>
                    <p style="margin: 5px 0 0 0; font-size: 12px; color: #cbd5e1;">Χρονολογική κατάταξη πρώτης υποβολής (index + 1) και αυτόματη ταξινόμηση Βαθμίδας (classify_school_level).</p>
                </div>
                <div style="display: flex; gap: 10px;">
                    <span style="background-color: #065f46; padding: 6px 12px; border-radius: 6px; font-size: 12px;">📊 master_registry_levels.csv</span>
                </div>
            </div>
        </div>
    """,
      unsafe_allow_html=True,
  )

with tab2:
  st.subheader("📅 Ημερολόγιος & Προγραμματισμός")
  st.info("Διαχείριση ημερομηνιών και επισκέψεων.")

with tab3:
  st.subheader("📊 Στατιστικά & Προγράμματα")
  st.info("Συγκεντρωτικές αναφορές και γραφήματα.")

with tab4:
  st.subheader("⚙️ Βαθμίδες & Priority Dashboard")
  st.info("Διαχείριση μορίων και προτεραιοτήτων.")
