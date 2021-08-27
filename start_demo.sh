python3 -m virtualenv venv
source venv/bin/activate 

python3 -m pip install --upgrade pip
pip install wordcloud

./gen.py
