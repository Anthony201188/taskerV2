# Guide to Creating CRUD Operations with Google Sheets API using FastAPI

## Table of Contents
- [Guide to Creating CRUD Operations with Google Sheets API using FastAPI](#guide-to-creating-crud-operations-with-google-sheets-api-using-fastapi)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Step 1: Set Up a Google Cloud Project](#step-1-set-up-a-google-cloud-project)
  - [Step 2: Enable the Google Sheets API](#step-2-enable-the-google-sheets-api)
  - [Step 3: Create OAuth 2.0 Credentials](#step-3-create-oauth-20-credentials)
  - [Step 4: Install Dependencies](#step-4-install-dependencies)

## Introduction
This guide will walk you through the process of creating CRUD operations with FastAPI and the Google Sheets API. We will set up OAuth 2.0 authentication and interact with a Google Sheet to perform Create, Read, Update, and Delete (CRUD) operations.

## Step 1: Set Up a Google Cloud Project
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project by clicking on **Select a Project** > **New Project**.
3. Give your project a name and select the billing account and location.
4. Click **Create** to finish setting up the project.

## Step 2: Enable the Google Sheets API
1. In the Google Cloud Console, navigate to **APIs & Services** > **Library**.
2. Search for **Google Sheets API** in the search bar.
3. Click on **Google Sheets API**, then click **Enable**.

## Step 3: Create OAuth 2.0 Credentials
1. Go to **APIs & Services** > **Credentials** in the Google Cloud Console.
2. Under **Credentials**, click **Create Credentials** and select **OAuth 2.0 Client IDs**.
3. Set the **Application type** to **Web application**.
4. Under **Authorized redirect URIs**, add `http://localhost:8000/callback` (or the URL you will use to handle the OAuth callback).
5. Click **Create**, then download the credentials as `credentials.json`.

## Step 4: Install Dependencies
You need to install the necessary libraries to interact with the Google Sheets API and FastAPI.

Run the following commands to install the dependencies:
```bash
pip install fastapi uvicorn google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
