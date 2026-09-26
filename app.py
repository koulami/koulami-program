import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="ΚΠΕ Ακρωτηρίου - Διαχείριση", layout="wide"
)

st.title("🌱 ΚΠΕ Ακρωτηρίου - Σύστημα Διαχείρισης Δεδομένων")
st.write(
    "Καλώς ήρθατε στο σύστημα. Παρακάτω μπορείτε να δείτε τα δεδομένα από τα"
    " αρχεία Excel."
)

# Επιλογή αρχείου Excel από αυτά που έχουμε ανεβάσει στο GitHub
file_option = st.selectbox(
    "Επιλέξτε αρχείο Excel για προβολή:",
    ["Απαντήσεις (15).xlsx", "Απαντήσεις (16).xlsx", "Απαντήσεις (17).xlsx"],
)

try:
  # Ανάγνωση του Excel με το pandas
  df = pd.read_excel(file_option)
  st.success(
      f"Το αρχείο **{file_option}** φορτώθηκε επιτυχώς! (Συνολικές εγγραφές:"
      f" {len(df)})"
  )

  # Εμφάνιση πίνακα δεδομένων
  st.dataframe(df, use_container_width=True)

  # Βασικά στατιστικά ή φίλτρα αν χρειάζεται
  st.subheader("Γρήγορη Επισκόπηση")
  st.write(df.describe(include="all"))

except Exception as e:
  st.warning(
      "Δεν ήταν δυνατή η αυτόματη ανάγνωση του αρχείου. Βεβαιωθείτε ότι το"
      " όνομα ταιριάζει ακριβώς."
  )
  st.error(f"Λεπτομέρειες σφάλματος: {e}")
