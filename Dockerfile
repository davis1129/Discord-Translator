FROM python:3.11-slim

RUN apt-get update && apt-get install -y git build-essential

# LibreTranslate
RUN pip install libretranslate

# Bot
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

# 起動スクリプト作る
RUN echo '#!/bin/bash\n\
libretranslate --host 0.0.0.0 --port 5000 &\n\
sleep 10\n\
python bot.py\n\
wait' > start.sh

RUN chmod +x start.sh

CMD ["./start.sh"]
