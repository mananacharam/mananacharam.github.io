# GitHub Pages Deployment Guide

This guide will help you deploy the Mana Nacharam Voter Information System to GitHub Pages.

## Prerequisites

- A GitHub account
- Git installed on your local machine
- Node.js and npm installed

## Step 1: Initialize Git Repository (if not already done)

```bash
git init
git add .
git commit -m "Initial commit"
```

## Step 2: Add GitHub Remote

```bash
git remote add origin https://github.com/mananacharam/mananacharam.github.io.git
```

## Step 3: Push to GitHub

```bash
git branch -M main
git push -u origin main
```

## Step 4: Enable GitHub Pages

1. Go to your repository on GitHub: https://github.com/mananacharam/mananacharam.github.io
2. Click on **Settings** tab
3. Scroll down to **Pages** section (in the left sidebar)
4. Under **Source**, select **GitHub Actions**
5. Save the settings

## Step 5: Verify Deployment

1. After pushing to the `main` branch, GitHub Actions will automatically:
   - Build your Vue.js application
   - Deploy it to GitHub Pages
   
2. Check the **Actions** tab in your repository to see the deployment progress

3. Once deployment is complete, your site will be available at:
   **https://mananacharam.github.io**

## Troubleshooting

### If the site doesn't load:

1. Check the Actions tab for any build errors
2. Verify that `wards_data.json` is in the `public/` folder
3. Ensure all file paths are correct (use relative paths)
4. Check browser console for any errors

### If assets don't load:

- Make sure `vite.config.js` has `base: '/'` set
- Verify that all assets are in the `public/` folder
- Check that the build completed successfully

## Updating the Site

Simply push changes to the `main` branch:

```bash
git add .
git commit -m "Update site"
git push origin main
```

GitHub Actions will automatically rebuild and redeploy the site.

## Local Testing

Before deploying, test the production build locally:

```bash
npm run build
npm run preview
```

This will build and serve the production version locally at `http://localhost:4173`

