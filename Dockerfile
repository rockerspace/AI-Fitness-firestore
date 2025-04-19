FROM python: 3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8000", "--server.address=0.0.0.0"]
