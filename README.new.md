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
export _rg='asia-northeast1'
export _zn='asia-northeast1-c'



gcloud config set project ${_pj_id}
gcloud config set compute/region ${_rg}
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

## GCS に画像をアップロードする

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

## App Engine のダミーをデプロイする

```
cd app-engine-dummy
cat hogehoge | sed hoggeho > hogehoge
```

```
gcloud app deploy
```
```
export _app_url=$(gcloud app describe | grep defaultHostname | awk '{print $2}')
echo ${_app_url}
```
```
gcloud app browse
```

```
### Ex.

# gcloud app browse
Did not detect your browser. Go to this link to view your app:
https://ca-igarashi-test-v5v2.an.r.appspot.com
```
```
cd -
```

## [WIP] Firestore をデプロイする

GCP コンソールの FireStore に行き、 `Native mode` を選択

![](./images/readme-01.png)

リージョンは `asia-northeast1` を選択

![](./images/readme-02.png)


line-users というDBを作る??



## [WIP] App Engine をデプロイする

```

export _UID="Your user ID"
export _YR_CH_SCR="Your Channel secret"
export _YR_CH_ACC_TKN="Your Channel access token"
export _LIFF_URL=""
export _YR_BCK=${_pj_id}-liff-20200823


export _UID="Udfd12adfcc22b1633bfb80f270d75193"
export _YR_CH_SCR="46024dcd52682ccb821c3b39057a28a6"
export _YR_CH_ACC_TKN='ijL4J/asnkPxxqylJiI3R7fmiDZsSeHLzGHiK7KFNTalSYw+Sb7kVEqnWuigADI/OuSlm55UsYBaLtTXlJWfSv6RX4jIFF+jV8rhcjfMH+UT5NUxIVvmSPPJCftBpHwSUWrLGDx/s9XcMhb+ciH0YwdB04t89/1O/w1cDnyilFU='
export _LIFF_ID="1654838518-pW5bGvkR"
export _YR_BCK=${_pj_id}-liff-20200823
```



+ [WIP] template yaml から app を作る

```
cat app.yaml.template | sed "s/_uid/${_UID}/g" | sed "s/_yr_ch_scr/${_YR_CH_SCR}/g" | sed "s/_LIFF_ID/${_liff_id}/g" | sed "s/_liff_id/${_LIFF_ID}/g" | sed "s/_yr_bck/${_YR_BCK}/g" > app.yaml
```

+ liff-starter.js.template から作る

```
cat static/js/liff-starter.js.template | sed "s/_liff_id/${_LIFF_ID}/g" > static/js/liff-starter.js
```



+ App Engine にデプロイ

```
gcloud app deploy
```

## 確認

WIP


























