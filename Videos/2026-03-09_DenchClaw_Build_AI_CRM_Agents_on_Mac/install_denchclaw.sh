#!/bin/bash

# DenchClaw Installation Script
# This script automates the installation of Rust and DenchClaw on macOS.
# Run with: ./install_denchclaw.sh

set -e  # Exit on any error

# Check if Rust is installed
if ! command -v rustc &> /dev/null; then
    echo "Installing Rust..."
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
    source $HOME/.cargo/env
else
    echo "Rust is already installed."
fi

# Clone DenchClaw repo
if [ ! -d "denchclaw" ]; then
    echo "Cloning DenchClaw repository..."
    git clone https://github.com/DenchHQ/denchclaw
else
    echo "DenchClaw repository already exists."
fi

# Navigate and build
cd denchclaw
cargo build --release

# Verify installation
echo "Verifying installation..."
./target/release/denchclaw --version

# Run doctor check
echo "Running system checks..."
./target/release/denchclaw doctor

echo "Installation complete! Initialize with: ./target/release/denchclaw init --name mycrm"