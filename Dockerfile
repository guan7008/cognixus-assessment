# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV API_KEY=5cebc2dc-894e-4ce9-ae13-e446c348f7e6
ENV FLASK_APP=src/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV MYSQL_HOST=db
ENV MYSQL_PORT=3306
ENV MYSQL_DATABASE=cadb
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=r00t
ENV GOOGLE_CLIENT_ID=47725177727-d0hia48tklelj658f6hju223udehs9bn.apps.googleusercontent.com
ENV GOOGLE_PROJECT_ID=sunlit-monolith-212409
ENV GOOGLE_AUTH_URI=https://accounts.google.com/o/oauth2/auth
ENV GOOGLE_TOKEN_URI=https://oauth2.googleapis.com/token
ENV GOOGLE_AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
ENV GOOGLE_CLIENT_SECRET=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
ENV GOOGLE_REDIRECT_URI=http://localhost:8000/google/auth
RUN apk add --no-cache gcc musl-dev linux-headers libffi-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]