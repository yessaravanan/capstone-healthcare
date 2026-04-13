# 🚀 Streamlit Cloud Deployment Guide

## Deploy to Streamlit Community Cloud (FREE)

Your Healthcare Risk Prediction Dashboard is ready to deploy to Streamlit's free tier!

---

## 📋 Pre-Deployment Checklist

✅ Code pushed to GitHub  
✅ `requirements.txt` exists with dependencies  
✅ `dashboard.py` is the main file  
✅ CSV data files are committed  

---

## 🎯 Step-by-Step Deployment (5 minutes)

### Step 1: Go to Streamlit Cloud
Visit: https://share.streamlit.io

### Step 2: Sign In with GitHub
- Click **"Sign in with GitHub"**
- Authorize Streamlit to access your repositories

### Step 3: Click "New app"
- Button is in the top-left or center of page

### Step 4: Select Your Repository
- **Repository:** `yessaravanan/capstone-healthcare`
- **Branch:** `main`
- **Main file path:** `dashboard.py`

### Step 5: Click "Deploy"
- Streamlit will build and launch your app
- This takes 1-3 minutes

### Step 6: Your Live URL
Once deployed, your app will be live at:
```
https://capstone-healthcare.streamlit.app
```

---

## ✨ What Happens Automatically

✅ **Auto-Deploy:** Every time you push to GitHub, Streamlit auto-redeploys  
✅ **Free Tier:** Unlimited apps, no credit card needed  
✅ **HTTPS:** Secure connection included  
✅ **Custom Domain:** Optional (paid feature)  

---

## 🔧 Post-Deployment

### View Logs
- Click **Settings** (⚙️) in app header
- Click **Logs** to debug issues

### Share Your App
- Copy URL: `https://capstone-healthcare.streamlit.app`
- Share on LinkedIn, GitHub, portfolio, etc.

### Update Your Project
```bash
# Make changes locally
git add .
git commit -m "Update dashboard"
git push origin main

# Streamlit auto-deploys! ✨
# Check status at https://share.streamlit.io
```

---

## 📊 Expected Performance

| Metric | Value |
|--------|-------|
| Load Time | 3-5 seconds |
| Cost | FREE ✅ |
| Uptime | 99.9% |
| Max Inactivity | 7 days (free tier) |

---

## ⚠️ Free Tier Limits

- **Inactivity:** App sleeps after 7 days of no activity (restart on visit)
- **Compute:** Shared resources (not an issue for demos)
- **Storage:** No persistent storage (data in memory only)

---

## 🎓 Your Deployment Commands

```bash
# These commands already done ✅
git init                           # Initialize repo
git add .                          # Stage files
git commit -m "Initial commit"     # Create commit
git push origin main               # Push to GitHub

# Then go to: https://share.streamlit.io
# Select your repo, click Deploy
# Done! 🎉
```

---

## 📱 Test Your App

After deployment, test these features:

- [ ] Dashboard loads without errors
- [ ] KPI metrics display correctly
- [ ] Charts render (Risk Distribution, Score Distribution)
- [ ] Filters work (Risk Level, Age Range, Sex)
- [ ] Patient table displays with color-coding
- [ ] Anomaly Report shows flagged cases
- [ ] LLM Summary loads for selected patients

---

## 🆘 Troubleshooting

### "Module not found" error
→ Check `requirements.txt` has all packages  
→ Push fix to GitHub, Streamlit auto-redeploys

### "CSV files not found"
→ Make sure all `.csv` files are committed to GitHub  
→ Check file paths in `dashboard.py` match actual filenames

### "App takes too long to load"
→ Free tier may be slower initially  
→ App caches data after first load (faster on refresh)

### "App goes to sleep"
→ Normal on free tier (7-day inactivity)  
→ Restarts automatically when you visit

---

## 📊 Monitoring

Once deployed, check your app status:

1. Go to: https://share.streamlit.io
2. Click your app in the list
3. View logs, resource usage, deployment history

---

## 🎉 Success!

Once deployed, your app will be live and accessible worldwide!

**Your Demo URL:** `https://capstone-healthcare.streamlit.app`

Share it on:
- 📌 LinkedIn
- 🐙 GitHub repo README
- 📧 Email to stakeholders
- 💼 Portfolio website

---

## Next Steps (Optional)

- **Custom Domain:** Upgrade to paid tier
- **Private Sharing:** Restrict to specific users
- **Monitoring:** Set up alerts & analytics
- **Enhancements:** Add more features based on feedback

---

**Status:** Ready to deploy! 🚀  
**Time to deploy:** 5 minutes  
**Cost:** FREE ✅  
**Go to:** https://share.streamlit.io
