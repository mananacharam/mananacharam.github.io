# Quick Setup for GitHub Pages

## 🚀 Quick Start

### 1. Initialize Git (if not already done)
```bash
git init
```

### 2. Add all files
```bash
git add .
```

### 3. Commit
```bash
git commit -m "Initial commit - Mana Nacharam Voter Information System"
```

### 4. Add GitHub remote
```bash
git remote add origin https://github.com/mananacharam/mananacharam.github.io.git
```

### 5. Push to GitHub
```bash
git branch -M main
git push -u origin main
```

### 6. Enable GitHub Pages
1. Go to: https://github.com/mananacharam/mananacharam.github.io/settings/pages
2. Under **Source**, select **"GitHub Actions"**
3. Click **Save**

### 7. Wait for Deployment
- Go to the **Actions** tab in your repository
- Wait for the workflow to complete (usually 2-3 minutes)
- Your site will be live at: **https://mananacharam.github.io**

## ✅ What's Already Configured

- ✅ GitHub Actions workflow (`.github/workflows/deploy.yml`)
- ✅ Vite config with correct base path
- ✅ Public folder with `wards_data.json`
- ✅ All necessary build scripts

## 📝 Notes

- The site will automatically rebuild and deploy whenever you push to the `main` branch
- The `dist/` folder is in `.gitignore` (GitHub Actions builds it fresh each time)
- Your data file (`wards_data.json`) is in the `public/` folder and will be copied to the root during build

## 🔄 Updating the Site

After making changes:
```bash
git add .
git commit -m "Your update message"
git push origin main
```

The site will automatically update in a few minutes!

