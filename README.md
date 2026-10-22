# My Wealth: put it online and build the Android app

All files are in one flat folder so they upload easily from a phone.

1. Create a free GitHub account, then a new PUBLIC repository named my-wealth.
2. Add file > Upload files. Upload every file here EXCEPT update.yml and apk.yml. Commit.
3. Add file > Create new file. In the name box type: .github/workflows/update.yml
   Paste the full text of update.yml from this folder. Commit.
4. Do the same with the name .github/workflows/apk.yml and the text of apk.yml.
5. Settings > Pages > Source: Deploy from a branch > main > / (root) > Save. After a minute your link is https://YOURNAME.github.io/my-wealth/
6. Settings > Actions > General > Workflow permissions > Read and write > Save.
7. Actions tab > Update NAV > Run workflow. Then check data.json for a new line.
8. Actions tab > Build APK > Run workflow. Wait about 5 to 10 minutes. Open the finished run and download my-wealth-apk at the bottom. Unzip it, install app-debug.apk on your phone (allow installs from this source).

Notes
- The APK opens your hosted page, so page changes appear without rebuilding. It needs internet.
- Typed NAVs are saved inside the app on that phone.
- If Update NAV prints "price not found", Al Meezan changed its site layout. Tell Claude.
