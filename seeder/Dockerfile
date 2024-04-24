FROM python:alpine
WORKDIR /app/seeder
COPY . .
RUN pip install pymongo
CMD ["python", "seeder.py"]