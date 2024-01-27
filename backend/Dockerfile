FROM python:3.11
WORKDIR /backend
COPY . .
RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt
EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]