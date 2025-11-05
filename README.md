# 🧭 IOPS Git Version Control Guide

### Author: Ian Alt ([ian.alt@orange.com](mailto:ian.alt@orange.com))
### Purpose: Define good practices and a standard Git workflow for all team projects.

---

## 📘 Overview

This guide establishes consistent practices for version control using **Git**. It helps ensure that all developers follow the same conventions for branching, commits, and pull requests, leading to cleaner collaboration and simpler project management.

---

## 🧱 Core Principles

1. **One feature/fix per branch** — keep branches focused and small.  
2. **Never commit directly to `main` or `development`**.  
3. **Always use clear, consistent branch names**.  
4. **Write meaningful commit messages**.  
5. **Create Merge Requests (MRs) early for visibility and feedback**.  
6. **Keep commits and branches synchronized with the remote repository**.  

---

## 🌿 Branching Strategy

Our intent is to follow a **feature-based branching model** inspired by GitHub Flow, adapted for monorepos.

### 🔤 Branch Naming Convention

```
project_name/work_type/task_name
```

**Examples:**
- `datahub/feature/authentication`
- `pigeon/fix/send-notification`
- `was-tool/refactor/departments-page`

### Work Types
| Type | Purpose | Example |
|------|----------|----------|
| **feature** | New functionality | `datahub/feature/authentication` |
| **fix** | Bug or issue fix | `pigeon/fix/send-notification` |
| **refactor** | Code improvements or restructuring, without impacting core functionality | `was-tool/refactor/departments-page` |

---

## 🪜 Standard Git Workflow

Here’s the **step-by-step guide** for daily development.

---

### 1. **Update Your Local Repository**

Before starting any new work:
```bash
git switch main
git pull origin main
```

This ensures you start from the latest version of the main branch.

---

### 2. **Create a New Branch**

Create a new branch based on `main` (or `development` if your project uses one):

```bash
git switch -c project_name/work_type/task_name
```

**Example:**
```bash
git switch -c datahub/feature/authentication
```

---

### 3. **Implement Your Changes**

Work normally on your code.  
Use small, logical commits — each one should represent a meaningful change.

---

### 4. **Commit Changes**

Follow this pattern for commit messages:

```
[work_type]: short summary

Optional longer description of what and why you changed something.
```

**Examples:**
```
feature: add login endpoint for user authentication
fix: correct typo in signup response message
refactor: extract user validation logic to separate module
```

**Commands:**
```bash
git add .
git commit -m "feature: add login endpoint for user authentication"
```

---

### 5. **Sync Your Branch (Optional but Recommended)**

If the main branch has moved forward:
```bash
git fetch origin
git rebase origin/main
```
_Or:_
```bash
git merge origin/main
```

Resolve any conflicts before proceeding.

---

### 6. **Push Your Branch**

```bash
git push -u origin project_name/work_type/task_name
```

**Example:**
```bash
git push -u origin datahub/feature/authentication
```

---

### 7. **Create a Merge Request (PR)**

Once pushed, open a Merge Request (MR) on GitLab.

#### **PR Title Convention**
```
project_name/work_type/task_name
```

**Example:**
```
datahub/feature/authentication
```

#### **MR Description Template**
- **Summary**: Briefly explain what this PR does.  
- **Related Issue**: (Optional) Link to task/issue ID.  
- **Changes**: (Optional) List major modifications.  
- **Tests**: (Optional) Describe how you tested the feature.  

---

### 8. **Code Review**

- At least **one reviewer** must approve the PR.  
- Fix review comments and **push updates** to the same branch:
  ```bash
  git add .
  git commit -m "fix: update login validation based on review"
  git push
  ```

---

### 9. **Merge the MR**

Once approved and all checks pass:
- Squash commits if appropriate (to maintain a clean history).
- Merge into `main` or `development` (depending on the release flow).
- Delete the branch after merging (to keep the repository tidy).

---

### 10. **Pull the Latest Main**

After merging:
```bash
git switch main
git pull origin main
```

---

## 🔄 Recommended Branch Flow Example

```text
main
 └── development
   └── datahub/feature/authentication
   └── datahub/fix/loading-button
   └── datahub/refactor/reports-page
```

Each branch → Merge Request → Merge → Delete branch.

---

## 🧹 Suggested Additional Best Practices

✅ **Use .gitignore** — avoid committing environment files, secrets, or dependencies.  
✅ **Avoid force pushing** to shared branches.  
✅ **Write atomic commits** — small, self-contained, and reversible.  
✅ **Keep branches short-lived** — merge within a few days whenever possible.  

---

## 🧩 Example Summary

| Action | Command Example |
|--------|-----------------|
| Create branch | `git switch -c datahub/feature/authentication` |
| Add changes | `git add .` |
| Commit | `git commit -m "feature: add authentication middleware"` |
| Push | `git push -u origin datahub/feature/authentication` |
| Rebase | `git fetch origin && git rebase origin/main` |
| Merge via MR | Done in GitLab platform |
