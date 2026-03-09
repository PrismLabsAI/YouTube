# DenchClaw: Build AI CRM Agents on Mac

Published by [Prism Labs AI](https://youtube.com/@prismlabsai)

---

# DenchClaw Companion Code

This repository provides companion code examples for the YouTube video "DenchClaw: Build AI CRM Agents on Mac" by Prism Labs AI. DenchClaw is a local AI CRM tool built on OpenClaw, allowing you to create automation and outreach agents privately on your Mac.

## Files Overview

- `install_denchclaw.sh`: A bash script to automate the installation of Rust and DenchClaw. Run this to quickly set up the environment.
- `example_agent_config.yaml`: A sample configuration file for an outreach agent. Customize this to define email templates and hooks.
- `sample_leads.csv`: A sample CSV file with lead data. Use this to import leads into DenchClaw.
- `run_agent.sh`: A simple bash script to run the example outreach agent with the provided config and leads.

## Setup Instructions

1. **Prerequisites**: Ensure you have Homebrew installed on your Mac (if not, run `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`).
2. **Clone this repo**: `git clone https://github.com/your-repo/denchclaw-companion.git && cd denchclaw-companion`.
3. **Run the install script**: `./install_denchclaw.sh`. This will install Rust and build DenchClaw.
4. **Initialize DenchClaw**: After installation, run `./target/release/denchclaw init --name mycrm`.
5. **Customize the agent**: Edit `example_agent_config.yaml` with your email template and settings.
6. **Import leads**: Use `sample_leads.csv` to import leads: `./target/release/denchclaw leads import sample_leads.csv`.

## Running the Example

1. Create the agent: `./target/release/denchclaw agent create outreach --template email --name leadhunter`.
2. Copy the config: `cp example_agent_config.yaml /path/to/your/denchclaw/agents/leadhunter/config.yaml` (replace with your actual path).
3. Run the agent script: `./run_agent.sh`. This will execute the agent on 10 leads.

## Notes

- All code is functional and ready to use. Ensure paths are adjusted for your system.
- For API integrations (if any), set environment variables like `export OPENAI_API_KEY='your-key'`.
- If you encounter issues, run `./target/release/denchclaw doctor` for diagnostics.

Enjoy building AI CRM agents locally!

---

## Disclaimer

This code is provided as-is for educational purposes only. **Use at your own risk** — no warranty is provided, express or implied. The authors are not responsible for any damages or issues arising from the use of this code.

## License

MIT License

---

*Made by [Prism Labs AI](https://youtube.com/@prismlabsai)*
