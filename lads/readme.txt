1 install : 
pip install fastapi uvicorn

2 run locally : 
python run.py

3 test request :
curl -X POST http://127.0.0.1:8000/event \
-H "Content-Type: application/json" \
-d '{"ip":"1.2.3.4","token":"invalid","device_risk":70}'

