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


## 事前に必要なもの

+ LINE Developer にて
  + Provider 作成
  + Channel 作成
    + USER_ID
    + YOUR_CHANNEL_SECRET
    + YOUR_CHANNEL_ACCESS_TOKEN
    + LIFF_URL
+ GCP
  + 任意のプロジェクト作成


## GCP を操作するための準備をする

+ GCP の認証をする

```
gcloud auth login -q
```

+ gcloud コマンドの設定を行う

```
export _pj_id='Your GCP Project ID'

export _pj_id='ca-igarashi-test-v5v2'

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

+ 自分のワークスペースにて、このレポジトリを clone する

```
git clone https://github.com/line-bot-gcp/recommend-bot-using-liff.git
cd recommend-bot-using-liff.git
```

## Service Account の作成と Role の割り当て、Json Key の取得を行う

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

## [WIP] GCS に画像をアップロードする

+ bucket の作成

```
gsutil mb gs://${_pj_id}-liff-20200823
gsutil ls | grep ${_pj_id}-liff-20200823
```

+ GCS にイメージファイルをコピー

```
gsutil cp static/images/*.png gs://${_pj_id}-liff-20200823/
gsutil ls gs://${_pj_id}-liff-20200823
```

+ GCS にアップロードしたイメージを一般公開する

```
gsutil iam ch allUsers:objectViewer gs://${_pj_id}-liff-20200823

```


+ GCS に

maguro.png
maguro_mini.png
maguro1_half.png
maguro2_half.png
maguro3_half.png
maguro4_half.png
sushi.png
menu0.png
menu1.png
menu2.png
menu3.png




## [WIP] Firestore をデプロイする

GCP コンソールの FireStore に行き、 `Native mode` を選択

![](./images/readme-01.png)

リージョンは `asia-northeast1` を選択

![](./images/readme-02.png)


line-users というDBを作る??



## [WIP] App Engine をデプロイする

WIP










## 確認

WIP


























