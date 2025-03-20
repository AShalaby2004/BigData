FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-venv

RUN mkdir -p /home/doc-bd-a1/

WORKDIR /home/doc-bd-a1/

RUN python3 -m venv venv
ENV PATH="/home/doc-bd-a1/venv/bin:$PATH"

RUN pip install --no-cache-dir pandas numpy seaborn matplotlib scikit-learn scipy

COPY dataset.csv /home/doc-bd-a1/dataset.csv

CMD ["/bin/bash"]
