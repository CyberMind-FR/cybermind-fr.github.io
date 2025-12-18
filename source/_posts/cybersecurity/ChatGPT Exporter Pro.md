---
title: ChatGPT Exporter Pro — Architecture complète, Code source, CI/CD & Déploiement
date: 2025-11-25 20:00:00
tags:
  - ChatGPT
  - Automation
  - DevOps
  - CI/CD
  - Vercel
  - Railway
  - TypeScript
  - React
  - NodeJS
  - ExoJS
  - IA
categories:
  - Engineering
  - Fullstack
description: "Documentation complète pour ChatGPT Exporter Pro — extraction, génération ExoJS, upload GitHub/Drive, interface React, backend Express, CI/CD GitHub, déploiement Vercel + Railway."
toc: true
---

# ChatGPT Exporter Pro  
**Fullstack TS — Scraper, Export ExoJS, Upload GitHub & Drive, CI/CD, Vercel & Railway**

Ce guide couvre **l'intégralité du projet professionnel ChatGPT Exporter Pro**, incluant :
<!-- more -->
- extraction automatique d’une conversation ChatGPT  
- génération d’un fichier **ExoJS**  
- export GitHub / Google Drive via API  
- interface web moderne (React + TS + Tailwind + MUI + Dark Mode)  
- backend (Node + Express + TypeScript)  
- CI/CD GitHub automatique  
- déploiements automatisés sur **Vercel** (frontend) et **Railway** (backend)  
- architecture propre et professionnelle  

---

# 1. Présentation du Projet

**ChatGPT Exporter Pro** est une solution complète pour automatiser l’extraction, la sauvegarde et l’exploitation des conversations ChatGPT.

Elle permet de :

- récupérer automatiquement **tout le contenu textuel et média**  
- générer un format standard **ExoJS**  
- synchroniser le contenu vers :
  - **GitHub** (export structuré)
  - **Google Drive** (backup)
- proposer une interface web élégante (dark mode)  
- supporter une architecture CI/CD avancée (GitHub Actions)

---

# 2. Architecture Générale

```
chatgpt-exporter/
 ├── backend/
 │     ├── src/
 │     │     ├── server.ts
 │     │     ├── api/exportRouter.ts
 │     │     ├── services/
 │     │     │       ├── chatgptScraper.ts
 │     │     │       ├── exoExporter.ts
 │     │     │       ├── githubUploader.ts
 │     │     │       ├── googleDriveUploader.ts
 │     │     │       └── assetDownloader.ts
 │     ├── package.json
 │     ├── tsconfig.json
 │     └── Dockerfile
 │
 ├── frontend/
 │     ├── index.html
 │     ├── package.json
 │     ├── tailwind.config.js
 │     ├── tsconfig.json
 │     └── src/
 │           ├── main.tsx
 │           ├── App.tsx
 │           ├── pages/ExportPage.tsx
 │           ├── components/
 │           └── lib/api.ts
 │
 ├── scripts/install.sh
 │
 ├── .github/workflows/
 │     ├── frontend-deploy.yml
 │     ├── backend-deploy.yml
 │     └── build-test.yml
 │
 ├── README.md
 └── LICENSE
```

---

# 3. Backend — Code Source Complet

## 3.1 Serveur Express (`server.ts`)

```ts
import express from "express";
import cors from "cors";
import { exportRouter } from "./api/exportRouter";

const app = express();
app.use(cors());
app.use(express.json());
app.use("/api/export", exportRouter);

app.listen(3000, () => {
  console.log("Backend running at http://localhost:3000");
});
```

---

## 3.2 Route d’exportation (`exportRouter.ts`)

```ts
import express from "express";
import { fetchConversation } from "../services/chatgptScraper";
import { generateExoJS } from "../services/exoExporter";
import { pushToGitHub } from "../services/githubUploader";
import { uploadToDrive } from "../services/googleDriveUploader";
import fs from "fs";

export const exportRouter = express.Router();

exportRouter.post("/", async (req, res) => {
  try {
    const { url } = req.body;
    const convo = await fetchConversation(url);
    const filename = `conversation_${Date.now()}.exo.js`;
    const filepath = `./tmp/${filename}`;

    generateExoJS(convo, filepath);
    const content = fs.readFileSync(filepath, "utf-8");

    const github = await pushToGitHub(content, filename);
    const gdrive = await uploadToDrive(filepath, filename);

    res.json({
      status: "OK",
      messagesCount: convo.messages.length,
      github,
      gdrive
    });
  } catch (e: any) {
    res.status(500).json({ error: e.message });
  }
});
```

---

## 3.3 Scraper ChatGPT (`chatgptScraper.ts`)

