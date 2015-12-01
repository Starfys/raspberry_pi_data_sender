#!/bin/bash
echo "Run this from the repository"
cp gathering_script.service /etc/systemd/system/
systemctl enable gathering_script
