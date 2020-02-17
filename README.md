[![Build Status](https://travis-ci.com/landier/waky.svg?branch=master)](https://travis-ci.com/landier/waky)

# Waky
Waky is a web application to manage Wake-On-Lan supporting devices

# Local dev
```
docker run -it --rm -v $PWD:/workspace -w /workspace ubuntu /bin/bash
tox -e dev
WAKY_CONF=waky.conf
env/bin/waky
```

# Testing
```
tox
```

# Deploy using Docker
## Build
```
docker build -f docker/Dockerfile -t waky .
```

## Run
```
docker run -it --rm -p 8888:8888 waky:latest
```

# To do
* Web server
* Wake up feature
* Healthcheck feature
* Suspend feature
* Telegram integration
* PyPI publishing
