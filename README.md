# dynamodb_globalsecondaryindex_sample
## はじめに
DynamoDBのGlobalSecondaryIndexの使い方のサンプル（※特定の個人向け）

### 環境
- OS
  - Windows
- コマンド
  - awscli
  - awscli-local
  - pip
- ソフトウェア
  - Docker
    - localstack
  - poetry
  - python

### 補足
- AWSの費用を抑えるためにlocalstack環境（≒疑似的なAWS環境）で今回は検証
- boto3については最新のライブラリを利用しているはずなので、これで問題ないはず

### ターミナルに投入したCLIコマンド
```
table_name=XXXXXXXXXX
awslocal dynamodb list-tables

awslocal dynamodb create-table \
    --table-name $table_name \
    --attribute-definitions \
        AttributeName=user_id,AttributeType=S \
        AttributeName=user_code,AttributeType=S \
    --key-schema AttributeName=user_id,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST \
    --global-secondary-indexes \
            "[
                {
                    \"IndexName\": \"UserCodeIndex\",
                    \"KeySchema\": [{\"AttributeName\":\"user_code\",\"KeyType\":\"HASH\"}],
                    \"Projection\":{
                        \"ProjectionType\":\"INCLUDE\",
                        \"NonKeyAttributes\":[\"user_id\"]
                    }
                }
            ]"

awslocal dynamodb describe-table --table-name $table_name

awslocal dynamodb put-item \
    --table-name $table_name  \
    --item \
        '{"user_id": {"S": "dummy"},"status": {"S": "none"},"user_code": {"S": "dummy_user_code"}}'

awslocal dynamodb get-item \
    --table-name $table_name \
    --key '{ "user_id": { "S": "dummy" }}'

awslocal dynamodb query \
    --table-name $table_name \
    --index-name UserCodeIndex \
    --key-condition-expression "user_code = :user_code" \
    --expression-attribute-values  '{":user_code":{"S":"dummy_user_code"}}'
```
## poetry install
```
poetry install
```
## poetry環境でプログラムを実行
```
poetry run python ./main.py
```