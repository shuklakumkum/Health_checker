

## Deployment Platforms Researched
- Heroku
- Railway
- AWS EC2 / Elastic Beanstalk
- Dockerized deployment

## Environment Variables Required
- API_HOST
- API_PORT
- SCAN_TIMEOUT
- MAX_SCANS_PER_DAY
- API_KEY

#steps
Clone repo
Install dependencies:'pip install -r requirements.txt'
Set environment variables
Run server:'uvicorn main:app  --host $API_HOST --port $API_PORT'
setup custom domain and SSL if needed
Monitor with UptimeRobot or Prometheus