FROM python:3.13

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install uv
RUN pip install --upgrade pip
RUN pip install --upgrade uv

COPY requirements.txt /app/

# Use uv with --system flag to install packages system-wide without virtual env
RUN uv pip install --system --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]