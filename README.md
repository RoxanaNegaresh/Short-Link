#  Short Link  

An accessible tool for shortening long links into short links!  

<img width="1653" height="919" alt="Screenshot (293)" src="https://github.com/user-attachments/assets/4cab762e-839d-4dfe-8724-34c4ffe48d39" />

---

##  Features
- Less memory usage  
- Clear and clean short links  
- Fast and simple to use  
- User-friendly interface  

---

##  Setup

 **Clone the repository**  
```bash
git clone https://github.com/RoxanaNegaresh/Short-Link.git
cd Short-Link
```
**Create a virtual environment**
```bash

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate   # Linux/Mac
```
**Install dependencies**
```bash

pip install -r requirements.txt
```
**Run migrations**
```bash

python manage.py migrate
```
**Run the server**
```bash

python manage.py runserver
```
Now open your browser and visit:
 http://127.0.0.1:8000/


