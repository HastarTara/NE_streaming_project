#!/bin/bash
echo "Running security checks..."
bandit -r src/
safety check -r requirements.txt
echo "Security checks completed."
