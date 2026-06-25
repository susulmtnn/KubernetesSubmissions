import uuid
from datetime import datetime, timezone
from time import sleep

result = str(uuid.uuid4())
while True:
    timestamp = datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
    print(f"{timestamp}: {result}")
    sleep(5)