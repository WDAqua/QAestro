# Installation of QAestro {#installation-with-docker}
## Requirements
The following instructions are for installation of QAestro in Linux Fedora >=23. For different Linux versions or operating systems follow the steps described in [Installation of QAestro with docker](#installation-with-docker).
- Install Python 2.7 or newer
- Install the following libraries gcc-c++ glibc.i686 libstdc++.i686
    sudo apt-get install gcc-c++ glibc.i686 libstdc++.i686

## Execution of QAestro scripts
1. Given a set of views and a query you can produce all rewritings by executing:
    ./run_QAestro.sh <views> <query> <output>

Usage example:
    ./run_QAestro.sh qa/views_1.txt qa/query_1.txt qa/output.txt

2. Given a set of views and multiple queries you can produce all rewritings by executing:
    ./run_all_QAestro.sh <views> <queries> <output>

Usage example:
    ./run_all_QAestro.sh qa/views_1.txt qa/query_*.txt qa/output.txt

# Installation of QAestro with docker {#installation-with-docker}
1. Install docker - see <https://docs.docker.com/> for details
2. Start docker - see <https://docs.docker.com/> for details
3. Build docker image
    docker build -t qaestro .
4. Run docker container and open bash shell
    docker run --name qaestro --rm -i -t qaestro bash
5. Execute QAestro following the instructions above, for example:
    ./run_QAestro.sh qa/views_1.txt qa/query_1.txt qa/output.txt
