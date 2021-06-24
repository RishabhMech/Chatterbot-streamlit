mkdir -p ~/.streamlit/

echo "[theme]
primaryColor = '#3C9E7E'
backgroundColor = '#000000'
secondaryBackgroundColor = '#426DBF'
textColor = '#AF8E3D'
font = ‘sans serif’
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
