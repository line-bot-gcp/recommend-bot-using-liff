# Recommend bot Using liff

## 準備するもの

+ GCP Project
+ 以下のコマンドが実行できる環境
  + git
    + なるべく最新
  + Python
    + v 3.x
  + gcloud
    + なるべく最新

## 参考ドキュメント

+ Quickstart using a server client library
  + https://cloud.google.com/firestore/docs/quickstart-servers?hl=en#command-line


## GCP を操作するための準備をする

+ GCP の認証をする

```
gcloud auth login -q
```

+ gcloud コマンドの設定を行う

```
export _pj_id='Your GCP Project ID'

gcloud config set project ${_pj_id}
```

+ [WIP] GCP Project 内で各コンポーネントの API を有効化する

```
gcloud beta services enable cloudbuild.googleapis.com && \
gcloud beta services enable appengine.googleapis.com && \
gcloud beta services enable firestore.googleapis.com && \
gcloud beta services enable storage.googleapis.com && \
gcloud beta services enable storage-component.googleapis.com
```

## ソースコードを取得する

+ [WIP] 自分のワークスペースにて、このレポジトリを clone する

```
git clone https://hogehoge
cd hogehoge
```

## [WIP] Service Account の作成と Role の割り当て、JSON Key の取得を行う

+ Service Account の作成

```
export _common='liff-bot'

gcloud iam service-accounts create ${_common} \
    --display-name ${_common}
```

+ 作成した Service Account に Project Owner の Role を付与

```
export _sa_mail=$(gcloud iam service-accounts list | grep ${_common} | awk '{print $2}')

gcloud projects add-iam-policy-binding ${_pj_id} \
    --member "serviceAccount:${_sa_mail}" \
    --role "roles/owner"
```

+ 作成した Service Account を実行する Json ファイルの生成

```
gcloud iam service-accounts keys create ${_common}.json --iam-account ${_sa_mail}
```



## App Engine をデプロイする

WIP

## Firestore をデプロイする

WIP

## GCS にデプロイする

WIP


## 確認

WIP


























