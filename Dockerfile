FROM python:3.9

COPY * /build/

WORKDIR /build

# since pipenv installs into a venv we can't use it to install stuff
RUN python3 -mpip install pipenv && python3 -mpipenv lock -r > req.txt && \
    python3 -mpip install -r req.txt

CMD ["python3", "/build/dependabot-auto-merge.py"]
