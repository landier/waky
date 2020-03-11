[![Build Status](https://travis-ci.com/landier/waky.svg?branch=master)](https://travis-ci.com/landier/waky)

# Waky
Waky is a web application to manage Wake-On-Lan supporting devices

## Requirements
* Python 3
* Bower
* tox

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

## Run
```
tox -e run
```

## Release
```
bumpversion minor
```

## Build
```
tox -e build
```

## Build & Publish to PyPI
```
tox -e upload
```

# Resources
* [favicon.io](https://favicon.io/favicon-generator/?t=W&ff=Righteous&fs=180&fc=%23000&b=rounded&bc=transparent)
* [Righteous font](https://fonts.google.com/specimen/Righteous)
