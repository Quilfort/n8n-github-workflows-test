# n8n GitHub Workflows Test

This repository demonstrates how to connect GitHub with n8n using webhooks to trigger automated workflows when code is pushed.

## Purpose

This project serves as a testing ground for integrating n8n workflows with GitHub Actions. When code is pushed to the repository, a GitHub Action workflow sends commit information to an n8n webhook, which can then trigger various automated tasks.

## Setup Requirements

### GitHub Secret

To use this integration, you need to set up a repository secret:

- **Secret Name**: `N8N_WEBHOOK_URL`
- **Value**: Your n8n webhook URL

This secret is used in the GitHub workflow to securely send data to your n8n instance without exposing the webhook URL in the code.

## GitHub Workflow

The repository includes a GitHub Actions workflow file (`.github/workflows/send_email_commit.yml`) that:

- Triggers when code is pushed to the main branch
- Extracts information about the latest commit (message, author, hash)
- Sends this data to your n8n webhook URL

## Test Project: Cool Name Speller 3000

The `cool_name_speller_3000` directory contains a simple Python project that was created as part of testing this workflow. It's an ASCII art name spelling program with colorful terminal output.

This Python project was developed with AI assistance and serves as a demonstration codebase for triggering the GitHub Actions workflow. It's not the main focus of this repository but provides a practical example of code that can trigger the workflow when pushed to GitHub.

### Running the Cool Name Speller

```bash
cd cool_name_speller_3000
python main.py
```

Or spell a specific name:

```bash
python main.py "Your Name"
```

## Testing the Integration

1. Make changes to any file in the repository
2. Commit and push to the main branch
3. The GitHub Action will automatically run and send commit data to your n8n webhook
4. Check your n8n workflow to see the received data and any actions it triggered
