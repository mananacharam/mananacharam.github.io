# Mana Nacharam - Voter Information System

A modern Vue.js application for searching voters and viewing statistics for Mana Nacharam Village.

🌐 **Live Site**: [https://mananacharam.github.io](https://mananacharam.github.io)

## Features

- 🔍 **Search Voters**: Search by name or EPIC number
- 📊 **Dashboard**: View comprehensive statistics including:
  - Total male, female, and other voters
  - Ward-wise breakdown
  - Percentage distributions
- 🎨 **Modern UI**: Beautiful, responsive design with gradient backgrounds
- ⚡ **Fast Performance**: Built with Vite for optimal performance

## Installation

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

3. Open your browser and navigate to `http://localhost:3000`

## Build for Production

```bash
npm run build
```

The built files will be in the `dist` directory.

## Deployment to GitHub Pages

This project is automatically deployed to GitHub Pages using GitHub Actions.

### Automatic Deployment

1. Push your changes to the `main` branch
2. GitHub Actions will automatically build and deploy the site
3. The site will be available at: `https://mananacharam.github.io`

### Manual Deployment

If you need to deploy manually:

1. Build the project:
```bash
npm run build
```

2. Copy the contents of the `dist` folder to the `gh-pages` branch (or configure GitHub Pages to use the `dist` folder from the main branch)

### GitHub Pages Configuration

1. Go to your repository settings
2. Navigate to "Pages" section
3. Under "Source", select "GitHub Actions"
4. The workflow will automatically deploy on every push to `main` branch

## Project Structure

```
├── src/
│   ├── components/
│   │   ├── SearchVoters.vue    # Search functionality
│   │   └── Dashboard.vue       # Statistics dashboard
│   ├── App.vue                 # Main app component
│   ├── main.js                 # App entry point
│   └── style.css               # Global styles
├── wards_data.json             # Voter data
├── index.html                  # HTML template
├── vite.config.js              # Vite configuration
└── package.json                # Dependencies
```

## Usage

### Search Voters
1. Click on "🔍 Search Voters" tab
2. Select search type (Name or EPIC No.)
3. Enter your search query
4. View results with complete voter details

### Dashboard
1. Click on "📈 Dashboard" tab
2. View overall statistics
3. Check ward-wise breakdown in the table

## Technologies Used

- Vue 3 (Composition API)
- Vite
- Modern CSS with CSS Variables
- Google Fonts (Inter)

## Data Source

The application uses `wards_data.json` which contains voter information for all 10 wards of Nacharam Gram Panchayat.

