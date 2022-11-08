hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-file /home/anjali_kumari2/tf_idf/mapper_1.py \
-mapper  'python3 mapper_1.py' \
-file /home/anjali_kumari2/tf_idf/reducer_1.py \
-reducer 'python3 reducer_1.py' \
-input gs://dataproc-staging-europe-west4-396516896416-gmdooth6/spam_data_top_10_users/A18U49406IPPIJ.txt \
-output gs://dataproc-staging-europe-west4-396516896416-gmdooth6/spam_data_top_10_users/out1

hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-file /home/anjali_kumari2/tf_idf/mapper_2.py \
-mapper  'python3 mapper_2.py' \
-file /home/anjali_kumari2/tf_idf/reducer_2.py \
-reducer 'python3 reducer_2.py' \
-input gs://dataproc-staging-europe-west4-396516896416-gmdooth6/spam_data_top_10_users/out1/ \
-output gs://dataproc-staging-europe-west4-396516896416-gmdooth6/spam_data_top_10_users/out2

hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-file /home/anjali_kumari2/tf_idf/mapper_3.py \
-mapper  'python3 mapper_3.py' \
-file /home/anjali_kumari2/tf_idf/reducer_3.py \
-reducer 'python3 reducer_3.py' \
-input gs://dataproc-staging-europe-west4-396516896416-gmdooth6/spam_data_top_10_users/out2/ \
-output gs://dataproc-staging-europe-west4-396516896416-gmdooth6/spam_data_top_10_users/out3

hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-file /home/anjali_kumari2/tf_idf/mapper_4.py \
-mapper  'python3 mapper_4.py' \
-input gs://dataproc-staging-europe-west4-396516896416-gmdooth6/spam_data_top_10_users/out3/ \
-output gs://dataproc-staging-europe-west4-396516896416-gmdooth6/spam_data_top_10_users/final

hadoop fs -getmerge gs://dataproc-staging-europe-west4-396516896416-gmdooth6/spam_data_top_10_users/final/ /home/anjali_kumari2/tf_idf/results/A18U49406IPPIJ.txt