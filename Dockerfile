FROM python:3.7

WORKDIR /DragonGenerator
ADD . /DragonGenerator

RUN pip3 --no-cache-dir install -r requirements.txt
RUN rm -rf /usr/local/lib/python3.7/site-packages/stylegan2_pytorch
COPY /sgp /usr/local/lib/python3.7/site-packages

EXPOSE 8080

CMD ["python", "app.py"]