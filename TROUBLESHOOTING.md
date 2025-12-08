# Troubleshooting GitHub Pages Deployment

## Error: "Failed to resolve module specifier 'vue'"

This error occurs when the browser tries to load source files instead of the built/bundled files.

### Common Causes:

1. **Testing locally by opening `index.html` directly**
   - ❌ Don't open `index.html` from the source folder
   - ✅ Use `npm run preview` to test the production build
   - ✅ Or use `npm run dev` for development

2. **GitHub Pages deployment not complete**
   - Wait 2-3 minutes after pushing to GitHub
   - Check the Actions tab to ensure deployment completed successfully
   - Clear browser cache and hard refresh (Ctrl+Shift+R)

3. **GitHub Pages serving wrong files**
   - Ensure GitHub Pages source is set to "GitHub Actions" (not "Deploy from a branch")
   - Verify the workflow completed successfully

### Solution:

The built files in `dist/` folder are correct. The GitHub Actions workflow will:
1. Build the app (bundling Vue and all dependencies)
2. Deploy only the `dist/` folder contents
3. Serve the bundled JavaScript files (not source files)

### Verify Deployment:

1. Check Actions tab: https://github.com/mananacharam/mananacharam.github.io/actions
2. Ensure the workflow shows green checkmark
3. Visit: https://mananacharam.github.io
4. Open browser console (F12) and check for errors
5. Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)

### If Error Persists:

1. **Rebuild and redeploy:**
   ```bash
   npm run build
   git add dist/
   git commit -m "Rebuild for GitHub Pages"
   git push origin main
   ```

2. **Check browser console:**
   - Open DevTools (F12)
   - Check Network tab to see which files are being loaded
   - Verify `/assets/index-*.js` files are loading (not `/src/main.js`)

3. **Verify GitHub Pages settings:**
   - Go to Settings > Pages
   - Source should be "GitHub Actions"
   - Not "Deploy from a branch"

