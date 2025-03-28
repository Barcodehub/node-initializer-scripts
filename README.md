# Automation Scripts for React and Express Projects

This repository contains two Python scripts to automate the setup of modern web development projects:

1. **React + Vite + TypeScript + SWC + Tailwind CSS**: A script to create a React project with Vite, TypeScript, SWC, and optional Tailwind CSS and React Router DOM.
2. **Express + TypeScript**: A script to create an Express project with TypeScript, MongoDB (Mongoose), and environment variables support.

These scripts are designed to save time and ensure consistent project setups.

## Features

### React + Vite + TypeScript + SWC + Tailwind CSS
- Creates a React project with Vite, TypeScript, and SWC.
- Optionally installs Tailwind CSS (version 3 or 4) and React Router DOM.
- Automatically removes unnecessary files and configures Tailwind CSS.
- Sets up a basic `App.tsx` and removes unused CSS imports.

### Express + TypeScript
- Creates an Express project with TypeScript.
- Configures `tsconfig.json` for modern TypeScript features.
- Sets up a basic Express server with CORS, environment variables, and MongoDB (Mongoose) support.
- Adds development scripts for `nodemon`, `ts-node`, and production builds.

---

## Prerequisites

Before using these scripts, ensure you have the following installed:

- [Python](https://www.python.org/) (v3.6 or higher)
- [Node.js](https://nodejs.org/) (v16 or higher)
- [npm](https://www.npmjs.com/) (usually comes with Node.js)

---