FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000 8501

CMD ["python manage.py runserver 0.0.0.0:8000", "streamlit run app.py"]