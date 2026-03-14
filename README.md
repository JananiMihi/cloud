MapReduce: Sales Aggregation by Customer Segment
Team Members
EG/2021/4433 — BANDARA L.R.T.D
EG/2021/4432 — BANDARA K.M.T.O.N
EG/2021/4424 — BALASOORIYA J.M
---
Dataset
Name: Online Store Customer Transactions (1M Rows)  
Source: https://www.kaggle.com/datasets/mountboy/online-store-customer-transactions-1m-rows  
Size: ~1,000,000 rows | Format: CSV  
Key Columns Used:
`Segment` (column index 6) — Customer segment: Basic, Silver, Gold, Platinum
`Amount_spent` (column index 10) — Total transaction value in USD
---
Requirements
Java 11+ (OpenJDK 11)
Apache Hadoop 3.3.6
Python 3.8+
SSH (for Hadoop pseudo-distributed mode)
---

---
Steps to Run
1. Start Hadoop
```bash
start-dfs.sh
start-yarn.sh
jps   # verify: NameNode, DataNode, ResourceManager, NodeManager
```
2. Upload data to HDFS
```bash
hdfs dfs -mkdir -p /user/hadoop/transactions/input
hdfs dfs -put transactions.csv /user/hadoop/transactions/input/
```
3. Run Job 1 — Sales Aggregation by Segment
```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input  /user/hadoop/transactions/input/transactions.csv \
  -output /user/hadoop/transactions/output \
  -mapper  'python3 mapper.py' \
  -reducer 'python3 reducer.py' \
  -file mapper.py \
  -file reducer.py
```
4. View results
```bash
hdfs dfs -cat /user/hadoop/transactions/output/part-00000
```
5. Run Job 2 — Top-N Segments by Revenue (Bonus)
```bash
hdfs dfs -mkdir -p /user/hadoop/transactions/topn_input
hdfs dfs -put output_results.tsv /user/hadoop/transactions/topn_input/

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input  /user/hadoop/transactions/topn_input/output_results.tsv \
  -output /user/hadoop/transactions/topn_output \
  -mapper  'python3 top_n_mapper.py' \
  -reducer 'python3 top_n_reducer.py' \
  -file top_n_mapper.py \
  -file top_n_reducer.py

hdfs dfs -cat /user/hadoop/transactions/topn_output/part-00000
```
---
Local Test (No Hadoop Required)
```bash
# Test with full dataset
cat transactions.csv | python3 mapper.py | sort | python3 reducer.py

# Test Top-N job
cat output_results.tsv | python3 top_n_mapper.py | sort | python3 top_n_reducer.py
```
---
Actual Output — Job 1 (output_results.tsv)
Segment	Total Revenue ($)	Order Count
Basic	585,266,645.02	414,486
Gold	121,010,540.09	87,659
Missing	103,382,061.55	72,897
Platinum	227,907,626.66	156,826
Silver	242,519,078.43	172,067
TOTAL	1,280,085,951.75	903,935
---
Actual Output — Job 2 Top-N by Revenue (topn_results.tsv)
Rank	Segment	Total Revenue ($)	Order Count
1	Basic	585,266,645.02	414,486
2	Silver	242,519,078.43	172,067
3	Platinum	227,907,626.66	156,826
4	Gold	121,010,540.09	87,659
5	Missing	103,382,061.55	72,897
---

Stop Hadoop (when done)
```bash
stop-yarn.sh
stop-dfs.sh
```
