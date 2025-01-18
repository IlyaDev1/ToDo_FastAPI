FROM python:3.10-slim

WORKDIR /todo

COPY requirements.txt /todo/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /todo/

ENV PYTHONWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["python", "todo/app/main.py"]
