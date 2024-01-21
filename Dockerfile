FROM python:3.8-slim

WORKDIR /app

COPY setup.py setup.py 
COPY . .

RUN python3 setup.py install

EXPOSE 8501

ENV STREAMLIT_SERVER_PORT=8501

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]


