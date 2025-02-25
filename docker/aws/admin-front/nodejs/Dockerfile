# 使用するNode.jsのバージョンを指定
FROM public.ecr.aws/docker/library/node:18-bullseye

# アップデート
RUN apt-get update && apt-get upgrade -y

# 環境変数
ENV NODE_ENV=production
ENV HOST=0.0.0.0
ENV PORT=3000

# アプリケーションのディレクトリを設定
WORKDIR /project

# npmを最新バージョンにアップグレード
RUN npm install -g npm@10

# プロジェクトのファイルをコピー
COPY ./apps/admin-front/ /project/

# ライブラリのインストールと型定義の追加
RUN npm install && npm install --save-dev @types/jsonwebtoken

# caniuse-lite のアップデート（オプション）
RUN npx update-browserslist-db@latest

# ビルド
RUN npm run build

# Dockerfile内でAWSのパラメーターストアから設定を動的に取得するには、ビルド時ではなく、コンテナの実行時に設定を取得する必要があります。
# Dockerのビルドプロセス（RUN コマンドを使用する部分）は静的であり、実行時の動的な操作（例えば、環境変数に基づいて異なる動作をする）はサポートしていません。
# そのため、ENTRYPOINT や CMD を使って実行時に設定を取得する方法を検討する必要があります。

# サーバーの起動
COPY ./docker/aws/admin-front/nodejs/cmd.sh /usr/local/bin/cmd.sh
RUN chmod 777 /usr/local/bin/cmd.sh
CMD ["/usr/local/bin/cmd.sh"]
