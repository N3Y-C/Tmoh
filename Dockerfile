FROM python

WORKDIR /app
COPY requirements.txt .
COPY Tmoh.py .
RUN pip install -r requirements.txt
CMD ["python", "./Tmoh.py"]
