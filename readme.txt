docker run -it --rm jupyter/base-notebook /bin/bash -v /Users/rperezl9/workspace/incomes:/home/jovyan


docker run -it --rm jupyter/scipy-notebook /bin/bash -v /Users/rperezl9/workspace/incomes:/home/jovyan

docker run -v /Users/rperezl9/workspace/incomes:/home/jovyan -p 8888:8888 jupyter/scipy-notebook
