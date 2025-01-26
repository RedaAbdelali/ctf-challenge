FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

# Create a fake flag and a real flag
RUN echo "DEFENSYS{c00k13_m4n1pul4t10n_4nd_c0mm4nd_1nj3ct10n}" > /app/flag

# Make the flag readable only by root
RUN chown root:root /app/flag && chmod 644 /app/flag

CMD ["python", "app.py"]