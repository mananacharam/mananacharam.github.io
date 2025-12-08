# Fix GitHub Pages Deployment Issue

## Problem
The error "Failed to resolve module specifier 'vue'" occurs because GitHub Pages is serving the source `index.html` file instead of the built files from GitHub Actions.

## Solution Steps

### 1. Verify GitHub Pages Settings

Go to your repository settings:
- Navigate to: https://github.com/mananacharam/mananacharam.github.io/settings/pages
- Under "Source", make sure it says **"GitHub Actions"** (not "Deploy from a branch")
- If it's set to "Deploy from a branch", change it to **"GitHub Actions"**

### 2. Check GitHub Actions Workflow

- Go to: https://github.com/mananacharam/mananacharam.github.io/actions
- Make sure the latest workflow run completed successfully (green checkmark ✓)
- If it failed, click on it to see the error

### 3. If GitHub Actions is Not Enabled

If you don't see "GitHub Actions" as an option in Settings > Pages:

1. Go to Settings > Pages
2. Under "Source", select **"GitHub Actions"**
3. If the option doesn't appear, make sure:
   - The workflow file exists at `.github/workflows/deploy.yml`
   - The workflow has run at least once
   - You have the correct permissions

### 4. Manual Trigger (if needed)

If the workflow hasn't run:
- Go to: https://github.com/mananacharam/mananacharam.github.io/actions
- Click on "Deploy to GitHub Pages" workflow
- Click "Run workflow" button
- Select "main" branch and click "Run workflow"

### 5. Wait for Deployment

After changing settings or triggering the workflow:
- Wait 2-5 minutes for deployment to complete
- Check the Actions tab for completion status
- Visit: https://mananacharam.github.io
- Hard refresh: `Ctrl + Shift + R` (Windows) or `Cmd + Shift + R` (Mac)

## Verification

After deployment completes, the site should:
- Load without errors
- Show the voter search interface
- Have Google Analytics tracking enabled

If you still see the error, the browser might be caching the old version. Try:
- Hard refresh: `Ctrl + Shift + R`
- Clear browser cache
- Open in incognito/private mode

