# Discord-Translator

# Discord 自動翻訳Bot（英語 ⇄ 日本語）

無料・クラウド常時稼働のDiscord翻訳Bot  
英語と日本語を自動で相互翻訳します。

---

## 🧩 構成

- Discord Bot
- Railway（クラウド実行）
- googletrans（無料翻訳）

👉 PC不要 / 無料 / シンプル構成

---

## 🚀 セットアップ手順

---

## 1. Discord Bot作成

### ① Developer Portalにアクセス
https://discord.com/developers/applications

---

### ② Bot作成
1. 「New Application」
2. 名前を入力して作成
3. 左メニュー「Bot」→「Add Bot」

---

### ③ トークン取得
- 「Reset Token」→コピーして保存  
⚠️ 他人に絶対共有しない

---

### ④ 必須設定
- 「MESSAGE CONTENT INTENT」→ ON

---

### ⑤ サーバーに招待

左メニュー  
→ OAuth2 → URL Generator

#### Scopes
- bot

#### Bot Permissions
- Send Messages
- Read Message History

---

生成されたURLを開く  
→ サーバーを選択  
→ 「追加」

---

### ✅ 確認
DiscordでBotがメンバー一覧に表示される

---

## 2. GitHubにコード配置

リポジトリを作成し、以下のファイルを追加

---

### 📄 必要ファイル

- bot.py
- requirements.txt
- Dockerfile

---

### 📌 GitHubにアップロード

1. 「Add file」→「Upload files」
2. 上記ファイルを追加
3. 「Commit changes」

---

## 3. Railwayにデプロイ

### ① Railwayにアクセス
https://railway.app/

→ GitHubでログイン

---

### ② プロジェクト作成
1. 「New Project」
2. 「Deploy from GitHub repo」
3. リポジトリ選択

---

### ③ 環境変数設定（必須）

「Variables」で追加：  
TOKEN=DiscordのBotトークン  
---

### ④ デプロイ
- 自動で開始 or 「Deploy / Redeploy」

---

## 4. 動作確認

Discordでメッセージ送信：
