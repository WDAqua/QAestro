# Installation of QAestro
## Requirements
The following instructions are for installation of QAestro in Linux Fedora >=23. For different Linux versions or operating systems follow the steps described in [Installation of QAestro with docker](#installation-of-qaestro-with-docker).
- Install Python 2.7 or newer
- Install the following libraries `gcc-c++`, `glibc.i686`, and `libstdc++.i686`

    sudo apt-get install gcc-c++ glibc.i686 libstdc++.i686

## Execution of QAestro scripts
1. Given a set of views and a query you can produce all rewritings by executing

    ./run_QAestro.sh <views> <query> <output>

`views` is the name of the file containing the views, `query` is the name of the file containing the query, and `output` is the name of the output file.
Usage example:
    
    ./run_QAestro.sh qa/views/views.txt qa/queries/query_1.txt qa/output/output.txt

2. Given a set of views and multiple queries you can produce all rewritings by executing

    ./run_all_QAestro.sh <views> <query_folder> <output_folder>

`views` is the name of the file containing the views, `queries` a folder containing query files, and `output` is the name of the output file.
Usage example:
    
    ./run_all_QAestro.sh qa/views/views.txt qa/queries/ qa/output/

# Installation of QAestro with docker
1. Install docker - see <https://docs.docker.com/> for details

2. Start docker - see <https://docs.docker.com/> for details

3. Clone the GitHub repository:

    git clone https://github.com/WDAqua/QAestro

4. Build docker image

    docker build -t qaestro .

5. Run docker container and open bash shell

    docker run --name qaestro --rm -i -t qaestro bash

6. Execute QAestro following the instructions above, for example

    ./run_QAestro.sh qa/views/views.txt qa/queries/query_1.txt qa/output/output.txt
