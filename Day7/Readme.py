#website Health Chekcer API

#Features
HTTP Check
SSL Check
security headers
security score

#Installation
bash
git clone<repo-url>
cd website-health-checker
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt

## Run

```bash
uvicorn main:app --reload