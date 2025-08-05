# 🐘 PostgreSQL & pgAdmin Setup Guide for ML Projects

This guide will help you install PostgreSQL and pgAdmin, set up your database, and get started with Feast for feature store management.  
**Follow these steps if you are new to PostgreSQL!**

---

## 1️⃣ Install PostgreSQL and pgAdmin

1. **Download the installer:**  
   [https://www.postgresql.org/download/windows/](https://www.postgresql.org/download/windows/)

2. **Run the installer:**  
   - Accept defaults unless you have specific needs.
   - **Set a password** for the `postgres` superuser (remember this!).
   - Make sure **pgAdmin** is selected for installation.

3. **Finish installation.**

---

## 2️⃣ Add PostgreSQL to your PATH (Optional but recommended)

If `psql` is not recognized in Command Prompt:

- Open **Start Menu** → search for **Environment Variables** → select **Edit the system environment variables**.
- Click **Environment Variables**.
- Under **System variables**, select **Path** → **Edit** → **New**.
- Add:  
  ```
  C:\Program Files\PostgreSQL\17\bin
  ```
  (or your installed version)
- Click **OK** and restart your terminal.

---

## 3️⃣ Open pgAdmin and Connect to PostgreSQL

1. **Open pgAdmin** from Start Menu.
2. In the left sidebar, under "Servers", double-click your server (e.g., `PostgreSQL 17`).
3. Enter the password you set during installation.
4. You are now connected!

---

## 4️⃣ Create a Database for Feast

1. In pgAdmin, expand your server → right-click **Databases** → **Create** → **Database...**
2. Name it (e.g.) `feast_offline`.
3. Click **Save**.

---

## 5️⃣ (Optional) Test psql Command Line

Open Command Prompt and run:
```sh
psql -U postgres -d feast_offline
```
- Enter your password if prompted.
- Type `\q` to quit.

---

## 6️⃣ Initialize Feast Feature Store

1. Open a terminal in your project directory.
2. Run:
   ```sh
   feast init feature_store -t postgres
   ```
3. When prompted, enter:
   - **Postgres host:** `localhost`
   - **Postgres port:** `5432`
   - **Postgres DB name:** `feast_offline`
   - **Postgres schema:** `public` (default)
   - **Postgres user:** `postgres` (or your user)
   - **Postgres password:** (the password you set)
   - For uploading example data, press Enter for yes (or `n` for no).

---

## 7️⃣ Troubleshooting

- **Can't connect?**  
  - Make sure PostgreSQL service is running (check in Services or pgAdmin).
  - Double-check your username, password, and database name.
- **psql not found?**  
  - Add PostgreSQL's `bin` folder to your PATH (see step 2).
- **Database does not exist?**  
  - Create it in pgAdmin (see step 4).

---

## 🎉 You're Ready!

You now have PostgreSQL, pgAdmin, and a Feast-ready database set up for your ML project!

---
```<!-- filepath: d:\Projects\MLJourneyE2E\PGSQL_GUIDE.md -->

# 🐘 PostgreSQL & pgAdmin Setup Guide for ML Projects

This guide will help you install PostgreSQL and pgAdmin, set up your database, and get started with Feast for feature store management.  
**Follow these steps if you are new to PostgreSQL!**

---

## 1️⃣ Install PostgreSQL and pgAdmin

1. **Download the installer:**  
   [https://www.postgresql.org/download/windows/](https://www.postgresql.org/download/windows/)

2. **Run the installer:**  
   - Accept defaults unless you have specific needs.
   - **Set a password** for the `postgres` superuser (remember this!).
   - Make sure **pgAdmin** is selected for installation.

3. **Finish installation.**

---

## 2️⃣ Add PostgreSQL to your PATH (Optional but recommended)

If `psql` is not recognized in Command Prompt:

- Open **Start Menu** → search for **Environment Variables** → select **Edit the system environment variables**.
- Click **Environment Variables**.
- Under **System variables**, select **Path** → **Edit** → **New**.
- Add:  
  ```
  C:\Program Files\PostgreSQL\17\bin
  ```
  (or your installed version)
- Click **OK** and restart your terminal.

---

## 3️⃣ Open pgAdmin and Connect to PostgreSQL

1. **Open pgAdmin** from Start Menu.
2. In the left sidebar, under "Servers", double-click your server (e.g., `PostgreSQL 17`).
3. Enter the password you set during installation.
4. You are now connected!

---

## 4️⃣ Create a Database for Feast

1. In pgAdmin, expand your server → right-click **Databases** → **Create** → **Database...**
2. Name it (e.g.) `feast_offline`.
3. Click **Save**.

---

## 5️⃣ (Optional) Test psql Command Line

Open Command Prompt and run:
```sh
psql -U postgres -d feast_offline
```
- Enter your password if prompted.
- Type `\q` to quit.

---

## 6️⃣ Initialize Feast Feature Store

1. Open a terminal in your project directory.
2. Run:
   ```sh
   feast init feature_store -t postgres
   ```
3. When prompted, enter:
   - **Postgres host:** `localhost`
   - **Post port:** `5432`
   - **Postgres DB name:** `feast_offline`
   - **Postgres schema:** `public` (default)
   - **Postgres user:** `postgres` (or your user)
   - **Postgres password:** (the password you set)
   - For uploading example data, press Enter for yes (or `n` for no).

---

## 7️⃣ Troubleshooting

- **Can't connect?**  
  - Make sure PostgreSQL service is running (check in Services or pgAdmin).
  - Double-check your username, password, and database name.
- **psql not found?**  
  - Add PostgreSQL's `bin` folder to your PATH (see step 2).
- **Database does not exist?**  
  - Create it in pgAdmin (see step 4).

---

## 🎉 You're Ready!

You now have PostgreSQL, pgAdmin, and a Feast-ready database set up for your ML project!