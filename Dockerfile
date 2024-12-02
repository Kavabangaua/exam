FROM alpine

WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]