import streamlit as st

# --- Streamlit App Title and Description ---
st.title("🚗 Simple Car Price Predictor")
st.write("Masukkan detail mobil di bawah ini untuk mendapatkan estimasi harga (dalam IDR).")
st.write("---")

# --- Input Widgets for Car Features ---
st.header("Masukkan Detail Mobil:")

# Mileage input (slider for a range)
mileage = st.slider(
    "⏲ odometer : Mileage (in kilometers)",
    min_value=0,
    max_value=300000,
    value=50000,
    step=1000,
    help="Jarak total yang telah ditempuh mobil."
)

# Year of Manufacture (NOW A SLIDER)
year_manufacture = st.slider(
    " 📅 Tahun Pembuatan",
    min_value=1990,
    max_value=2025,
    value=2018,
    step=1,
    help="Tahun mobil diproduksi."
)

# Brand selection (dropdown remains the same)
brand_options = ["Toyota", "Honda", "Ford", "BMW", "Mercedes-Benz", "Nissan", "Mitsubishi", "Suzuki", "Hyundai", "Other"]
brand = st.selectbox(
    "🚘Brand Mobil",
    brand_options,
    help="Pilih merek pabrikan mobil."
)

# Engine Size (NOW A SLIDER)
engine_size = st.slider(
    " ⛽ Ukuran Mesin (dalam Liter)",
    min_value=0.5,
    max_value=8.0,
    value=2.0,
    step=0.1,
    help="Kapasitas mesin mobil."
)

# --- Prediction Logic (Simulated Model) ---
def predict_car_price(mileage, year_manufacture, brand, engine_size):
    """
    Fungsi dummy yang sangat disederhanakan untuk memperkirakan harga mobil.
    Harga dalam Rupiah Indonesia (IDR).
    """
    base_price = 200_000_000  # Harga dasar awal (misalnya, 200 juta IDR)

    # Penyesuaian berdasarkan fitur
    # 1. Mileage: Mileage lebih tinggi mengurangi harga
    price = base_price - (mileage * 500) # Kurangi Rp 500 per km

    # 2. Year of Manufacture: Mobil lebih tua lebih murah
    current_year = 2025
    age = current_year - year_manufacture
    price -= (age * 7_500_000) # Kurangi Rp 7.5 juta per tahun usia

    # 3. Brand: Merek yang berbeda memiliki nilai dasar yang berbeda
    if brand == "BMW" or brand == "Mercedes-Benz":
        price += 50_000_000  # Merek premium menambah Rp 50 juta
    elif brand == "Toyota" or brand == "Honda":
        price += 20_000_000  # Merek populer menambah Rp 20 juta
    elif brand == "Ford":
        price -= 10_000_000  # Contoh: Ford mungkin sedikit kurang dalam model dummy ini
    # "Other" atau merek yang tidak terdaftar tidak mendapat penyesuaian khusus

    # 4. Engine Size: Mesin lebih besar umumnya berarti harga lebih tinggi
    price += (engine_size * 8_000_000) # Tambah Rp 8 juta per liter ukuran mesin

    # Pastikan harga tidak di bawah minimum yang wajar
    if price < 30_000_000: # Harga minimum Rp 30 juta
        price = 30_000_000

    return int(price) # Kembalikan sebagai bilangan bulat untuk tampilan yang lebih bersih

# --- Prediction Button and Output ---
st.write("---")
if st.button("Prediksi Harga Mobil"):
    predicted_price = predict_car_price(mileage, year_manufacture, brand, engine_size)

    st.success(f"**Estimasi Harga Mobil:**")
    st.markdown(f"## Rp {predicted_price:,.0f}") # Format dengan koma untuk keterbacaan
    st.info("*(Ini adalah prediksi yang disederhanakan untuk tujuan demonstrasi. Harga sebenarnya bervariasi berdasarkan banyak faktor lain seperti kondisi, fitur, permintaan pasar, dll.)*")
