FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 libgl1 libgl1-mesa-glx -y
COPY requirements.txt ./
COPY src/ ./src/

RUN pip3 install streamlit
RUN pip3 install tensorflow
RUN pip3 install opennsfw2
RUN pip install opencv-python




EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "src/contentchecker/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]