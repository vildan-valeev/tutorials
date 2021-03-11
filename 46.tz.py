from datetime import datetime
import pytz

print(datetime.now())

print(pytz.utc.localize(datetime.utcnow()))

print(pytz.utc.localize(datetime.utcnow()).astimezone())

print(pytz.utc.localize(datetime.utcnow()).astimezone().isoformat())