# Experimental Setup for Galaxybase in FinBench

- [Galaxybase Official Website](https://createlink.com)

## 1. Preparation

- Download the `galaxybase.zip` file from [here](https://drive.google.com/file/d/1euXCtu-oEzeh6M3Z4mP6LxofbhaYHHxs/view?usp=sharing), unzip it, and you will find `galaxybase.tar.gz` and the JSON files.
- Prepare the data files for both `sf10` and `sf100` datasets.

## 2. Installation & Data Loading

- **Package Extraction**

Extract the Galaxybase package:

```bash
tar -zxf galaxybase.tar.gz
```

- **Environment Setup and Image Installation**

Install the Galaxybase environment and necessary Docker images:

```bash
./galaxybase-*/bin/galaxybase-deploy install docker
./galaxybase-*/bin/galaxybase-deploy image install
```

- **Service Container Deployment**

Deploy the `graph` service containers. 

```shell
./galaxybase-*/bin/galaxybase-deploy build graph --home home
```

- **Validation & Start-Up**

To validate the service, retrieve the verification code using the following command (replace `CONTAINER_ID` with the actual container ID):

```
docker exec -i CONTAINER_ID gtools graph auth-check
```

Then, input the authorization code:

```
docker exec -i CONTAINER_ID gtools graph auth --code 'AUTH_CODE'
```

*Note: You can acquire the authorization code by contacting the support team at support@createlink.com.*

- **Data Transfer**

Move the benchmark data to the `home/graph/data` directory. Example for the `sf10` dataset:

```shell
mv sf10/snapshot home/graph/data/sf10
```

- **Data Loading**

Load the `sf10` dataset into Galaxybase using the provided schema and mapping files:

```shell
./galaxybase-*/bin/galaxybase-load -s json/schema_sf10.json -m json/mapping_sf10.json -g sf10
```

## 3. Benchmark Execution

- **Compilation**

First, clone the repository and compile the benchmark implementation. 

```shell
git clone https://github.com/ldbc/ldbc_finbench_transaction_impls 
mv sf10_finbench_benchmark.* ldbc_finbench_transaction_impls/
mv sf100_finbench_benchmark.* ldbc_finbench_transaction_impls/
cd ldbc_finbench_transaction_impls
mvn install -DskipTests
cd galaxybase-cypher
```

- **Benchmark Run**

Execute the benchmark for both `sf10` and `sf100` datasets. 

```shell
# Run benchmark for sf10
nohup sh sf10_finbench_benchmark.sh > console.log &

# Run benchmark for sf100
nohup sh sf100_finbench_benchmark.sh > console.log &
```

