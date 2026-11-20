#! /bin/bash

set -euo pipefail

usage() {
    cat <<EOF
Usage: $0 <target_ip> <nse_script> [extra_nmap_flags]

EOF
    exit 1
}


if [[ $# -lt 2 ]]; then
    usage
fi

TARGET="$1"
SCRIPT="$2"
shift 2
EXTRA_FLAGS=("$@")


if ! command -v nmap >/dev/null 2>&1; then
    echo "[!] Error: 'nmap' is not installed or not in PATH." >&2
    exit 1
fi


if [[ ! "$TARGET" =~ ^[a-zA-Z0-9._:/-]+$ ]]; then
    echo "[!] Error: Invalid target format: '$TARGET'" >&2
    exit 1
fi

if [[ ! "$SCRIPT" =~ ^[a-zA-Z0-9,._-]+$ ]]; then
    echo "[!] Error: Invalid NSE script name format: '$SCRIPT'" >&2
    exit 1
fi

echo "[*] Target     : $TARGET"
echo "[*] NSE Script : $SCRIPT"
if [[ ${#EXTRA_FLAGS[@]} -gt 0 ]]; then
    echo "[*] Extra Flags: ${EXTRA_FLAGS[*]}"
fi
echo "[*] Running Nmap scan..."
echo "----------------------------------------"


if [[ ${#EXTRA_FLAGS[@]} -gt 0 ]]; then
    nmap --script "$SCRIPT" "${EXTRA_FLAGS[@]}" "$TARGET"
else
    nmap --script "$SCRIPT" "$TARGET"
fi