# Usage of output_es.py
本脚本用于Transfer elasticsearch的数据库至manticoresearch的数据库

## Installation
1. 首先你需要安装elasticserach和manticoresearch的python库

```bash
pip3 install manticoresearch elasticsearch
```

2. 然后进入脚本，填写MANTICORE_URL和ELASTICSEARCH_URL, 指定正确的数据库服务器位置。

若考虑使用SSL链接Elasticsearch, 需要指定SSL的CA_CERTS_PATH

根据ES的设置，填写ES_USERNAME 和 ES_PASSWORD

3. 启动es和ms的服务

Linux(Debian/Ubuntu)
```bash
sudo systemctl start elasticsearch
```

```bash
sudo systemctl start manticore
```
其它系统可自行GPT。


4. 运行脚本

```bash
python3 output_es.py
```

5. 本脚本运行后会在当前文件夹输出生成的JSON文件，其中包含了ES索引的mapping和documents。Manticoresearch将插入所有JSON的值。

## Check Your Results in Manticoresearch

```bash
python showtables.py
```
