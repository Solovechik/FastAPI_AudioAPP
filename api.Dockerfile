FROM 	python:3.11.3-slim
WORKDIR /code
COPY	./requirements.txt /code/requirements.txt
COPY	./ffmpeg.tar.gz /code
RUN	mkdir /usr/local/bin/ffmpeg
RUN	tar -xf /code/ffmpeg.tar.gz -C /usr/local/bin/ffmpeg && rm /code/ffmpeg.tar.gz
RUN	ln -s /usr/local/bin/ffmpeg/ffmpeg /usr/bin/ffmpeg
RUN	pip install pip --upgrade
RUN 	pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY	./audio_app /code/audio_app
CMD	["uvicorn", "audio_app.main:app", "--host", "0.0.0.0", "--port", "8000"]
