# Start rabbit mq server
```sudo docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management```

# Start worker
from manager directory:
    ```python3 downloader/consumer.py```

# Start api
from managerD directory:
    ```./start-dev.sh```

# Add chrome extension
Make sure the previous steps have been completed before trying to download using the extension

1. Go to chrome
1. navigate to chrome://extensions/
1. turn on developer mode
1. load package from extension directory