```ts
import axios from "axios";
import cheerio from "cheerio";
import { downloadAsset } from "./assetDownloader";

export async function fetchConversation(url: string) {
  const { data } = await axios.get(url);
  const $ = cheerio.load(data);

  const messages: any[] = [];

  $(".min-h-[20px]").each((_, el) => {
    const role = $(el).attr("data-message-author") ?? "assistant";
    const text = $(el).text().trim();
    const images = [];
    $(el).find("img").each((_, img) => images.push($(img).attr("src")));
    messages.push({ role, text, images });
  });

  const assets: Record<string, string[]> = {};

  for (const msg of messages) {
    if (!msg.images) continue;

    assets[msg.text] = [];
    for (const img of msg.images) {
      const file = await downloadAsset(img);
      assets[msg.text].push(file);
    }
  }

  return { messages, assets };
}
```

---

## 3.4 Téléchargement des images (`assetDownloader.ts`)

```ts
import axios from "axios";
import fs from "fs";

export async function downloadAsset(url: string): Promise<string> {
  const filename = "asset_" + Date.now() + ".png";
  const filepath = "./tmp/" + filename;

  const response = await axios.get(url, { responseType: "arraybuffer" });
  fs.writeFileSync(filepath, response.data);

  return filepath;
}
```

---

## 3.5 Génération du fichier ExoJS (`exoExporter.ts`)

```ts
import fs from "fs";

export function generateExoJS(data: any, outPath: string) {
  const content =
    `export const conversation = ` + JSON.stringify(data, null, 2) + `;`;
  fs.writeFileSync(outPath, content);
}
```

---

## 3.6 Upload GitHub (`githubUploader.ts`)

```ts
import axios from "axios";

export async function pushToGitHub(content: string, filename: string) {
  const repo = process.env.GITHUB_REPO!;
  const token = process.env.GITHUB_TOKEN!;
  const path = "exports/" + filename;

  const url = `https://api.github.com/repos/${repo}/contents/${path}`;

  const res = await axios.put(
    url,
    { message: "Export automatique ChatGPT", content: Buffer.from(content).toString("base64") },
    { headers: { Authorization: `token ${token}` } }
  );

  return res.data.content.html_url;
}
```

---

## 3.7 Upload Google Drive (`googleDriveUploader.ts`)

```ts
import { google } from "googleapis";
import fs from "fs";

export async function uploadToDrive(filepath: string, name: string) {
  const auth = new google.auth.GoogleAuth({
    keyFile: process.env.GOOGLE_SERVICE_ACCOUNT_KEY!,
    scopes: ["https://www.googleapis.com/auth/drive.file"]
  });

  const drive = google.drive({ version: "v3", auth });

  const res = await drive.files.create({
    requestBody: { name, parents: [process.env.GOOGLE_DRIVE_FOLDER!] },
    media: { mimeType: "application/javascript", body: fs.createReadStream(filepath) }
  });

  return `https://drive.google.com/file/d/${res.data.id}`;
}
```

---

# 4. Frontend — Interface complète (React + TS + Tailwind + MUI)

## 4.1 Application principale (`App.tsx`)

```tsx
import { ThemeProvider, createTheme } from "@mui/material";
import { useState, useEffect } from "react";
import ExportPage from "./pages/ExportPage";
import DarkModeToggle from "./components/DarkModeToggle";

export default function App() {
  const [dark, setDark] = useState(true);

  useEffect(() => {
    document.documentElement.classList.toggle("dark", dark);
  }, [dark]);

  const theme = createTheme({
    palette: {
      mode: dark ? "dark" : "light",
      primary: { main: "#6366f1" }
    }
  });

  return (
    <ThemeProvider theme={theme}>
      <div className="min-h-screen bg-black text-white">
        <DarkModeToggle dark={dark} setDark={setDark} />
        <ExportPage />
      </div>
    </ThemeProvider>
  );
}
```

---

# 5. CI/CD GitHub — Déploiement Automatique

## 5.1 Frontend → Vercel

```yaml
name: Deploy Frontend

on:
  push:
    branches: [ main ]
    paths:
      - "frontend/**"

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
      - run: cd frontend && npm install && npm run build
      - uses: amondnet/vercel-action@v20
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          github-token: ${{ secrets.GITHUB_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_FRONTEND_PROJECT_ID }}
```

---

## 5.2 Backend → Railway

```yaml
name: Deploy Backend

on:
  push:
    branches: [ main ]
    paths:
      - "backend/**"

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - uses: railwayapp/github-action@v2
        with:
          railwayToken: ${{ secrets.RAILWAY_TOKEN }}
          serviceId: ${{ secrets.RAILWAY_BACKEND_SERVICE_ID }}
```

---

# 6. Installation Locale

```
chmod +x scripts/install.sh
./scripts/install.sh
```

Lancer :

```
cd backend && npm start
cd frontend && npm run dev
```

---

# 7. Conclusion

ChatGPT Exporter Pro est une **solution clé-en-main fullstack**, adaptée pour :

- l’automatisation  
- l’archivage  
- l’ingestion de contenu ChatGPT  
- les workflows DevOps pros  
- le blogging technique (Hexo)  
- les pipelines CI/CD modernes  

Si tu veux :  
- que je **génère le ZIP Hexo complet**,  
- que je crée une **version NPM**,  
- ou que j’installe **un thème Hexo personnalisé**,  
demande :

**« Génère la version Hexo complète »**  
ou  
**« Fais le ZIP Hexo »**.

