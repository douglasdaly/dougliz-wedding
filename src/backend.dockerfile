FROM python:3.7

RUN pip install --upgrade pip

# Required dependencies
RUN pip install uvicorn gunicorn passlib[bcrypt] tenacity requests emails \
    fastapi pyjwt python-multipart email_validator jinja2 psycopg2-binary \
    alembic SQLAlchemy

# - Additional dependencies
RUN pip install click python-dotenv orjson

# For development, Jupyter remote kernel, Hydrogen
# Using inside the container:
# jupyter lab --ip=0.0.0.0 --allow-root --NotebookApp.custom_display_url=http://127.0.0.1:8888
ARG env=prod
RUN bash -c "if [ $env == 'dev' ] ; then pip install jupyterlab ; fi"
EXPOSE 8888

# Setup application
COPY ./backend /app
RUN chmod +x /app/scripts/*.sh
WORKDIR /app/

# Setup and start application
ENV PYTHONPATH=/app
EXPOSE 80

CMD ["/app/scripts/start.sh"]
