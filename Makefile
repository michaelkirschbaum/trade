init:
    pip3 install -r requirements.txt

test:
    py.test tests

run:
    python3 trade/app.py