FROM python:3.9

COPY * /build/

WORKDIR /build

RUN python3 -mpip install pipenv && python3 -mpipenv install

CMD ["python3", "-mpipenv", "run", "/build/dependabot-auto-merge.py"]
