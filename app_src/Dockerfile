FROM python:3.11-slim

WORKDIR /app

# Install Flask
RUN pip install flask

# Copy backend and UI
COPY override_api.py /app/override_api.py
COPY web /app/web
COPY run.sh /app/run.sh

RUN chmod +x /app/run.sh

EXPOSE 5005

CMD ["/app/run.sh"]
